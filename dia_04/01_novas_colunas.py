# %%
import pandas as pd
df = pd.read_csv("../data/clientes.csv", sep = ";")

df["qtdePontos"] + 100
# %%


nova_coluna = []
for i in df["qtdePontos"]:
    nova_coluna.append(i+100)

nova_coluna    