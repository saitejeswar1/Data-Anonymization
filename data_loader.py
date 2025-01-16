import pandas as pd
import os
from config import DATA_PATH, HIERARCHY_DIR, QUASI_IDENTIFIERS

def load_dataset():
    return pd.read_csv(DATA_PATH)

def load_hierarchies():
    hierarchies = {}
    for category in QUASI_IDENTIFIERS:
        file_path = os.path.join(HIERARCHY_DIR, f"{category}.csv")
        if os.path.exists(file_path):
            hierarchies[category] = dict(pd.read_csv(file_path, header=None))
    return hierarchies