import pandas as pd

datos = pd.read_csv("ventas.csv")

datos.columns = datos.columns.str.strip().str.lower()

datos["descuento"] = datos["total"] * 0.10

datos["total_con_descuento"] = datos["total"] - datos["descuento"]

print(datos[["total", "descuento", "total_con_descuento"]].head())
datos.to_csv("ventas_con_descuento.csv", index=False)