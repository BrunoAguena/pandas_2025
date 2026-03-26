# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep = ";")
df.head()

# %%

idCliente = "000dc0f6-e4f2-4a42-b8cd-b586ed1c709a"

def get_last_id(x):
    return x.split("-")[-1]
# %%
get_last_id("000dc0f6-e4f2-4a42-b8cd-b586ed1c709a")

# %%

id_novo = []
for i in df["idCliente"]:
    novo = get_last_id(i)
    id_novo.append(novo)

df["novo_id"]= id_novo
df.head()

# %%

df["novo_id"] = df["idCliente"].apply(get_last_id)
df.head()