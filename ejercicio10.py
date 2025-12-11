import pandas as pd

gran_total = 0

for bloque in pd.read_csv("ventas.csv", chunksize=100):
    bloque.columns = bloque.columns.str.strip().str.lower()
    
    bloque["total"] = pd.to_numeric(bloque["total"], errors="coerce").fillna(0)
    
    subtotal = bloque["total"].sum()
    print(f"Subtotal del bloque: {subtotal}")
    
    gran_total += subtotal

print(f"Total global acumulado: {gran_total}")
