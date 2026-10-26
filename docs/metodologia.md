# Metodología

## 1. Unidades espaciales
Usar `L01`–`L16` desde `data/reference/potreros_la_rosaura.geojson`. Todo registro debe conservar `potrero_id`; para análisis interno agregar `pixel_id` o coordenadas.

## 2. Inventario y QC
Registrar `product_id`, sensor, fecha, campaña, CRS, resolución, calidad y transformaciones. SAOCOM piloto: L1D QP, EPSG:32721, ~43,55×42,33 m, `Sigma0Type=AMPLITUDE`; dB = `20*log10(amplitud)` para valores positivos. Sentinel-2 debe conservar métricas/máscaras de nube y calidad.

## 3. Serie multisensor
Construir una tabla `potrero × fecha` con estadísticos SAOCOM y ópticos. No forzar coincidencia exacta de fechas: conservar fecha real de cada observación y derivar atributos temporales de forma reproducible.

## 4. Modelo 1: reconstrucción histórica
Objetivo: `potrero × campaña → maíz/pastura/otro/incierto + confianza`. Usar forma temporal/fenológica (nivel, amplitud, pendientes, máximos/mínimos y fechas características) y complementariedad SAR–óptica. No usar una regla única “más biomasa = maíz”. Validar con cualquier campaña/lote de referencia disponible y mantener `incierto` cuando la evidencia sea insuficiente.

## 5. Features históricas
Derivar, sólo después de clasificar con confianza suficiente: `cultivo_campania_anterior`, `anios_desde_ultimo_maiz`, `n_maiz_ultimas_n_campanias`, conservando probabilidad/confianza de origen.

## 6. Modelo 2: ambientes en maíz
Filtrar potreros/campañas de maíz y construir dataset espacial con SAR multitemporal, Sentinel-2, DEM, suelo y manejo. EDA → features → clustering (K-Means baseline; GMM/jerárquico opcional) → estabilidad espacial/temporal → validación agronómica. Supervisado sólo con target real.

## 7. Validación
Evitar `train_test_split` aleatorio de píxeles como única validación. Usar grupos por potrero o bloques espaciales y generalización temporal entre campañas. Ajustar imputación/escalado dentro de cada fold. Silhouette es diagnóstico interno, no validación agronómica.

## 8. Explicabilidad y límites
SHAP describe el modelo, no causalidad. sigma0 no es humedad/biomasa/rendimiento directo. Los clusters no se etiquetan alto/medio/bajo potencial sin evidencia independiente. Ningún sensor define por sí solo dosis de fertilizante.

## 9. Trazabilidad mínima
`potrero_id`, `fecha`, `campania`, `sensor`, `product_id/source_id`, coordenada/unidad espacial, variables, indicadores de calidad, versión de features/modelo y, para cultivo inferido, clase + confianza.
