import pandas as pd

datos = pd.read_csv("ventas.csv")
datos.columns = datos.columns.str.strip().str.lower()

filtro = datos[datos["total"] > 1000]

ordenado = filtro.sort_values(by="total", ascending=False)

print(ordenado.head())
datos.to_csv("ventas_filtrado_ordenado.csv", index=False)