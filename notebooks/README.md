# Notebook final

El notebook principal se incorporará progresivamente y deberá poder ejecutarse de principio a fin con datos observados.

## Estructura actualizada

1. Resumen ejecutivo
2. Contexto productivo de La Rosaura
3. Formulación del problema
4. Pregunta de investigación e hipótesis
5. Producto SAOCOM real y trazabilidad
6. Carga de datos procesados
7. Control de calidad espacial/radiométrico
8. EDA
9. Ingeniería de atributos SAR
10. Integración de topografía y manejo
11. Estrategia de validación espacial
12. Aprendizaje no supervisado
13. Evaluación de estabilidad de clusters
14. Definición del target supervisado, si existe
15. Baseline
16. Entrenamiento de modelos
17. Optimización de hiperparámetros
18. Comparación y selección
19. Explicabilidad con SHAP
20. Mapas de ambientes y análisis agronómico
21. Limitaciones
22. Conclusiones
23. Reproducibilidad

## Producto real ya disponible

El primer producto de referencia es `EOL1DSARSAO1A14948810` (07/09/2024), con HH/HV/VH/VV, EPSG:32721, resolución aproximada de 43,55 × 42,33 m y `Sigma0Type=AMPLITUDE`.

Para valores positivos se utilizará `σ⁰_dB = 20·log10(amplitud)` en los datos derivados por el pipeline geoespacial.

## Regla metodológica

No se generarán datos simulados para completar resultados. Las secciones de ML se habilitarán a medida que existan datasets observados y documentados. Los píxeles vecinos no se tratarán como observaciones independientes durante la validación.
