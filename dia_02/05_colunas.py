# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv",sep=";")
df.shape

# %%
df.dtypes

# %%

renamed_columns = {
    "QtdePontos":"qtPontos",
    "DescSistemaOrigem":"SistemaOrigem"
}

#df = df.rename(columns=renamed_columns)
df.rename(columns=renamed_columns, inplace=True)

# %%

df

# %%

colunas = ["IdCliente","qtPontos"]
df[colunas]

# %%
# SELECT * from DF
df
# %%
# SELECT IdCliente FROM df

df[["IdCliente"]]

# %%
# SELECT IdCliente, qtPontos FROM df LIMIT 5
colunas = ["IdCliente", "qtPontos"]
df[colunas].tail(5)

# %%
# SELECT IdCliente, IdTransacao, qtpontos
#FROM df
#Limit 5

df[["IdCliente", "IdTransacao", "qtPontos"]].head(5)


# %%
colunas = list(df.columns)
colunas.sort()

df = df[colunas]
df