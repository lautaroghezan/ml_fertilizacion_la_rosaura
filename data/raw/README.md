# data/raw

Datos originales pesados; no versionarlos en Git.

Fuentes previstas:
- SAOCOM L1D originales y metadatos;
- Sentinel-2 originales/consultas de reflectancia e índices con información de calidad/nubes;
- DEM;
- análisis de suelo, manejo, clima y producción cuando existan.

Las geometrías pequeñas y estables de los 16 potreros sí se versionan por separado en `data/reference/potreros_la_rosaura.geojson` (`L01`–`L16`).

Producto SAOCOM piloto validado: `EOL1DSARSAO1A14948810`, 07/09/2024, QP HH/HV/VH/VV, EPSG:32721, ~43,55×42,33 m, `Sigma0Type=AMPLITUDE`.

La historia maíz/pastura NO es un dato raw disponible: será una variable inferida por el Modelo 1 y deberá almacenarse con confianza y versión del modelo.
