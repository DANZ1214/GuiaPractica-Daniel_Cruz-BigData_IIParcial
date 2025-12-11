import pandas as pd

lista_chunks = []

for chunk in pd.read_csv("ventas.csv", chunksize=100):
    lista_chunks.append(chunk)

df_final = pd.concat(lista_chunks, ignore_index=True)

print(df_final)
df_final.to_csv("ventas_completo.csv", index=False)