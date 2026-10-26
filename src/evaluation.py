"""Evaluación espacial/temporal para los dos modelos del proyecto."""
import numpy as np
from sklearn.metrics import accuracy_score,balanced_accuracy_score,classification_report,mean_absolute_error,mean_squared_error,r2_score,silhouette_score
from sklearn.model_selection import GroupKFold

def clustering_metrics(X,labels):
    u=np.unique(labels);return {"n_clusters":int(len(u)),"silhouette":float(silhouette_score(X,labels)) if 1<len(u)<len(labels) else None}

def crop_classification_metrics(y_true,y_pred):
    return {"accuracy":float(accuracy_score(y_true,y_pred)),"balanced_accuracy":float(balanced_accuracy_score(y_true,y_pred)),"report":classification_report(y_true,y_pred,output_dict=True,zero_division=0)}

def regression_metrics(y_true,y_pred):
    return {"mae":float(mean_absolute_error(y_true,y_pred)),"rmse":float(mean_squared_error(y_true,y_pred)**0.5),"r2":float(r2_score(y_true,y_pred))}

def make_group_kfold(n_splits:int=5):return GroupKFold(n_splits=n_splits)
