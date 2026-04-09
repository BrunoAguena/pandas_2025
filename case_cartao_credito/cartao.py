# %%
import pandas as pd

df = pd.read_csv("cartao.csv", sep=";")


# %%

df["dtTransacao"] = pd.to_datetime(df["dtTransacao"],format= '%d/%m/%Y')
df["vlParcela"] = df["vlVenda"] / df["qtParcelas"]
#%%
df.head()
# %%
df["ordemParcela"] = df.apply(lambda row: [i for i in range(row["qtParcelas"])], axis=1)
df

# %%

df_explode = df.explode("ordemParcela")
df_explode
# %%
def calcDtParcela(row):
    dt = row ["dtTransacao"] + pd.DateOffset(months=row["ordemParcela"])
    dt = f"{dt.year}-{dt.month}"
    return dt

df_explode["dtParcela"] = df_explode.apply(calcDtParcela, axis=1)
df_explode

# %%

(df_explode.groupby(["idCliente", "dtParcela"])
            ["vlParcela"].sum()
            .reset_index()
            .pivot_table(index="idCliente", columns="dtParcela", values="vlParcela", fill_value=0)
)