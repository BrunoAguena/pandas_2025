# %%
import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

response = requests.get(url, headers=headers)
dfs = pd.read_html(response.text)
uf = dfs[1]

# %%
numero = "251 259,2"
def str_to_float(x:str):
    x = float(x.replace(" ", "")
              .replace(",",".")
              .replace("\xa0", "")
              )
    return x

# %%
uf
# %%
uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)
# %%

uf.dtypes

# %%
x = "73,9 anoa"


def exp_to_anos(exp):
    return float(exp.replace(",", ".").replace(" ", "").replace("anos", ""))

uf["xpectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(exp_to_anos)

uf.head()

# %%
# CASE WHEN DO SQL, criando uma coluna regiao que devolve a região do estado.

def uf_to_regiao(uf):
    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte"]:
        return "Nordeste"
    elif uf in ["Amapá", "Acre", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
        return "Norte"
    elif uf in ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste" 
    elif uf in ["Santa Catarina", "Paraná", "Rio Grande do Sul"]:
        return "Sul"   

uf["Região"] = uf["Unidade federativa"].apply(uf_to_regiao) 

uf

# %%

def mortalide_to_float(x:str):
    x = float(x.replace("‰", "").replace(",", "."))
    return x

uf["Mortalidade infantil (/1000)"] = uf["Mortalidade infantil (2016)"].apply(mortalide_to_float)

# %%
uf.head()
# %%

def classifica_bom(linha):
    return(linha["PIB per capita (R$) (2015)"]>30000 and 
            linha["Mortalidade infantil (/1000)"] < 15 and
            linha["IDH (2010)"] > 700)

# %%

uf["Classifica Bom"] = uf.apply(classifica_bom, axis = 1)

# %%

uf.apply(lambda x: print(x), axis=1)

