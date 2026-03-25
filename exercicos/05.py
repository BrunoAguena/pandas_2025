#Exercicio para localizar a primeira transacao do dia de cada cliente.

# %%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ';')

transacoes["Data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date
transacoes = transacoes.sort_values("DtCriacao")

#transacoes.drop_duplicates(keep="first", subset=["IdCliente", "Data"])

# %%
first = transacoes.drop_duplicates(keep = "first", subset=["IdCliente", "Data"])

last = transacoes.drop_duplicates(keep = "last", subset=["IdCliente", "Data"])

pd.concat([last, first])