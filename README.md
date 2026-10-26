# ML multisensor para La Rosaura

Proyecto de Machine Learning para construir una **constelación virtual SAOCOM–Sentinel-2** aplicada a La Rosaura (Tandil).

## Dos problemas encadenados

**Modelo 1 — uso histórico:** reconstruir `potrero × campaña → maíz / pastura / otro / incierto + confianza` usando la firma fenológica temporal multisensor. No se asumirá que mayor biomasa implica automáticamente maíz.

**Modelo 2 — fertilización selectiva:** una vez identificados potreros/campañas de maíz, integrar SAR, óptico, topografía, suelo y manejo para detectar ambientes espacialmente persistentes. La dosis no se predice directamente desde el radar.

## Geometría

Los 16 potreros aportados por el productor están en `data/reference/potreros_la_rosaura.geojson` con IDs estables `L01`–`L16`. Son la unidad espacial primaria para unir campañas y sensores. El perímetro exterior aproximado sigue usándose como control de ubicación.

## Fuentes

- **SAOCOM L1D:** HH/HV/VH/VV, producto piloto `EOL1DSARSAO1A14948810` del 07/09/2024, EPSG:32721, ~43,55 × 42,33 m, `Sigma0Type=AMPLITUDE`, `sigma0_dB=20*log10(amplitud)` para valores positivos.
- **Sentinel-2 L2A:** catálogo automático vía Copernicus STAC, reflectancias e índices ópticos/fenológicos con control de nubes/calidad.
- **DEM:** elevación, pendiente y posición topográfica.
- **Agronomía:** suelo, manejo, clima, siembra, fertilización y producción cuando existan.

## Sentinel-2 2024/25: catálogo real

La consulta reproducible realizada desde `proyecto-saocom` para los 16 potreros encontró:

- 73 productos Sentinel-2 L2A;
- 69 fechas únicas;
- período observado: 05/08/2024–26/06/2025;
- intervalo mediano entre fechas: 5 días;
- intervalo máximo observado: 10 días.

La nubosidad informada por el catálogo corresponde al producto completo y no se usará como sustituto de la calidad local sobre La Rosaura. El siguiente paso es inspeccionar los assets STAC, aplicar máscara de nubes/sombras y calcular porcentaje válido e índices por `potrero × fecha`.

## Dataset esperado

Nivel temporal por potrero:

```text
potrero_id | fecha | campania | sensor | variables SAR/ópticas | calidad
```

Para Sentinel-2, la primera tabla analítica deberá incluir al menos:

```text
fecha | potrero_id | valid_pct | NDVI_med | NDVI_p25 | NDVI_p75 | EVI_med | variables_red_edge
```

Nivel de reconstrucción histórica:

```text
potrero_id | campania | cultivo_inferido | confianza | evidencia | version_modelo
```

Nivel espacial para ambientes:

```text
potrero_id | pixel_id/x/y | fecha | campania | SAR | óptico | DEM | suelo | manejo
```

## ML

Para uso histórico se compararán reglas fenológicas transparentes y clasificadores sólo cuando haya etiquetas de referencia suficientes. La clase `incierto` es válida y evita forzar decisiones. Para ambientes, K-Means es baseline; GMM/jerárquico y PCA son alternativas exploratorias. Modelos supervisados (Ridge, Random Forest, Gradient Boosting/XGBoost) sólo con target agronómico real.

## Validación

No usar separación aleatoria de píxeles vecinos como única evidencia. Priorizar `GroupKFold` por potrero/bloque y validación temporal entre campañas. SHAP explica comportamiento del modelo, no causalidad agronómica. Clusters no se llaman alto/medio/bajo potencial sin evidencia independiente.

## Flujo

```text
proyecto-saocom → recortes L01–L16 + resumen SAR por potrero
Sentinel-2 STAC → 73 productos / 69 fechas en 2024/25
                         ↓
              máscara local de nubes/sombras
                         ↓
                índices por potrero-fecha
                         ↓
                reconstrucción histórica
                         ↓
            selección de maíz por campaña
                         ↓
      ML espacial de ambientes + validación
```

## Estado

- [x] AOI confirmado.
- [x] 16 potreros incorporados.
- [x] SAOCOM piloto inspeccionado y radiometría confirmada.
- [x] arquitectura multisensor y dos modelos definida.
- [x] consulta automática Copernicus STAC implementada.
- [x] catálogo Sentinel-2 L2A 2024/25 obtenido: 73 productos / 69 fechas únicas.
- [ ] inspeccionar assets Sentinel-2 y capa de calidad/nubes.
- [ ] calcular porcentaje válido e índices por L01–L16 y fecha.
- [ ] procesar serie SAOCOM 2024/25 por L01–L16.
- [ ] construir dataset potrero-fecha multisensor.
- [ ] reconstruir uso por campaña con confianza.
- [ ] incorporar DEM, suelo y manejo.
- [ ] entrenar/validar ambientes en maíz.

No se usarán targets simulados para completar resultados académicos.
