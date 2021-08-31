IGNORED_SCHEMAS = ["pg_catalog", "information_schema"]

IGNORED_TABLES = [
    "spatial_ref_sys",
    "t_ili2db_import_object",
    "t_ili2db_attrname",
    "t_ili2db_settings",
    "t_ili2db_import",
    "t_ili2db_inheritance",
    "t_ili2db_model",
    "t_ili2db_classname",
    "t_ili2db_import_basket",
    "T_ILI2DB_TABLE_PROP",
    "T_ILI2DB_INHERITANCE",
    "T_ILI2DB_ATTRNAME",
    "T_ILI2DB_SETTINGS",
    "T_KEY_OBJECT",
    "T_ILI2DB_MODEL",
    "T_ILI2DB_IMPORT",
    "T_ILI2DB_TRAFO",
    "T_ILI2DB_COLUMN",
    "T_ILI2DB_COLUMN_PROP",
    "T_ILI2DB_CLASSNAME",
    "T_ILI2DB_IMPORT_OBJECT",
    "T_ILI2DB_IMPORT_BASKET",
    "T_ILI2DB_META_ATTRS",
    "ogr_empty_table",
    "gm_curve2dlistvalue",
    "gm_curve3dlistvalue",
    "gm_multicurve2d",
    "gm_multicurve3d",
    "gm_surface2dlistvalue",
    "gm_surface3dlistvalue",
    "gm_multisurface2d",
    "gm_multisurface3d",
    "gpkg_contents",
    "gpkg_data_column_constraints",
    "gpkg_data_columns",
    "gpkg_geometry_columns",
    "gpkg_extensions",
    "gpkg_spatial_ref_sys",
    "gpkg_ogr_contents",
    "gpkg_tile_matrix_set",
    "gpkg_tile_matrix",
    "gpkg_metadata",
    "gpkg_metadata_reference",
    "sqlite_sequence",
]

BASKET_TABLES = [
    "t_ili2db_basket",
    "T_ILI2DB_BASKET",
    "t_ili2db_dataset",
    "T_ILI2DB_DATASET",
]

IGNORED_ILI_ELEMENTS = [
    "GeometryCHLV03_V1.MultiSurface",
    "GeometryCHLV03_V1.MultiLine",
    "GeometryCHLV03_V1.MultiDirectedLine",
    "GeometryCHLV95_V1.MultiSurface",
    "GeometryCHLV95_V1.MultiLine",
    "GeometryCHLV95_V1.MultiDirectedLine",
    "CatalogueObjects_V1.Catalogues.CatalogueReference",
    "CatalogueObjects_V1.Catalogues.MandatoryCatalogueReference",
    "LocalisationCH_V1.MultilingualMText",
    "LocalisationCH_V1.MultilingualText",
    "LocalisationCH_V1.LocalisedMText",
    "LocalisationCH_V1.LocalisedText",
]
