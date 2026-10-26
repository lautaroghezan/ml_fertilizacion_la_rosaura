"""Feature engineering para la constelación virtual La Rosaura."""
from __future__ import annotations
import numpy as np
import pandas as pd

SAR_DB_COLUMNS=["sigma0_hh_db","sigma0_hv_db","sigma0_vh_db","sigma0_vv_db"]

def add_polarization_differences(df:pd.DataFrame)->pd.DataFrame:
    out=df.copy();pairs={"hh_minus_hv_db":("sigma0_hh_db","sigma0_hv_db"),"vv_minus_vh_db":("sigma0_vv_db","sigma0_vh_db"),"hh_minus_vv_db":("sigma0_hh_db","sigma0_vv_db"),"hv_minus_vh_db":("sigma0_hv_db","sigma0_vh_db")}
    for name,(a,b) in pairs.items():
        if a in out and b in out:out[name]=out[a]-out[b]
    return out

def add_temporal_statistics(df:pd.DataFrame,group_cols:list[str],value_cols:list[str]|None=None)->pd.DataFrame:
    out=df.copy();cols=value_cols or [c for c in SAR_DB_COLUMNS if c in out]
    for c in cols:
        g=out.groupby(group_cols)[c]
        out[f"{c}_mean"]=g.transform("mean");out[f"{c}_median"]=g.transform("median");out[f"{c}_std"]=g.transform("std")
    return out

def phenology_summary(df:pd.DataFrame,value_col:str,group_cols:list[str]|None=None,date_col:str="fecha")->pd.DataFrame:
    """Resume forma temporal sin asumir que un nivel alto identifica maíz."""
    groups=group_cols or ["potrero_id","campania"];x=df[groups+[date_col,value_col]].dropna().copy();x[date_col]=pd.to_datetime(x[date_col]);x=x.sort_values(groups+[date_col])
    def one(g):
        v=g[value_col].to_numpy(float);dates=g[date_col].to_numpy();imax=int(np.nanargmax(v));imin=int(np.nanargmin(v))
        return pd.Series({f"{value_col}_n":len(v),f"{value_col}_min":float(np.nanmin(v)),f"{value_col}_max":float(np.nanmax(v)),f"{value_col}_mean":float(np.nanmean(v)),f"{value_col}_amplitude":float(np.nanmax(v)-np.nanmin(v)),f"{value_col}_date_max":dates[imax],f"{value_col}_date_min":dates[imin]})
    return x.groupby(groups,dropna=False).apply(one).reset_index()

def add_rotation_features(history:pd.DataFrame,crop_col:str="cultivo_inferido",confidence_col:str="confianza",min_confidence:float=0.7)->pd.DataFrame:
    """Deriva historia sólo desde clasificaciones suficientemente confiables."""
    h=history.copy().sort_values(["potrero_id","campania"]);trusted=h[confidence_col].fillna(0)>=min_confidence;h["cultivo_confiable"]=h[crop_col].where(trusted,"incierto");h["cultivo_campania_anterior"]=h.groupby("potrero_id")["cultivo_confiable"].shift(1);h["maiz_confiable"]=(h["cultivo_confiable"]=="maiz").astype(int);h["n_maiz_previos"]=h.groupby("potrero_id")["maiz_confiable"].cumsum()-h["maiz_confiable"];return h

def numeric_feature_columns(df:pd.DataFrame,exclude:list[str]|None=None)->list[str]:
    ex=set(exclude or []);return [c for c in df.select_dtypes(include=[np.number]).columns if c not in ex]
