import pandas as pd

# Define los nombres de las columnas, ya que el archivo bezdekIris.data no los incluye
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

# Lee el archivo y crea el DataFrame
df = pd.read_csv("bezdekIris.data", names=column_names)

# Muestra los primeros registros para verificar
print(df.head())
