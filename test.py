import pandas as pd
from anjana.anonymity import k_anonymity, alpha_k_anonymity
import pycanon
import time
import os

data = pd.read_csv("data_anjana/dataset.csv")  # 32561 rows
#data.columns = data.columns.str.strip()

quasi_ident = ['sex', 'age', 'race', 'marital-status', 'education', 'native-country', 'workclass', 'occupation']
ident = ['ID', 'soc_sec_id', 'given_name', 'surname']
sens_att = "salary-class"
k = 5
alpha = 0.8
supp_level = 0

hierarchy_dir = "data_anjana/hierarchies"
hierarchies = {}

for category in quasi_ident:
    file_path = os.path.join(hierarchy_dir, f"{category}.csv")
    if os.path.exists(file_path):
        hierarchies[category] = dict(pd.read_csv(file_path, header=None))
print(hierarchies.keys())
start = time.time()
data_anon = alpha_k_anonymity(
    data, ident, quasi_ident, sens_att, k, alpha, supp_level, hierarchies
)
end = time.time()
print(f"Elapsed time: {end-start}")
print(f"Value of k calculated: {pycanon.anonymity.k_anonymity(data_anon, quasi_ident)}")
alpha_cal, _ = pycanon.anonymity.alpha_k_anonymity(data_anon, quasi_ident, [sens_att])
print(f"Value of alpha calculated: {alpha_cal}")

# Elapsed time: 0.9592475891113281
# Value of k calculated: 10

data_anon.to_csv(f"data_anjana/anonymized/adult_k{k}_A{alpha}_Sup{supp_level}.csv",index=False)

print(f"Number of records suppressed: {len(data) - len(data_anon)}")
print(
    f"Percentage of records suppressed: {100 * (len(data) - len(data_anon)) / len(data)} %"
)

start = time.time()
data_anon2 = k_anonymity(
    data, ident, quasi_ident, k, supp_level, hierarchies
)
end = time.time()
print(f"Elapsed time: {end-start}")
print(f"Value of k calculated: {pycanon.anonymity.k_anonymity(data_anon2, quasi_ident)}")

data_anon2.to_csv(f"data_anjana/anonymized/adult_k{k}_Sup{supp_level}.csv",index=False)

print(f"Number of records suppressed: {len(data) - len(data_anon2)}")
print(
    f"Percentage of records suppressed: {100 * (len(data) - len(data_anon2)) / len(data)} %"
)