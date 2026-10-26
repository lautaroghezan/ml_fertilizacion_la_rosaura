"""Preprocesamiento con trazabilidad espacial, temporal y multisensor."""
from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
RANDOM_STATE=42
REQUIRED_TRACE_COLUMNS=["potrero_id","fecha","campania","sensor"]

def validate_traceability(df:pd.DataFrame)->None:
    missing=[c for c in REQUIRED_TRACE_COLUMNS if c not in df.columns]
    if missing:raise ValueError(f"Faltan columnas de trazabilidad: {missing}")
    if df["potrero_id"].isna().any():raise ValueError("potrero_id contiene nulos")
    valid={f"L{i:02d}" for i in range(1,17)};bad=set(df["potrero_id"].dropna().astype(str))-valid
    if bad:raise ValueError(f"potrero_id fuera de L01-L16: {sorted(bad)}")

def replace_infinite(df:pd.DataFrame)->pd.DataFrame:
    return df.replace([np.inf,-np.inf],np.nan)

def build_preprocessor(numeric_cols:list[str],categorical_cols:list[str]|None=None)->ColumnTransformer:
    """Ajustar dentro de cada fold para evitar leakage."""
    num=Pipeline([("imputer",SimpleImputer(strategy="median")),("scaler",StandardScaler())]);trs=[("numeric",num,numeric_cols)]
    if categorical_cols:
        cat=Pipeline([("imputer",SimpleImputer(strategy="most_frequent")),("onehot",OneHotEncoder(handle_unknown="ignore"))]);trs.append(("categorical",cat,categorical_cols))
    return ColumnTransformer(trs,remainder="drop")
