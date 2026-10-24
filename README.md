# ML para fertilización selectiva — La Rosaura

Proyecto final de Machine Learning aplicado a la identificación de ambientes de manejo para fertilización selectiva de maíz en **La Rosaura**, partido de Tandil, provincia de Buenos Aires, Argentina.

## 1. Problema y objetivo

El proyecto busca construir una metodología cuantitativa, reproducible y espacialmente explícita para caracterizar la variabilidad dentro de los potreros de maíz y generar ambientes de manejo como soporte para futuras decisiones de fertilización diferencial.

El modelo **no inferirá directamente una dosis de fertilizante desde una imagen radar**. Primero se identificarán y validarán ambientes; la dosis será una decisión agronómica posterior que requerirá suelo, manejo, objetivo productivo y respuesta observada.

## 2. Pregunta de investigación

> ¿Es posible identificar ambientes de manejo espacialmente diferenciados dentro de los potreros de maíz de La Rosaura mediante la combinación de información SAR multitemporal SAOCOM, variables topográficas y datos agronómicos utilizando técnicas de Machine Learning?

## 3. Geometría maestra del establecimiento

El 24/10/2026 se confirmó manualmente el polígono aproximado de La Rosaura. Esta geometría es la referencia espacial común entre este repositorio y `proyecto-saocom`.

Coordenadas originales (latitud, longitud):

```text
-37.204333, -59.346855
-37.198350, -59.339680
-37.211288, -59.322638
-37.217224, -59.329805
-37.204333, -59.346855
```

Representación WKT en orden longitud, latitud:

```text
POLYGON((-59.346855 -37.204333, -59.339680 -37.198350, -59.322638 -37.211288, -59.329805 -37.217224, -59.346855 -37.204333))
```

Todo dataset geoespacial que ingrese al modelo deberá verificar intersección y coherencia con esta geometría. Los futuros límites de los 16 potreros deberán quedar contenidos o justificadamente vinculados a ella.

## 4. Producto SAOCOM real validado

- Product ID: `EOL1DSARSAO1A14948810`
- adquisición: **07/09/2024**
- nivel: **L1D**
- modo: **TOPSAR / TNB**
- polarización: **QP — HH, HV, VH y VV**
- GeoTIFF FLOAT32 sin extensión `.tif`
- CRS: **EPSG:32721 — WGS84 / UTM 21S**
- dimensiones: **4.396 × 7.104 píxeles**
- resolución: aproximadamente **43,55 × 42,33 m**
- `Sigma0Type = AMPLITUDE`

Para valores positivos y válidos:

```text
σ⁰_dB = 20 · log10(amplitud)
```

## 5. Hipótesis

**H1.** La variabilidad espacial y temporal observada mediante SAOCOM, combinada con características topográficas y agronómicas, permite identificar patrones persistentes compatibles con distintos ambientes de manejo.

**H2.** La combinación de información satelital, topográfica y agronómica permite caracterizar los ambientes mejor que una única fuente aislada.

## 6. Estrategia de Machine Learning

### Etapa A — no supervisada

K-Means como baseline, con posibilidad de comparar Gaussian Mixture Models y clustering jerárquico. PCA podrá utilizarse como herramienta exploratoria. Los clusters no se etiquetarán automáticamente como alto/medio/bajo potencial sin evidencia agronómica independiente.

### Etapa B — supervisada

Sólo si existe una variable objetivo real y confiable se compararán modelos baseline, lineales, Random Forest y Gradient Boosting/XGBoost.

## 7. Unidad de análisis y variables

La unidad prevista es una **celda espacial dentro de un potrero**, observada en múltiples fechas.

Variables candidatas:

- `sigma0_hh_db`, `sigma0_hv_db`, `sigma0_vh_db`, `sigma0_vv_db`;
- diferencias/relaciones justificadas entre polarizaciones;
- estadísticos multitemporales;
- elevación, pendiente y posición topográfica;
- suelo, fecha de siembra, híbrido, densidad y fertilización;
- clima/precipitaciones;
- rendimiento o producción de silo cuando exista una medición confiable.

No se asumirán equivalencias directas como HH = humedad, HV = biomasa o radar = dosis.

## 8. Validación

La autocorrelación espacial impide considerar píxeles vecinos como observaciones independientes. Se priorizarán grupos por potrero o bloques espaciales; `GroupKFold` será una alternativa inicial. Cuando existan múltiples campañas, se evaluará también generalización temporal.

## 9. Flujo entre repositorios

```text
proyecto-saocom
   ↓
recorte con geometría maestra
   ↓
GeoTIFF HH/HV/VH/VV + σ⁰ dB
   ↓
ml_fertilizacion_la_rosaura
   ↓
EDA + features + topografía + manejo
   ↓
clustering / modelos supervisados
   ↓
ambientes de manejo validados
```

## 10. Estado actual

- [x] Problema, hipótesis y objetivos definidos.
- [x] Geometría maestra del establecimiento confirmada.
- [x] Primer producto SAOCOM L1D real descargado e inspeccionado.
- [x] HH/HV/VH/VV, CRS, resolución y radiometría confirmados.
- [x] Conversión a dB definida.
- [ ] Ejecutar el recorte definitivo con la geometría maestra.
- [ ] Incorporar límites de los 16 potreros.
- [ ] Identificar potreros de maíz por campaña.
- [ ] Procesar la serie temporal 2024/25.
- [ ] Incorporar DEM/topografía.
- [ ] Incorporar suelo y manejo.
- [ ] Construir dataset analítico.
- [ ] Ejecutar EDA, clustering y validación.

Las conclusiones agronómicas se incorporarán únicamente cuando existan datos observados suficientes para respaldarlas.
