# Datos raw

Esta carpeta está reservada para datos originales o referencias reproducibles a sus fuentes.

No deben modificarse manualmente los archivos originales. Los productos SAOCOM de gran tamaño no se versionarán directamente en GitHub. Cada fuente incorporada deberá registrar como mínimo: origen, identificador, fecha de adquisición/medición, sistema de referencia espacial cuando corresponda y pasos necesarios para reproducir su obtención.

## Producto SAOCOM de referencia

Primer producto real validado:

- Product ID: `EOL1DSARSAO1A14948810`
- Fecha de adquisición: `2024-09-07`
- Nivel: `L1D`
- Modo: `TOPSAR / TNB`
- Polarizaciones: `HH`, `HV`, `VH`, `VV`
- CRS: `EPSG:32721`
- Resolución aproximada: `43.55 x 42.33 m`
- Tipo de dato: `FLOAT32`
- Metadato: `Sigma0Type=AMPLITUDE`
- Conversión a dB para valores positivos: `20 * log10(amplitud)`

El ZIP original y sus GeoTIFF no deben agregarse al repositorio. La trazabilidad se mantiene mediante Product ID, metadatos y documentación del pipeline de procesamiento.

## Fuentes previstas

- límites de los 16 potreros de La Rosaura;
- identificación de potreros de maíz por campaña;
- variables topográficas / DEM;
- productos SAR SAOCOM;
- análisis de suelo;
- datos de manejo;
- variables productivas medidas en campo.
