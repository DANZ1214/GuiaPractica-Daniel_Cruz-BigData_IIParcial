import pandas as pd

datos = pd.read_csv("ventas.csv")

datos = datos.rename(columns={"PrecioUnitario": "precio_unitario"})
datos.columns = datos.columns.str.strip().str.lower()

datos["cantidad"] = pd.to_numeric(datos["cantidad"], errors="coerce")
datos["cantidad"] = datos["cantidad"].fillna(datos["cantidad"].mean())

datos["precio_unitario"] = pd.to_numeric(datos["precio_unitario"], errors="coerce")
datos["precio_unitario"] = datos["precio_unitario"].fillna(datos["precio_unitario"].mean())

datos["total"] = pd.to_numeric(datos["total"], errors="coerce")
datos["total"] = datos["total"].fillna(datos["total"].mean())

print("Tipos de datos:")
print(datos[["cantidad", "precio_unitario", "total"]].dtypes)

print("Datos procesados:")
print(datos[["cantidad", "precio_unitario", "total"]].head())
datos.to_csv("ventas_procesado.csv", index=False)