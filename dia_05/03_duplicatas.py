# %%
import pandas as pd
# %%

df = pd.DataFrame({
    "nome" : ['Teo', 'lara', 'nah', 'bia', 'mah', 'lara', 'mah', 'mah'],
    "sobrenome" : ['calvo', 'calvo', 'ataide', 'ataide', 'silva', 'silva', 'silva', 'silva'],
    "salario" : [2332, 1231, 454, 6543, 6532, 4322, 987, 2134]
})

df

# %%
df = df.sort_values("salario", ascending=False)

df
#%%
df.drop_duplicates(subset=["nome", "sobrenome"])