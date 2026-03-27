# %%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
clientes = pd.read_csv("../data/clientes.csv", sep=";")

# %%

clientes.head()

# %%

transacoes.head()
# %%

transacoes.merge(right=clientes, 
                 how="left", 
                 left_on=["IdCliente"],
                 right_on=["idCliente"],
                 suffixes=["Transacao", "Cliente"])
