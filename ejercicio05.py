import pandas as pd
import numpy as np

datos = pd.read_csv("ventas.csv")
datos = datos.rename(columns={"PrecioUnitario": "precio_unitario"})
datos.columns = datos.columns.str.strip().str.lower()

datos["impuesto"] = datos["total"] * 0.15
datos["total_final"] = datos["total"] + datos["impuesto"]

condiciones = [
    (datos["total_final"] < 500),
    (datos["total_final"] >= 500) & (datos["total_final"] < 2000),
    (datos["total_final"] >= 2000)
]
etiquetas = ["Bajo", "Medio", "Alto"]

datos["clasificacion_total"] = np.select(condiciones, etiquetas, default="Desconocido")

print(datos[["total", "impuesto", "total_final", "clasificacion_total"]].head())
datos.to_csv("ventas_con_impuesto.csv", index=False)
