# ML para fertilización selectiva — La Rosaura

Proyecto final de Machine Learning aplicado a la identificación de ambientes de manejo para fertilización selectiva de maíz en el establecimiento **La Rosaura**, partido de Tandil, provincia de Buenos Aires, Argentina.

## 1. Contexto productivo

La Rosaura es un establecimiento agropecuario cuya actividad productiva incluye la producción lechera. Parte de la superficie agrícola se destina a maíz para silo, utilizado como componente de la alimentación del rodeo.

La producción agrícola presenta variabilidad espacial dentro de los potreros. Diferencias de relieve, suelo, disponibilidad hídrica, desarrollo del cultivo y manejo pueden generar sectores con distinto comportamiento agronómico y potencial productivo. Sin embargo, una aplicación uniforme de fertilizante no representa necesariamente esa heterogeneidad.

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
2. Procesar variables provenientes de imágenes SAR SAOCOM.
3. Incorporar variables topográficas y, cuando estén disponibles, edáficas y de manejo.
4. Realizar un análisis exploratorio de datos (EDA) que caracterice calidad, distribución y variabilidad espacial y temporal.
5. Aplicar técnicas no supervisadas para identificar ambientes de comportamiento homogéneo.
6. Si se dispone de una variable objetivo agronómica confiable, entrenar y comparar modelos supervisados.
7. Optimizar hiperparámetros mediante validación cruzada adecuada al problema espacial.
8. Evaluar los modelos con métricas cuantitativas y criterios agronómicos.
9. Aplicar herramientas de explicabilidad, incluyendo SHAP cuando corresponda.
10. Generar mapas de ambientes que puedan utilizarse como insumo para decisiones agronómicas posteriores.

## 7. Estrategia de Machine Learning

El proyecto contempla dos etapas, condicionadas por la disponibilidad de datos reales.

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

## 8. Unidad de análisis

La unidad de análisis prevista es una **celda espacial dentro de un potrero**, potencialmente observada en múltiples fechas. Esto permite integrar series temporales SAR con variables relativamente estables como topografía y suelo.

La existencia de miles de píxeles no implica miles de observaciones independientes. La autocorrelación espacial será considerada explícitamente durante la validación.

## 9. Fuentes de variables previstas

### SAR SAOCOM

El producto piloto solicitado es de polarización cuádruple (QP), con HH, HV, VH y VV. Las transformaciones radiométricas y variables derivadas se definirán únicamente después de inspeccionar los metadatos reales del producto.

No se asumirán relaciones directas del tipo HH = humedad, HV = biomasa o radar = dosis de fertilizante.

### Topografía

Se prevé incorporar, según disponibilidad y resolución del modelo digital de elevación:

- elevación;
- pendiente;
- orientación;
- posición topográfica relativa;
- otras variables derivadas que tengan justificación agronómica.

### Suelo y manejo

Cuando estén disponibles se podrán incorporar análisis de suelo, fechas de siembra, híbrido, densidad, fertilización y otras variables de manejo.

### Variable objetivo

La variable objetivo supervisada **todavía no está definida**. No se utilizarán valores simulados para reemplazar mediciones de campo. Su definición dependerá de la disponibilidad y calidad de datos productivos reales.

## 10. Validación

Debido a la dependencia espacial entre observaciones cercanas, no se utilizará un `train_test_split` aleatorio como única evidencia de generalización.

Se priorizarán esquemas de validación por grupos, potreros o bloques espaciales. Para modelos supervisados se evaluará, entre otras alternativas, `GroupKFold` utilizando el identificador del potrero como grupo. Si la información disponible lo permite, también se analizará generalización temporal entre campañas.

## 11. Métricas

Las métricas se definirán según la tarea final. Para regresión se consideran MAE, RMSE y R². Para clasificación se seleccionarán métricas acordes al balance de clases y al costo agronómico de los errores. Para clustering se utilizarán métricas internas junto con estabilidad espacial/temporal e interpretación agronómica.

La selección del modelo no dependerá exclusivamente de una métrica: también se considerarán generalización, interpretabilidad y utilidad para la decisión productiva.

## 12. Explicabilidad

Cuando el tipo de modelo lo permita, se utilizará SHAP para estudiar la contribución de las variables a las predicciones. La interpretación se realizará como explicación del comportamiento del modelo y no automáticamente como evidencia de causalidad agronómica.

## 13. Reproducibilidad

El proyecto se desarrollará en Python. El notebook final documentará el pipeline completo desde la carga de datos hasta la evaluación y las conclusiones. Se fijarán semillas aleatorias cuando corresponda y se documentarán dependencias, transformaciones y decisiones metodológicas.

## 14. Relación con el proyecto SAOCOM

Este repositorio contiene el análisis de Machine Learning. La adquisición y el procesamiento geoespacial primario de productos SAOCOM se mantienen separados del proyecto académico. Los datos que ingresen a este repositorio deberán estar documentados y ser reproducibles a partir de sus fuentes originales.

## 15. Estado actual

**Fase 1 — Diseño metodológico.**

Ya se definieron el problema productivo, la pregunta de investigación, las hipótesis, los objetivos y la estrategia general de validación. Permanecen pendientes la incorporación de límites individuales de los potreros, topografía, imágenes SAOCOM reales y datos agronómicos de campo.

---

Este repositorio se encuentra en desarrollo. Las conclusiones agronómicas y los resultados de Machine Learning se incorporarán únicamente cuando existan datos observados suficientes para respaldarlos.
