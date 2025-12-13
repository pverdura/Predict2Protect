import pandas as pd
import numpy as np

# Seed per reproduïbilitat
np.random.seed(42)

# Definim els gens i alguns allels possibles
genes = ["2DL1", "2DL2", "3DL1", "2DS1", "2DS2"]
allels = ["*001", "*002", "*003", "*004", "*005"]

n_patients = 100

# Generem dades dels pacients
data = []

for _ in range(n_patients):
    patient = {}
    
    for gene in genes:
        # 70% allels, 20% '+', 10% NaN
        r = np.random.rand()
        if r < 0.7:
            n_allels = np.random.choice([1, 2])
            patient[gene] = "/".join(
                np.random.choice(allels, n_allels, replace=False)
            )
        elif r < 0.9:
            patient[gene] = "+"
        else:
            patient[gene] = np.nan
    
    # Variable target: 0 = recau, 1 = no recau
    patient["recaiguda"] = np.random.choice([0, 1])
    
    data.append(patient)

# Crear DataFrame final
df = pd.DataFrame(data)

# Guardar a un únic fitxer
df.to_csv("data.csv", index=False)

# Mostrar primeres files
print("Dataset (first 5 patients):")
print(df.head())
