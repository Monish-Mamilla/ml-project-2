
import os

# Get project root (assumes config.py is in src/)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Raw data files
RAW_DATA_PATHS = {
    "campaigns": os.path.join(PROJECT_ROOT, "data/raw/dim_campaigns.csv"),
    "products": os.path.join(PROJECT_ROOT, "data/raw/ordersdim_products.csv"),
    "stores": os.path.join(PROJECT_ROOT, "data/raw/dim_stores.csv"),
    "events": os.path.join(PROJECT_ROOT, "data/raw/fact_events.csv"),
}

DATA_PATH = 'data/raw/data.csv'
MODEL_PATH = 'models/model.pkl'


# Example processed data location
PROCESSED_DATA_DIR = "data/processed/"

# Model and artifacts
MODEL_DIR = "models/"