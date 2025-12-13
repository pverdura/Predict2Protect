import pandas as pd
import numpy as np

# Semilla per reproducció
np.random.seed(42)

# Definim els gens i alguns allels possibles
genes = ["2DL1", "2DL2", "3DL1", "2DS1", "2DS2"]
allels = ["*001", "*002", "*003", "*004", "*005"]

# Generem X (30 pacients x 5 gens)
X_data = []
for _ in range(100):
    patient = []
    for gene in genes:
        # 70% probabilitat d'allels específics, 20% '+', 10% NaN
        r = np.random.rand()
        if r < 0.7:
            # 1 o 2 allels separats per '/'
            n_allels = np.random.choice([1, 2])
            patient.append("/".join(np.random.choice(allels, n_allels, replace=False)))
        elif r < 0.9:
            patient.append("+")
        else:
            patient.append(np.nan)
    X_data.append(patient)

X = pd.DataFrame(X_data, columns=genes)

# Generem y aleatoriament amb 0 o 1
y = pd.Series(np.random.choice([0, 1], size=100))
X.to_csv("X.csv", index=False)
y.to_csv("y.csv", index=False)
# Mostrem les primeres files
print("X (first 5 patients):")
print(X.head())
print("\ny:")
print(y.head())
