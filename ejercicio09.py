import pandas as pd

archivo = "ventas.csv"
tamanio_bloque = 100
total_registros = 0

for bloque in pd.read_csv(archivo, chunksize=tamanio_bloque):
    print(f"Procesando bloque de {len(bloque)} registros")
    total_registros += len(bloque)

print(f"Total procesado: {total_registros}")