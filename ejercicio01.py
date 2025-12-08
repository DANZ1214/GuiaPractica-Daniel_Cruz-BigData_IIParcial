import pandas as pd

datos = pd.read_csv("ventas.csv")

print("Registros iniciales:")
print(len(datos))

print("Conteo de valores nulos:")
print(datos.isnull().sum())

datos_sin_nulos = datos.dropna()

datos_finales = datos_sin_nulos.drop_duplicates()

print("Total final de registros:")
print(len(datos_finales))
datos_finales.to_csv("ventas_limpio.csv", index=False)