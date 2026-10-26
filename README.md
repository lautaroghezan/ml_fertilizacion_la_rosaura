# ML multisensor para La Rosaura

Proyecto de Machine Learning para construir una **constelación virtual SAOCOM–Sentinel-2** aplicada a La Rosaura (Tandil), con foco activo en reconstrucción histórica de cultivos y fertilización selectiva del maíz forrajero.

La infraestructura deja planteada además una línea futura independiente para **manejo inteligente de pasturas del tambo**, donde la fusión multisensor se evaluará para estimar utilización, recuperación y prioridad de pastoreo.

## Dos problemas encadenados — proyecto activo

**Modelo 1 — uso histórico:** reconstruir `potrero × campaña → maíz / pastura / otro / incierto + confianza` usando la firma fenológica temporal multisensor. No se asumirá que mayor biomasa implica automáticamente maíz.

**Modelo 2 — fertilización selectiva:** una vez identificados potreros/campañas de maíz, integrar SAR, óptico, topografía, suelo y manejo para detectar ambientes espacialmente persistentes. La dosis no se predice directamente desde el radar.

## Geometría y manejo intrapotrero

Los 16 potreros aportados por el productor están en `data/reference/potreros_la_rosaura.geojson` con IDs estables `L01`–`L16`. Son la unidad espacial primaria para unir campañas y sensores.

Las franjas visibles dentro de algunos potreros pueden corresponder a **subdivisiones temporarias para pastoreo**. Pueden persistir después del cambio de uso del potrero y un sector recientemente pastoreado puede presentar menor biomasa/NDVI que otro sector del mismo potrero. Por lo tanto:

- la textura de una fecha aislada no define maíz/pastura;
- la heterogeneidad intrapotrero no equivale directamente a potencial productivo;
- la clasificación de uso se basará prioritariamente en dinámica temporal;
- mediana, P25, P75 y dispersión ayudarán a representar heterogeneidad sin confundirla con una etiqueta agronómica.

## Fuentes

- **SAOCOM L1D:** HH/HV/VH/VV, producto piloto `EOL1DSARSAO1A14948810` del 07/09/2024, EPSG:32721, resolución aproximada **43,55 × 42,33 m**, `Sigma0Type=AMPLITUDE`, `sigma0_dB=20*log10(amplitud)` para valores positivos.
- **Sentinel-2 L2A:** catálogo automático vía Copernicus STAC; B02/B03/B04/B08 a 10 m, red-edge a 20 m y SCL/CLD para calidad.
- **DEM:** elevación, pendiente y posición topográfica.
- **Agronomía:** suelo, manejo, clima, siembra, fertilización y producción cuando existan.

## Sentinel-2 2024/25: catálogo y acceso real

La consulta reproducible realizada desde `proyecto-saocom` para los 16 potreros encontró:

- 73 productos Sentinel-2 L2A;
- 69 fechas únicas;
- período observado: 05/08/2024–26/06/2025;
- intervalo mediano entre fechas: 5 días;
- intervalo máximo observado: 10 días.

Se verificó el acceso autenticado a Copernicus Data Space S3 y se ejecutó correctamente la visualización piloto del producto:

`S2A_MSIL2A_20240904T134701_N0511_R024_T21HTU_20240904T212846`

para el **04/09/2024**, con nubosidad global informada de **0,0 %**. Se leyeron B02/B03/B04/B08 y se generaron RGB y NDVI recortados a L01–L16.

La nubosidad del catálogo corresponde al producto completo y no sustituye el control local. La siguiente etapa aplicará SCL/CLD y calculará porcentaje válido dentro de cada potrero.

## Dataset esperado

Nivel temporal por potrero:

```text
potrero_id | fecha | campania | sensor | variables SAR/ópticas | calidad
```

Para Sentinel-2:

```text
fecha | potrero_id | valid_pct | NDVI_med | NDVI_p25 | NDVI_p75 | NDVI_iqr | EVI_med | variables_red_edge
```

Nivel de reconstrucción histórica:

```text
potrero_id | campania | cultivo_inferido | prob_maiz | prob_pastura | confianza | evidencia | version_modelo
```

Nivel espacial para ambientes:

```text
potrero_id | pixel_id/x/y | fecha | campania | SAR | óptico | DEM | suelo | manejo
```

## ML

Para uso histórico se compararán reglas fenológicas transparentes y clasificadores sólo cuando haya etiquetas de referencia suficientes. La clase `incierto` es válida y evita forzar decisiones.

Las variables temporales deberán representar la **forma de la curva**, no sólo su nivel: crecimiento, máximo, senescencia, amplitud, pendientes, persistencia y cambios intraestacionales. En pasturas, caídas localizadas pueden estar asociadas al ingreso del rodeo y posterior recuperación.

Para ambientes, K-Means es baseline; GMM/jerárquico y PCA son alternativas exploratorias. Modelos supervisados (Ridge, Random Forest, Gradient Boosting/XGBoost) sólo con target agronómico real.

## Validación

No usar separación aleatoria de píxeles vecinos como única evidencia. Priorizar `GroupKFold` por potrero/bloque y validación temporal entre campañas. SHAP explica comportamiento del modelo, no causalidad agronómica. Clusters no se llaman alto/medio/bajo potencial sin evidencia independiente.

## Flujo activo

```text
proyecto-saocom → L01–L16 + SAOCOM + Sentinel-2
                         ↓
              máscara local de nubes/sombras
                         ↓
       NDVI/EVI/red-edge + P25/P50/P75 por potrero-fecha
                         ↓
                 curvas fenológicas
                         ↓
          reconstrucción histórica + confianza
                         ↓
            selección de maíz por campaña
                         ↓
      ML espacial de ambientes + validación
                         ↓
          fertilización selectiva validada
```

## Línea futura — pastoreo de precisión

Se plantea como proyecto separado reutilizando la constelación virtual:

```text
Sentinel-2 + SAOCOM + clima + registros de pastoreo
                         ↓
estado de pastura + heterogeneidad + recuperación
                         ↓
fecha de entrada/salida + días de descanso + demanda del rodeo
                         ↓
prioridad de pastoreo / rotación
                         ↓
producción de leche + evaluación del resultado
```

La hipótesis multisensor deberá evaluarse explícitamente comparando:

```text
M1 = Sentinel-2
M2 = SAOCOM
M3 = Sentinel-2 + SAOCOM
M4 = Sentinel-2 + SAOCOM + clima + historial de pastoreo
```

El interés científico no es sólo combinar satélites, sino comprobar si la complementariedad **óptico Sentinel-2 + SAR banda L SAOCOM** mejora la caracterización dinámica de pasturas y el apoyo a decisiones respecto de sensores individuales.

## Estado

- [x] AOI confirmado.
- [x] 16 potreros incorporados.
- [x] SAOCOM piloto inspeccionado y radiometría confirmada.
- [x] arquitectura multisensor y dos modelos de maíz definida.
- [x] consulta automática Copernicus STAC implementada.
- [x] catálogo Sentinel-2 L2A 2024/25 obtenido: 73 productos / 69 fechas únicas.
- [x] assets Sentinel-2 B02/B03/B04/B08, red-edge y SCL/CLD identificados.
- [x] acceso S3 Copernicus autenticado y validado.
- [x] escena piloto 04/09/2024 procesada: RGB + NDVI para L01–L16.
- [x] efecto del manejo de pastoreo identificado como posible fuente de heterogeneidad intrapotrero.
- [ ] aplicar máscara local SCL/CLD y calcular `valid_pct`.
- [ ] calcular índices y estadísticas robustas por L01–L16 y fecha.
- [ ] construir 16 curvas fenológicas 2024/25.
- [ ] procesar serie SAOCOM 2024/25 por L01–L16.
- [ ] construir dataset potrero-fecha multisensor.
- [ ] reconstruir uso por campaña con confianza.
- [ ] incorporar DEM, suelo y manejo.
- [ ] entrenar/validar ambientes en maíz.

No se usarán targets simulados para completar resultados académicos.