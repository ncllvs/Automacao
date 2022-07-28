#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 1 - Importar a base de dados

import pandas as pd

tabela = pd.read_csv("telecom_users.csv")

# 2 - Visualizar a base de dados

tabela = tabela.drop("Unnamed: 0", axis=1) # comando drop exclui a coluna(axis=1) 1(Unnamed: 0)
display(tabela)


# In[6]:


# 3 - Tratamento de dados

# transforma o typo object para número float, força os erros a serem vazios (NaN)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# informações vazias
# colunas completamente vazias -> excluir
tabela = tabela.dropna(how="all", axis=1)
# linhas completamente vazias
tabela = tabela.dropna(how="any", axis=0)
print(tabela.info())


# In[7]:


# 4 - Análise Inicial dos dados

# como estão os cancelamentos? 26%
print(tabela["Churn"].value_counts()) # conta os valores totais de cancelamento
print(tabela["Churn"].value_counts(normalize=True).map("{:1%}".format)) # conta o percentual de cancelamento


# In[11]:


# 5 - Descobrir os motivos do cancelamento

import plotly.express as px

# https://plotly.com/python/histograms/

# para cada coluna na tabela // for variavel in lista
for coluna in tabela.columns:
    # criar o gráfico
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    # exibir o gráfico
    grafico.show()


# In[2]:


#!pip install plotly


# In[ ]:


# Conclusões:
    """
    1 - Clientes recentes estão cancelando mais do que os já fidelizados por mais tempo (+ 1 ano)
        - Pode tá fazendo alguma promoção em que está dando o 1º mês de graça
        - O início do serviço pro cliente está sendo muito confuso
        - A 1º experiência do cliente está ruim
        - Podemos criar incentivos nos primeiros meses
            - 1º ano mais barato, etc
    2 - Boleto eletrônico tem mais cancelamento do que as outras formas de pagamento
        - Oferecer desconto nas outras formas de pagamento
    3 - Clientes com contrato mensal tem mais chance de cancelar
        - Oferecer desconto para pagar anuidade
    4 - Quanto mais serviços o cliente tem, menor a chance de cancelamento
        - Oferecer serviços extras quase que de forma gratuita
    5 - Clientes com mais linhas (+ dependentes) tem menos chances de cancelar
        - Oferecer segunda linha de graça, ou com desconto
        
    """

