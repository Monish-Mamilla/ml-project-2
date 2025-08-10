import pandas as pd
from src.config import DATA_PATH
from src.config import RAW_DATA_PATHS

def load_data():
    return pd.read_csv(DATA_PATH).dropna(), pd.read_csv(DATA_PATH)['target']

def load_campaigns():
    return pd.read_csv(RAW_DATA_PATHS["campaigns"])

def load_products():
    return pd.read_csv(RAW_DATA_PATHS["products"])

def load_stores():
    return pd.read_csv(RAW_DATA_PATHS["stores"])

def load_events():
    return pd.read_csv(RAW_DATA_PATHS["events"])

