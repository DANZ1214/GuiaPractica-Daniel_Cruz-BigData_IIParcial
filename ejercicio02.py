import pandas as pd

datos = pd.read_csv("ventas.csv")
datos.columns = datos.columns.str.strip().str.lower()

print("Nombres de columnas corregidos:")
print(datos.columns)

print("Datos originales:")
print(datos[["cliente", "producto"]].head())

datos["cliente"] = datos["cliente"].str.title()

datos["producto"] = datos["producto"].str.upper()

print("Datos normalizados:")
print(datos[["cliente", "producto"]].head())
datos.to_csv("ventas_normalizado.csv", index=False)
