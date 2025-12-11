import pandas as pd

resultados = pd.Series(dtype=float)

for bloque in pd.read_csv("ventas.csv", chunksize=100):
    bloque.columns = bloque.columns.str.strip().str.lower()
    
    bloque["producto"] = bloque["producto"].str.title()
    bloque["total"] = pd.to_numeric(bloque["total"], errors="coerce").fillna(0)
    
    agrupado = bloque.groupby("producto")["total"].sum()
    
    resultados = resultados.add(agrupado, fill_value=0)

print(resultados)
