# Protocolo metodológico

## Principio general

El proyecto debe distinguir entre **patrones detectados por el algoritmo**, **asociaciones estadísticas** e **interpretación agronómica**. Ninguna variable SAR se interpretará automáticamente como humedad, biomasa, rendimiento o requerimiento de fertilizante sin calibración o evidencia independiente.

## Fases

### 1. Inventario y control de calidad

- documentar procedencia de cada fuente;
- revisar CRS, resolución espacial, fechas, unidades y valores faltantes;
- verificar cobertura de los potreros;
- registrar transformaciones de manera reproducible.

### 2. EDA

- estadísticos descriptivos;
- distribuciones y outliers;
- faltantes;
- correlaciones con cautela frente a dependencia espacial;
- visualización espacial por potrero;
- análisis temporal de variables SAR.

### 3. Ingeniería de atributos

Las variables derivadas se incorporarán únicamente con justificación física o agronómica. Se podrán evaluar agregados temporales, diferencias entre fechas, medidas de variabilidad, variables topográficas y atributos de manejo.

Toda transformación aprendida a partir de los datos deberá ajustarse exclusivamente con el conjunto de entrenamiento durante la evaluación supervisada.

### 4. Aprendizaje no supervisado

Objetivo: explorar si existen grupos relativamente homogéneos y espacialmente coherentes.

Candidatos iniciales: K-Means, Gaussian Mixture Models y clustering jerárquico. Se analizará sensibilidad al escalado, número de clusters, inicialización y selección de variables.

La calidad no se juzgará sólo con silhouette score. También se estudiarán estabilidad, coherencia espacial, persistencia temporal e interpretación agronómica.

### 5. Aprendizaje supervisado

Sólo se implementará cuando exista una variable objetivo observada y metodológicamente defendible.

Se construirá primero un baseline. Luego se compararán modelos de complejidad creciente. La optimización de hiperparámetros se realizará dentro del esquema de validación para evitar leakage.

### 6. Validación espacial

La autocorrelación espacial impide tratar píxeles vecinos como observaciones completamente independientes. La validación principal utilizará grupos por potrero o bloques espaciales. `GroupKFold` será una alternativa inicial cuando el diseño de los datos lo permita.

Si existen múltiples campañas, se considerará además una evaluación temporal que pruebe generalización hacia períodos no utilizados durante el entrenamiento.

### 7. Explicabilidad

SHAP se utilizará cuando corresponda para describir cómo el modelo utiliza las características. Los valores SHAP no serán interpretados como prueba de causalidad.

### 8. Reproducibilidad

- semillas aleatorias documentadas;
- dependencias declaradas;
- rutas relativas;
- notebook ejecutable de principio a fin;
- separación entre datos originales, procesados y outputs;
- ausencia de credenciales y secretos en el repositorio.
