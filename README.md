# ML para fertilización selectiva — La Rosaura

Proyecto final de Machine Learning aplicado a la identificación de ambientes de manejo para fertilización selectiva de maíz en el establecimiento **La Rosaura**, partido de Tandil, provincia de Buenos Aires, Argentina.

## 1. Contexto productivo

La Rosaura es un establecimiento agropecuario cuya actividad productiva incluye la producción lechera. Parte de la superficie agrícola se destina a maíz para silo, utilizado como componente de la alimentación del rodeo.

La producción agrícola presenta variabilidad espacial dentro de los potreros. Diferencias de relieve, suelo, disponibilidad hídrica, desarrollo del cultivo y manejo pueden generar sectores con distinto comportamiento agronómico y potencial productivo. Una aplicación uniforme de fertilizante no representa necesariamente esa heterogeneidad.

Este proyecto busca construir una metodología cuantitativa, reproducible y espacialmente explícita que permita caracterizar esa variabilidad y generar ambientes de manejo como soporte para futuras decisiones de fertilización diferencial.

## 2. Problema

Actualmente no se dispone de una metodología cuantitativa y reproducible que permita identificar automáticamente sectores con diferente comportamiento agronómico dentro de los potreros de maíz de La Rosaura y utilizar esa información como soporte para decisiones de fertilización diferenciada.

El objetivo del modelo **no es inferir directamente una dosis de fertilizante a partir de una imagen radar**. La dosis agronómica requiere información adicional, como análisis de suelo, manejo previo, objetivo productivo y respuesta observada. El problema de ML se concentra primero en detectar y caracterizar ambientes espacialmente diferenciados.

## 3. Pregunta de investigación

> ¿Es posible identificar ambientes de manejo espacialmente diferenciados dentro de los potreros de maíz de La Rosaura mediante la combinación de información SAR multitemporal SAOCOM, variables topográficas y datos agronómicos utilizando técnicas de Machine Learning?

Pregunta complementaria:

> ¿Qué variables presentan mayor capacidad para diferenciar o explicar los ambientes productivos del establecimiento?

## 4. Hipótesis

**H1.** La variabilidad espacial y temporal observada mediante imágenes SAR SAOCOM, combinada con características topográficas y agronómicas, permite identificar patrones persistentes dentro de los potreros compatibles con diferentes ambientes de manejo.

**H2.** La combinación de información satelital, topográfica y agronómica permite caracterizar los ambientes de manejo mejor que el uso aislado de una única fuente de información.

## 5. Objetivo general

Desarrollar una metodología reproducible basada en Machine Learning que permita identificar ambientes de manejo dentro de los potreros de maíz del establecimiento La Rosaura utilizando información satelital SAOCOM y variables agronómicas, como soporte para estrategias futuras de fertilización selectiva.

## 6. Objetivos específicos

1. Construir una base de datos espacial y multitemporal de los potreros de maíz.
2. Procesar variables provenientes de imágenes SAR SAOCOM reales.
3. Incorporar variables topográficas y, cuando estén disponibles, edáficas y de manejo.
4. Realizar un análisis exploratorio de datos (EDA) que caracterice calidad, distribución y variabilidad espacial y temporal.
5. Aplicar técnicas no supervisadas para identificar ambientes de comportamiento homogéneo.
6. Si se dispone de una variable objetivo agronómica confiable, entrenar y comparar modelos supervisados.
7. Optimizar hiperparámetros mediante validación cruzada adecuada al problema espacial.
8. Evaluar los modelos con métricas cuantitativas y criterios agronómicos.
9. Aplicar herramientas de explicabilidad, incluyendo SHAP cuando corresponda.
10. Generar mapas de ambientes que puedan utilizarse como insumo para decisiones agronómicas posteriores.

## 7. Producto SAOCOM real validado

El primer producto disponible para el proyecto es:

- Product ID: `EOL1DSARSAO1A14948810`
- Fecha de adquisición: **07/09/2024**
- Nivel: **L1D**
- Modo: **TOPSAR / TNB**
- Polarización: **QP — HH, HV, VH y VV**
- Formato raster: **GeoTIFF FLOAT32**, entregado sin extensión `.tif`
- CRS: **EPSG:32721 — WGS84 / UTM 21S**
- Dimensiones: **4.396 × 7.104 píxeles** por polarización
- Resolución observada: aproximadamente **43,55 × 42,33 m**
- Metadato radiométrico: `Sigma0Type = AMPLITUDE`

Para valores positivos y válidos se utiliza:

```text
σ⁰_dB = 20 · log10(amplitud)
```

Esta transformación surge del metadato real del producto. No se utilizará la resolución previa supuesta de 10 m para este producto.

## 8. Estrategia de Machine Learning

### Etapa A — Aprendizaje no supervisado

Si no existe todavía una variable objetivo medida en campo, se utilizarán variables SAR, topográficas y agronómicas para identificar estructuras espaciales mediante técnicas como:

- K-Means;
- Gaussian Mixture Models;
- clustering jerárquico;
- PCA como herramienta exploratoria/reducción de dimensionalidad cuando resulte apropiado.

Los clusters obtenidos no serán denominados automáticamente ambientes de alto, medio o bajo potencial. Esa interpretación requerirá evidencia agronómica independiente.

### Etapa B — Aprendizaje supervisado

Si se incorpora una variable objetivo confiable —por ejemplo rendimiento, producción de materia seca u otra respuesta medida en campo— se evaluarán modelos de regresión o clasificación según corresponda. Entre los candidatos se consideran:

- modelo baseline simple;
- modelos lineales cuando correspondan;
- árboles de decisión;
- Random Forest;
- Gradient Boosting / XGBoost.

La selección final dependerá de los datos y no se fijará de antemano.

## 9. Unidad de análisis

La unidad de análisis prevista es una **celda espacial dentro de un potrero**, potencialmente observada en múltiples fechas. Esto permite integrar series temporales SAR con variables relativamente estables como topografía y suelo.

La existencia de muchos píxeles no implica muchas observaciones independientes. La autocorrelación espacial será considerada explícitamente durante la validación.

## 10. Variables candidatas

### SAR SAOCOM

- `sigma0_hh_db`
- `sigma0_hv_db`
- `sigma0_vh_db`
- `sigma0_vv_db`
- diferencias y razones entre polarizaciones cuando estén justificadas;
- estadísticos temporales por píxel o potrero;
- índices polarimétricos compatibles con la representación radiométrica disponible.

No se asumirán relaciones directas del tipo HH = humedad, HV = biomasa o radar = dosis de fertilizante.

### Topografía

Se prevé incorporar:

- elevación;
- pendiente;
- orientación;
- posición topográfica relativa;
- otras variables derivadas de un DEM con justificación agronómica.

### Suelo y manejo

Cuando estén disponibles:

- análisis de suelo;
- fecha de siembra;
- híbrido;
- densidad;
- fertilización aplicada;
- precipitaciones/clima;
- observaciones del cultivo;
- rendimiento o producción final de silo.

### Variable objetivo

La variable objetivo supervisada **todavía no está definida**. No se utilizarán valores simulados para reemplazar mediciones de campo.

## 11. Validación

Debido a la dependencia espacial entre observaciones cercanas, no se utilizará un `train_test_split` aleatorio como única evidencia de generalización.

Se priorizarán esquemas de validación por grupos, potreros o bloques espaciales. Para modelos supervisados se evaluará `GroupKFold` utilizando el identificador del potrero como grupo cuando el diseño de los datos lo permita. También se analizará generalización temporal entre campañas.

## 12. Métricas

- Regresión: MAE, RMSE y R².
- Clasificación: métricas acordes al balance de clases y costo agronómico de los errores.
- Clustering: métricas internas, estabilidad espacial/temporal y validación agronómica.

La selección del modelo no dependerá exclusivamente de una métrica.

## 13. Explicabilidad

Cuando el tipo de modelo lo permita, se utilizará SHAP para estudiar la contribución de las variables a las predicciones. Los valores SHAP describirán el comportamiento del modelo, no causalidad agronómica.

## 14. Reproducibilidad

El proyecto se desarrollará en Python. Se utilizarán semillas aleatorias cuando corresponda, rutas relativas, separación entre datos originales/procesados/outputs y documentación explícita de transformaciones.

Los productos SAOCOM originales y otros archivos geoespaciales pesados no se versionarán directamente en Git.

## 15. Relación con el proyecto SAOCOM

Este repositorio contiene el análisis de Machine Learning. La adquisición y el procesamiento geoespacial primario de SAOCOM se mantienen en el repositorio `proyecto-saocom`.

El flujo previsto es:

```text
proyecto-saocom
   ↓
GeoTIFF recortados + variables SAR documentadas
   ↓
ml_fertilizacion_la_rosaura
   ↓
EDA → features → clustering / modelos supervisados
   ↓
ambientes de manejo validados
```

## 16. Estado actual

**Fase 2 — datos satelitales reales disponibles.**

- [x] Problema, hipótesis y objetivos definidos.
- [x] Primer producto SAOCOM L1D real descargado e inspeccionado.
- [x] Polarizaciones HH/HV/VH/VV confirmadas.
- [x] CRS y resolución real confirmados.
- [x] `Sigma0Type=AMPLITUDE` confirmado.
- [x] Conversión radiométrica a dB definida.
- [ ] Incorporar límites individuales de los 16 potreros.
- [ ] Identificar potreros de maíz por campaña.
- [ ] Procesar serie temporal 2024/25.
- [ ] Incorporar DEM/topografía.
- [ ] Incorporar variables de suelo y manejo.
- [ ] Construir dataset analítico de ML.
- [ ] Ejecutar EDA y clustering.
- [ ] Entrenar modelos supervisados si aparece un target confiable.

---

Las conclusiones agronómicas y los resultados de Machine Learning se incorporarán únicamente cuando existan datos observados suficientes para respaldarlos.
