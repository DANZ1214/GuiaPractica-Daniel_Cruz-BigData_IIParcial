import pandas as pd

datos = pd.read_csv("ventas.csv")
datos.columns = datos.columns.str.strip().str.lower()

rango_min = 500
rango_max = 3000
producto_buscado = "Laptop"
clientes_buscados = ["Juan Perez", "Maria Lopez", "Carlos Ruiz"]

filtro = datos[
    (datos["total"] >= rango_min) &
    (datos["total"] <= rango_max) &
    (datos["producto"] == producto_buscado) &
    (datos["cliente"].isin(clientes_buscados))
]

print(filtro)
datos.to_csv("ventas_filtrado.csv", index=False)