# data/processed

Productos derivados reproducibles; evitar versionar rasters/tablas pesadas.

## A. serie_por_potrero_fecha
Campos mínimos: `potrero_id`, `fecha`, `campania`, `sensor`, `product_id/source_id`, variables, indicadores de calidad. SAOCOM: sigma0 HH/HV/VH/VV y estadísticos. Sentinel-2: reflectancias/índices y calidad de nubes.

## B. uso_historico_potreros
Una fila por `potrero_id × campania`: `cultivo_inferido` (`maiz`, `pastura`, `otro`, `incierto`), `confianza`, `evidencia`, `version_modelo`. Nunca reemplazar incertidumbre por una etiqueta forzada.

## C. dataset_ambientes_maiz
Sólo potreros/campañas de maíz con evidencia suficiente. Campos de trazabilidad: `potrero_id`, `pixel_id` o x/y, `fecha`, `campania`, IDs de fuentes. Features: SAR, ópticas, temporales, DEM, suelo/manejo disponibles y variables históricas de rotación con su procedencia.

Formatos recomendados: Parquet/CSV para tablas, GeoPackage/GeoJSON para vectores y GeoTIFF para rasters. No usar targets simulados.
