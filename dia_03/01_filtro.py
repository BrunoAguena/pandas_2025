# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

# %%
pontos = [10,1,1,1,50,100,130,30,25,50]
filtro = []
valores_50_mais = []

for i in pontos:
    filtro.append(i>=50)

resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])

print(resultado)

# %%

#List comprehension

valores_50_mais = [i for i in pontos if i >= 50]

valores_50_mais


# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32, 35, 14],
        "uf": ["sp", "pr", "rj"],
    }
)

filtro = brinquedo["idade"] >= 18

brinquedo[filtro]
# %%

df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

# %%

filtro = df["QtdePontos"] >= 50

df[filtro]

# %%

filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] <100)
df[filtro]

# %%

filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro]

# %%

filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"] <= 50) | (df["DtCriacao"] >= "2025-01-01")
df[filtro]