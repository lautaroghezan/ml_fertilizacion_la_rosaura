# Protocolo metodológico

## Principio general

El proyecto distingue entre **patrones detectados por el algoritmo**, **asociaciones estadísticas** e **interpretación agronómica**. Ninguna variable SAR se interpretará automáticamente como humedad, biomasa, rendimiento o requerimiento de fertilizante sin calibración o evidencia independiente.

El primer producto real validado es `EOL1DSARSAO1A14948810` (07/09/2024), nivel L1D, TOPSAR/TNB, QP (HH/HV/VH/VV), GeoTIFF FLOAT32, EPSG:32721, resolución aproximada de 43,55 × 42,33 m y `Sigma0Type=AMPLITUDE`.

Para valores positivos y válidos se utiliza:

```text
σ⁰_dB = 20 · log10(amplitud)
```

## Fases

### 1. Inventario y control de calidad

- documentar procedencia, Product ID y fecha de cada escena;
- revisar CRS, resolución espacial, dimensiones, unidades y NoData;
- verificar cobertura del establecimiento y de cada potrero;
- comprobar polarizaciones disponibles;
- registrar transformaciones de manera reproducible;
- evitar utilizar resoluciones o representaciones radiométricas supuestas cuando el producto real provee esos metadatos.

### 2. Construcción del dataset espacial

La unidad analítica prevista es una celda espacial dentro de un potrero, observada potencialmente en múltiples fechas.

Cada registro deberá conservar identificadores suficientes para evitar pérdida de trazabilidad:

- `potrero_id`;
- fecha de adquisición;
- Product ID;
- coordenadas o identificador espacial;
- campaña;
- fuente y versión del procesamiento.

Las variables SAR candidatas incluyen `sigma0_hh_db`, `sigma0_hv_db`, `sigma0_vh_db` y `sigma0_vv_db`.

### 3. EDA

- estadísticos descriptivos;
- distribuciones y outliers;
- faltantes;
- análisis de rangos y valores físicamente plausibles;
- correlaciones con cautela frente a dependencia espacial;
- visualización espacial por potrero;
- análisis temporal de variables SAR;
- comparación de variabilidad dentro y entre potreros.

### 4. Ingeniería de atributos

Las variables derivadas se incorporarán únicamente con justificación física o agronómica. Se podrán evaluar:

- diferencias entre polarizaciones;
- razones entre polarizaciones cuando sean matemáticamente válidas;
- agregados temporales;
- diferencias entre fechas;
- media, mediana, dispersión y persistencia temporal;
- variables topográficas derivadas de DEM;
- atributos de suelo y manejo.

Toda transformación aprendida a partir de los datos deberá ajustarse exclusivamente con el conjunto de entrenamiento durante la evaluación supervisada.

### 5. Aprendizaje no supervisado

Objetivo: explorar si existen grupos relativamente homogéneos y espacialmente coherentes.

Candidatos iniciales:

- K-Means;
- Gaussian Mixture Models;
- clustering jerárquico;
- PCA como herramienta exploratoria cuando corresponda.

La calidad no se juzgará sólo con silhouette score. También se estudiarán estabilidad, coherencia espacial, persistencia temporal e interpretación agronómica.

Los clusters no serán denominados automáticamente alto, medio o bajo potencial sin evidencia externa.

### 6. Aprendizaje supervisado

Sólo se implementará cuando exista una variable objetivo observada y metodológicamente defendible.

Se construirá primero un baseline. Luego se compararán modelos de complejidad creciente, por ejemplo modelos lineales, árboles, Random Forest y Gradient Boosting/XGBoost.

La optimización de hiperparámetros se realizará dentro del esquema de validación para evitar leakage.

### 7. Validación espacial y temporal

La autocorrelación espacial impide tratar píxeles vecinos como observaciones completamente independientes.

La validación principal utilizará grupos por potrero o bloques espaciales. `GroupKFold` será una alternativa inicial cuando el diseño de los datos lo permita.

Si existen múltiples campañas, se considerará una evaluación temporal que pruebe generalización hacia períodos no utilizados durante el entrenamiento.

No se aceptará un `train_test_split` aleatorio de píxeles vecinos como única evidencia de generalización.

### 8. Explicabilidad

SHAP se utilizará cuando corresponda para describir cómo el modelo utiliza las características. Los valores SHAP no serán interpretados como prueba de causalidad.

### 9. Reproducibilidad

- semillas aleatorias documentadas;
- dependencias declaradas;
- rutas relativas;
- notebooks ejecutables de principio a fin;
- separación entre datos originales, procesados y outputs;
- ausencia de credenciales y secretos;
- no versionar productos SAOCOM completos ni GeoTIFF pesados;
- documentar Product ID y parámetros de preprocesamiento para poder regenerar los datasets analíticos.
