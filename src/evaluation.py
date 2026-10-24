"""Evaluación de modelos y clusters para La Rosaura."""

from __future__ import annotations

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, silhouette_score
from sklearn.model_selection import GroupKFold


def clustering_metrics(X, labels) -> dict:
    """Calcula métricas internas básicas para clustering.

    Silhouette no reemplaza la evaluación de estabilidad espacial/temporal ni la
    validación agronómica.
    """
    unique = np.unique(labels)
    if len(unique) < 2 or len(unique) >= len(labels):
        silhouette = None
    else:
        silhouette = float(silhouette_score(X, labels))
    return {
        "n_clusters": int(len(unique)),
        "silhouette": silhouette,
    }


def regression_metrics(y_true, y_pred) -> dict:
    """Métricas estándar para un futuro target continuo observado."""
    rmse = mean_squared_error(y_true, y_pred) ** 0.5
    return {
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "rmse": float(rmse),
        "r2": float(r2_score(y_true, y_pred)),
    }


def make_group_kfold(n_splits: int = 5) -> GroupKFold:
    """Validador por grupos, por ejemplo potrero_id."""
    return GroupKFold(n_splits=n_splits)
