# Datos procesados

Esta carpeta contendrá datasets derivados y listos para análisis o Machine Learning.

El dataset tabular final deberá poder reconstruirse mediante código a partir de las fuentes documentadas. La unidad de análisis prevista es una celda espacial dentro de un potrero, con variables multitemporales cuando corresponda.

Esquema preliminar de columnas:

- `potrero_id`
- coordenadas o identificador de celda
- fecha/campaña
- variables SAR
- variables topográficas
- variables de suelo
- variables de manejo
- variable objetivo, únicamente si existe una medición real y válida

No se incorporarán targets simulados como sustituto de observaciones de campo.
