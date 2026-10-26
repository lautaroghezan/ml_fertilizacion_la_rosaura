# data/reference

Archivos pequeños y estables que definen referencias del proyecto.

`potreros_la_rosaura.geojson` contiene los 16 polígonos aportados por el productor, normalizados a GeoJSON en orden longitud/latitud y con IDs `L01`–`L16`. Deben tratarse como geometrías maestras para la integración SAOCOM–Sentinel-2 y la trazabilidad por campaña.

No modificar vértices para hacerlos coincidir artificialmente con el perímetro exterior aproximado. Cualquier corrección futura debe provenir de una nueva geometría validada por el productor y quedar documentada.
