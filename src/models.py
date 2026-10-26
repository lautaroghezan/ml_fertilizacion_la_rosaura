"""Modelos baseline. Ningún modelo sustituye validación agronómica."""
from sklearn.cluster import KMeans
from sklearn.ensemble import GradientBoostingRegressor,RandomForestClassifier,RandomForestRegressor
from sklearn.linear_model import LogisticRegression,Ridge
RANDOM_STATE=42

def make_kmeans(n_clusters:int=3):return KMeans(n_clusters=n_clusters,n_init=10,random_state=RANDOM_STATE)

def make_crop_classification_baselines():
    """Usar sólo cuando existan etiquetas históricas de referencia suficientes."""
    return {"logistic":LogisticRegression(max_iter=2000,class_weight="balanced",random_state=RANDOM_STATE),"random_forest":RandomForestClassifier(n_estimators=300,class_weight="balanced",n_jobs=-1,random_state=RANDOM_STATE)}

def make_regression_baselines():
    return {"ridge":Ridge(alpha=1.0),"random_forest":RandomForestRegressor(n_estimators=300,n_jobs=-1,random_state=RANDOM_STATE),"gradient_boosting":GradientBoostingRegressor(random_state=RANDOM_STATE)}
