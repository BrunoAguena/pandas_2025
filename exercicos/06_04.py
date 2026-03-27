
#Quem teve mais transacao de streak?

# %%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()
# %%
trasacao_produto = pd.read_csv("../data/transacao_produto.csv", sep=";")
trasacao_produto.head()
# %%
produtos = pd.read_csv("../data/produtos.csv", sep=";")
produtos.head()

# %%

cliente_transacao_produto = transacoes.merge(
    right=trasacao_produto,
    on="IdTransacao",
    how="left",
)[["IdTransacao", "IdCliente", "IdProduto"]]
cliente_transacao_produto.head()
# %%
df_full = cliente_transacao_produto.merge(produtos, on="IdProduto", how="left")

df_full = df_full[df_full["DescNomeProduto"] == "Presença Streak"]
df_full

(df_full.groupby(by=["IdCliente"])["IdTransacao"]
        .count()
        .sort_values(ascending=False)
        .head(1)
)
 
# %%

produtos = produtos[produtos["DescNomeProduto"]=="Presença Streak"]

(
    transacoes.merge(trasacao_produto, on = "IdTransacao", how="left")
                .merge(produtos, on=["IdProduto"], how="right")
                .groupby(by="IdCliente")["IdTransacao"]
                .count()
                .sort_values(ascending=False)
                .head(1)
)