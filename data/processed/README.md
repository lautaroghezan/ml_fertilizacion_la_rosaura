# Datos procesados

Esta carpeta contendrá datasets derivados y listos para análisis o Machine Learning.

El dataset tabular final deberá poder reconstruirse mediante código a partir de las fuentes documentadas. La unidad de análisis prevista es una celda espacial dentro de un potrero, observada en una o más fechas.

## Esquema mínimo de trazabilidad

- `potrero_id`
- `pixel_id` o coordenadas de la celda
- `fecha`
- `campania`
- `product_id`

## Variables SAR esperadas

- `sigma0_hh_db`
- `sigma0_hv_db`
- `sigma0_vh_db`
- `sigma0_vv_db`
- diferencias/razones derivadas con justificación
- estadísticos temporales por unidad espacial

El primer producto de referencia es `EOL1DSARSAO1A14948810`, con resolución aproximada de 43,55 × 42,33 m y `Sigma0Type=AMPLITUDE`.

## Variables auxiliares previstas

- elevación, pendiente y relieve relativo;
- variables de suelo;
- fecha de siembra y manejo;
- fertilización aplicada;
- clima/precipitaciones;
- variables productivas observadas.

## Variable objetivo

Sólo se incorporará una variable objetivo si existe una medición real y metodológicamente válida. No se usarán targets simulados para completar el trabajo.

## Formatos recomendados

- CSV o Parquet para datasets tabulares;
- GeoPackage/GeoJSON para resultados espaciales livianos;
- GeoTIFF para productos raster cuando sea necesario, sin versionar archivos pesados en Git.
