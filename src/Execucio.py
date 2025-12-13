import pandas as pd
from model import *  # train, preprocess_one_hot, predict_probability

# -----------------------------
# Llegir dades (X + y en un sol fitxer)
# -----------------------------
df = pd.read_csv("data.csv")  # fitxer únic

# Separar X i y
X = df.iloc[:, :-1]   # totes les columnes menys l'última
y = df.iloc[:, -1]    # última columna (recaiguda)

# -----------------------------
# Entrenar el model
# -----------------------------
model_trained, columns, avg_logloss = train(X, y)

# Mostrar resultats
print("Columns used for one-hot encoding:")
print(columns)
print("\nAverage cross-validation log-loss:", avg_logloss)

# -----------------------------
# Preprocessar X i obtenir prediccions de probabilitat
# -----------------------------
X_encoded = preprocess_one_hot(X, columns_trained=columns)
y_prob = predict_probability(model_trained, X_encoded)  # probabilitat de NO recaure

# Afegir les prediccions al DataFrame original
df_with_predictions = df.copy()
df_with_predictions["predicted_prob_not_relapsing"] = y_prob

# Mostrar les primeres 10 prediccions
print("\nPredictions for the first 10 patients:")
print(df_with_predictions.head(10))

# -----------------------------
# Opcional: ordenar per risc de recaiguda
# -----------------------------
df_sorted = df_with_predictions.sort_values(by="predicted_prob_not_relapsing")
print("\nTop 10 patients with highest risk of relapse:")
print(df_sorted.head(10)[["predicted_prob_not_relapsing"]])
