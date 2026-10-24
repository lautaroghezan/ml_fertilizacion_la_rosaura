"""Funciones de preprocesamiento para el proyecto ML de La Rosaura."""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

RANDOM_STATE = 42

REQUIRED_TRACE_COLUMNS = ["potrero_id", "fecha", "product_id"]


def validate_traceability(df: pd.DataFrame) -> None:
    """Verifica que el dataset conserve trazabilidad mínima."""
    missing = [c for c in REQUIRED_TRACE_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas de trazabilidad: {missing}")


def replace_infinite(df: pd.DataFrame) -> pd.DataFrame:
    """Reemplaza infinitos por NaN para que puedan imputarse explícitamente."""
    return df.replace([np.inf, -np.inf], np.nan)


def build_preprocessor(
    numeric_cols: list[str],
    categorical_cols: list[str] | None = None,
) -> ColumnTransformer:
    """Construye un preprocesador sin ajustar sobre el dataset completo.

    Debe entrenarse dentro de un Pipeline y dentro del esquema de validación.
    """
    categorical_cols = categorical_cols or []

    numeric_pipe = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    categorical_pipe = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    return ColumnTransformer(
        transformers=[
            ("num", numeric_pipe, numeric_cols),
            ("cat", categorical_pipe, categorical_cols),
        ],
        remainder="drop",
    )
