# Notebook principal — orden recomendado

1. Objetivo y guardrails científicos.
2. Carga/validación de `L01`–`L16`.
3. Mapa de los 16 potreros y control contra AOI.
4. Inventario SAOCOM y trazabilidad de productos.
5. QC radiométrico SAOCOM.
6. Resumen HH/HV/VH/VV por potrero-fecha.
7. Inventario Sentinel-2 y QC de nubes/calidad.
8. Series ópticas e índices por potrero-fecha.
9. Visualización comparada SAOCOM–Sentinel-2.
10. Definición de campaña agrícola.
11. Features fenológicas temporales.
12. EDA maíz/pastura cuando existan referencias.
13. Baseline transparente de clasificación histórica.
14. Modelo de cultivo si las etiquetas lo permiten.
15. Matriz `potrero × campaña` con clase y confianza.
16. Revisión explícita de casos `incierto`.
17. Features de rotación histórica.
18. Incorporación de DEM/topografía.
19. Incorporación de suelo/manejo.
20. Selección de potreros/campañas de maíz.
21. Dataset espacial para ambientes.
22. PCA exploratorio si aporta valor.
23. K-Means baseline y comparación opcional.
24. Estabilidad espacial/temporal de clusters.
25. Validación por potrero/bloque/campaña.
26. Modelo supervisado sólo con target observado.
27. SHAP/interpretabilidad cuando corresponda.
28. Mapas finales y limitaciones.

No usar datos simulados para completar resultados. No inferir maíz por un único umbral de biomasa/NDVI ni etiquetar clusters como potencial productivo sin validación.
