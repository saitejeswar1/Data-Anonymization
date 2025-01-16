import os

# Data paths
DATA_PATH = "data_anjana/dataset.csv"
HIERARCHY_DIR = "data_anjana/hierarchies"
OUTPUT_DIR = "data_anjana/anonymized"

# Anonymization parameters
QUASI_IDENTIFIERS = ['sex', 'age', 'race', 'marital-status', 'education', 'native-country', 'workclass', 'occupation']
IDENTIFIERS = ['ID', 'soc_sec_id', 'given_name', 'surname']
SENSITIVE_ATTRIBUTE = "salary-class"
K = 5
ALPHA = 0.8
SUPPRESSION_LEVEL = 0
# Additional anonymization parameters
L = 3  # for l-diversity
C = 0.5  # for recursive (c,l)-diversity
T = 0.2  # for t-closeness
DELTA = 0.1  # for δ-disclosure privacy
BETA = 0.2  # for β-likeness

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)