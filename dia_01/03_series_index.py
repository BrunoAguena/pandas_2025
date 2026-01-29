# %%

import pandas as pd

idades = [
    32,38,30,30,31,
    35,25,29,31,37,
    27,23,36,33,39
]

series_idades = pd.Series(idades)
series_idades


# %% 
idades[0]
series_idades[0]

# %%
# diferente de acessar lista -1, não consegue acessar o ultimo termo em uma serie
# Nas séries os indices são como as chaves dos dicionários

series_idades[-1]

# %%

series_idades = series_idades.sort_values()
series_idades

# %%

series_idades[0]

# %%
# para pegar o ultimo termo, utilizando o iloc você busca na posição

series_idades.iloc[-1]

# %%
# 3 primeiros termos
series_idades.iloc[:3]

# inverte a lista
series_idades.iloc[::-1]

# %%

idades = [
    32,38,30,30,31,
    35,25,29,31,37,
    27,23,36,33,39
]

indexs = [
    "Teo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Kozato"
]

series_idades = pd.Series(idades, index = indexs)
series_idades

# %%
#iloc é navegar nas linhas
#loc é navegar nos indices

series_idades.loc["Teo"]

# %%