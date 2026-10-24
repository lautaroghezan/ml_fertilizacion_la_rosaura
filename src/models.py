"""Modelos de Machine Learning para La Rosaura.

Incluye sólo constructores reproducibles. La selección final de modelos e
hiperparámetros se realizará después del EDA y según disponibilidad de target.
"""

from __future__ import annotations

from sklearn.cluster import KMeans
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import Ridge

RANDOM_STATE = 42


def make_kmeans(n_clusters: int = 3) -> KMeans:
    """Baseline no supervisado para ambientes de manejo."""
    return KMeans(
        n_clusters=n_clusters,
        random_state=RANDOM_STATE,
        n_init="auto",
    )


def make_regression_baselines() -> dict:
    """Modelos supervisados candidatos si existe target agronómico real."""
    return {
        "ridge": Ridge(alpha=1.0),
        "random_forest": RandomForestRegressor(
            n_estimators=300,
            random_state=RANDOM_STATE,
            n_jobs=-1,
        ),
        "gradient_boosting": GradientBoostingRegressor(
            random_state=RANDOM_STATE,
        ),
    }
