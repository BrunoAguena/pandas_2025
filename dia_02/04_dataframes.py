# %%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes

# %%
# Mostra as 5 primeiras linhas
df_clientes.head()

# %%
# Mostra as 10 primeiras linhas
df_clientes.head(n=10)

# %%
#mostra as 5 ultimas linhas do dataset
df_clientes.tail()

# %%
df_clientes.tail(n=10)

# %%
# Mostra linhas aleatórias para amostras
df_clientes.sample(10)

# %%
#mostra o numero da ultima liinha e a quantidade de colunas
df_clientes.shape

# %%
df_clientes.columns

#%%
df_clientes.index

#%%
df_clientes.info(memory_usage="deep", max_cols=2)

# %%
df_clientes.dtypes["idCliente"]

