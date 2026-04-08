# %%
import pandas as pd

df = pd.read_csv("cartao.csv", sep=";")


# %%

df["dtTransacao"] = pd.to_datetime(df["dtTransacao"],format= '%d/%m/%Y')
df["vlParcela"] = df["vlVenda"] / df["qtParcelas"]
#%%
df.head()
# %%

df["vlParcelaUnica"] = df.apply(lambda row:[row["vlParcela"]] * row["qtParcelas"], axis=1)
df.explode("vlParcelaUnica")

# %%

def calcDtParcela(row):
    dt = row ["dtTransacao"] + pd.DateOffset(months=row["ordemParcela"])
    dt = f"{dt.year}-{dt.month}"
    return dt

df["ordemParcela"] = df.apply(calcDtParcela, axis=1)
df_explode = df.explode("ordemParcela")

# %%

df_explode["dtParcela"] = df_explode.apply(lambda row: row["dtTransacao"] + pd.DateOffset(months=row["ordemParcela"]), axis=1)
df_explode.head()