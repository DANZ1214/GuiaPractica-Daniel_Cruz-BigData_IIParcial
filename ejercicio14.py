import pandas as pd
import time

inicio_normal = time.time()
df_normal = pd.read_csv("ventas.csv")
fin_normal = time.time()
print(f"Tiempo normal: {fin_normal - inicio_normal:.5f} segundos")

inicio_chunk = time.time()
for chunk in pd.read_csv("ventas.csv", chunksize=1000):
    pass
fin_chunk = time.time()
print(f"Tiempo por chunks: {fin_chunk - inicio_chunk:.5f} segundos")
