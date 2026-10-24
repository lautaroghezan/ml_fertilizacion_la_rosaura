"""Ingeniería de atributos para La Rosaura.

Las funciones de este módulo operan sobre variables ya procesadas por el
pipeline geoespacial. No convierten retrodispersión en variables agronómicas.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

SAR_DB_COLUMNS = ["sigma0_hh_db", "sigma0_hv_db", "sigma0_vh_db", "sigma0_vv_db"]


def add_polarization_differences(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega diferencias simples entre polarizaciones en dB."""
    out = df.copy()
    pairs = [
        ("sigma0_hh_db", "sigma0_hv_db", "hh_minus_hv_db"),
        ("sigma0_vv_db", "sigma0_vh_db", "vv_minus_vh_db"),
        ("sigma0_hh_db", "sigma0_vv_db", "hh_minus_vv_db"),
        ("sigma0_hv_db", "sigma0_vh_db", "hv_minus_vh_db"),
    ]
    for a, b, name in pairs:
        if a in out.columns and b in out.columns:
            out[name] = out[a] - out[b]
    return out


def add_temporal_statistics(
    df: pd.DataFrame,
    group_cols: list[str],
    value_cols: list[str] | None = None,
) -> pd.DataFrame:
    """Calcula media, mediana y desvío temporal por unidad espacial.

    `group_cols` debe identificar de forma estable la unidad espacial, por ejemplo
    ["potrero_id", "pixel_id"].
    """
    value_cols = value_cols or [c for c in SAR_DB_COLUMNS if c in df.columns]
    if not value_cols:
        return df[group_cols].drop_duplicates().copy()

    agg = df.groupby(group_cols, dropna=False)[value_cols].agg(["mean", "median", "std"])
    agg.columns = [f"{col}_{stat}" for col, stat in agg.columns]
    return agg.reset_index()


def numeric_feature_columns(df: pd.DataFrame, exclude: set[str] | None = None) -> list[str]:
    """Devuelve columnas numéricas utilizables como candidatas de ML."""
    exclude = exclude or set()
    return [
        c for c in df.select_dtypes(include=[np.number]).columns
        if c not in exclude
    ]
