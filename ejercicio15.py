import pandas as pd

datos = pd.read_csv("ventas.csv")
datos.columns = datos.columns.str.strip().str.lower()

datos["total"] = pd.to_numeric(datos["total"], errors="coerce").fillna(0)

resumen = datos.groupby(["producto", "cliente"])["total"].sum().reset_index()
resumen.to_csv("resumen_general.csv", index=False)

productos = datos["producto"].unique()

for prod in productos:
    nombre_valido = str(prod).replace('"', '').replace('/', '').replace('\\', '').replace(':', '').strip()
    
    filtro_producto = datos[datos["producto"] == prod]
    filtro_producto.to_csv(f"ventas_{nombre_valido}.csv", index=False)
    print(f"Archivo generado para el producto '{prod}': ventas_{nombre_valido}.csv")