#!/usr/bin/env python
# coding: utf-8

# In[14]:


# feito utilizando o jupyter :)

import pandas as pd

# Passo 1: Importar a base de dados

tabela = pd.read_csv("telecom_users.csv")

# Passo 2: Visualizar a base de dados
# Entender as Informarções que você tem disponível
# Descobrir as cagadas da base

# axis = 0 = linha, axis = 1 = coluna

tabela = tabela.drop("Unnamed: 0", axis=1)

# Passo 3: Tratamento de Dados

# resolver valores que estão reconhecidos de forma errada(tipo)

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce") 

# resolver valores vazios
# colunas em que todos os valores são vazios

tabela = tabela.dropna(how="all", axis=1) # dropna = exclui valores vazios

# linhas que possuem pelo menos 1 valor vazio

tabela = tabela.dropna(how="any" , axis=0) 

# Passo 4: Analise Inicial

print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.2%}".format)) 

# Passo 5: Análise detalhada - descobrir causas dos cancelamentos
# comparar cada coluna da base de dados com a coluna churn

import plotly.express as px

# etapa 1: criar o gráfico
for coluna in tabela.columns:
    # para edições nos gráficos: https://plotly.com/python/histograms/
    # para mudar a cor do gráfico , color_discrete_sequence=["blue", "green"]
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    # etapa 2: exibir o gráfico
    grafico.show()
    
# análise final
# CONCLUSÕES E AÇÕES

# 1. A proporção de clientes que tem familia/casados tendem a cancelar menos.
# - Promoções diferenciadas para mais pessoas da mesma família.
# 2. Clientes nos primeiros meses tem uma tendência muito maior a caancelar.
# - Marketing muito agressivo.
# - Experiência tenha sido ruim.
# - Promoção de desconto no primeiro ano.
# 3. Cancelamentos exorbitantes no serviço de fibra, analisar problema no serviço.
# 4. Pessoas com mais pacotes de serviço tendem a cancelar menos.
# - Oferecer mais serviços gratuito ou com desconto.
# 5. Quase todos cancelamentos estão no contrato mensal.
# - Oferecer desconto no anual.
# 6. Grande maioria dos cancelamento estão no boleto eletrônico.


# In[16]:


get_ipython().system('pip install plotly')

