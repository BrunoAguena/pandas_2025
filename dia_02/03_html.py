# %%

import pandas as pd

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
dfs = pd.read_html(
    url,
    storage_options={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }               
)
dfs


# %%

df_uf = dfs[1]
df_uf.to_csv("ufs.csv", sep=";", index=False)