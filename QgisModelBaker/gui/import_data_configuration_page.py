# -*- coding: utf-8 -*-
"""
/***************************************************************************
                              -------------------
        begin                : 06.07.2021
        git sha              : :%H$
        copyright            : (C) 2021 by Dave Signer
        email                : david at opengis ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import pathlib
import configparser

from QgisModelBaker.gui.panel.log_panel import LogPanel

from QgisModelBaker.libili2db.ilicache import (
    IliMetaConfigCache,
    IliMetaConfigItemModel,
    MetaConfigCompleterDelegate,
    IliToppingFileCache,
    IliToppingFileItemModel
)
from QgisModelBaker.gui.ili2db_options import Ili2dbOptionsDialog
from QgisModelBaker.gui.options import ModelListView

from qgis.PyQt.QtCore import (
    Qt, 
    QSettings,
    QTimer,
    QEventLoop
)

from qgis.PyQt.QtWidgets import (
    QWizardPage,
    QCompleter,
    QSizePolicy,
    QGridLayout,
    QMessageBox,
    QAction,
    QToolButton,
    QHeaderView
)
from qgis.PyQt.QtGui import QPixmap
from qgis.gui import QgsGui, QgsMessageBar
from qgis.core import QgsCoordinateReferenceSystem
from QgisModelBaker.libili2db.ili2dbconfig import ImportDataConfiguration

from ..utils import get_ui_class

PAGE_UI = get_ui_class('import_data_configuration.ui')

class ImportDataConfigurationPage(QWizardPage, PAGE_UI):

    def __init__(self, parent):
        QWizardPage.__init__(self, parent)
        
        self.setupUi(self)
        self.setFixedSize(1200,800)
        self.setTitle(self.tr("Data import configuration"))
        self.log_panel = LogPanel()
        layout = self.layout()
        layout.addWidget(self.log_panel)
        self.setLayout(layout)

        self.import_wizard = parent
        self.is_complete = True
        
        self.import_wizard.import_data_file_model.sourceModel().setHorizontalHeaderLabels([self.tr('Import File'),self.tr('Dataset')])
        self.file_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.file_table_view.setModel(self.import_wizard.import_data_file_model)
        self.file_table_view.verticalHeader().setSectionsMovable(True)
        self.file_table_view.verticalHeader().setDragEnabled(True)
        self.file_table_view.verticalHeader().setDragDropMode(QHeaderView.InternalMove)

        self.ili2db_options = Ili2dbOptionsDialog()
        self.ili2db_options_button.clicked.connect(self.ili2db_options.open)
        self.ili2db_options.finished.connect(self.fill_toml_file_info_label)

    def fill_toml_file_info_label(self):
        text = None
        if self.ili2db_options.toml_file():
            text = self.tr('Extra Model Information File: {}').format(('…'+self.ili2db_options.toml_file()[len(self.ili2db_options.toml_file())-40:]) if len(self.ili2db_options.toml_file()) > 40 else self.ili2db_options.toml_file())
        self.toml_file_info_label.setText(text)
        self.toml_file_info_label.setToolTip(self.ili2db_options.toml_file())

    def restore_configuration(self):
        self.fill_toml_file_info_label()
        # set chk_delete_data always to unchecked because otherwise the user could delete the data accidentally
        self.chk_delete_data.setChecked(False)

    def update_configuration(self, configuration):
        configuration.inheritance = self.ili2db_options.inheritance_type()
        configuration.tomlfile = self.ili2db_options.toml_file()
        configuration.create_basket_col = self.ili2db_options.create_basket_col()
        configuration.create_import_tid = self.ili2db_options.create_import_tid()
        configuration.stroke_arcs = self.ili2db_options.stroke_arcs()
        configuration.pre_script = self.ili2db_options.pre_script()
        configuration.post_script = self.ili2db_options.post_script()
        configuration.delete_data = self.chk_delete_data.isChecked()