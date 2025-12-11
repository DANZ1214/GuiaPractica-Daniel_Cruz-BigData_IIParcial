import pandas as pd

datos = pd.read_csv("ventas.csv")
datos.columns = datos.columns.str.strip().str.lower()

datos["total"] = pd.to_numeric(datos["total"], errors="coerce").fillna(0)

agrupado = datos.groupby(["cliente", "producto"])["total"].sum().reset_index()

print(agrupado.head())
agrupado.to_csv("ventas_agrupado.csv", index=False)