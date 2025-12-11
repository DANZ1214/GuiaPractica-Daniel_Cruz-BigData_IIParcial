import pandas as pd

datos = pd.read_csv("ventas.csv")
datos.columns = datos.columns.str.strip().str.lower()

busqueda = input("Ingrese nombre a buscar: ")

resultados = datos[datos["cliente"].str.contains(busqueda, case=False, na=False)]

print(resultados)
