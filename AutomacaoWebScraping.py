#!pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 1 - Pegar a cotação do dólar
# abrir o navegador
navegador = webdriver.Chrome()

# entrar no google
navegador.get("https://www.google.com.br/")

# pesquisar cotacao dolar no google
navegador.find_element('xpath', 
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotacao dolar")
# pressiona enter na pesquisa google
navegador.find_element('xpath',
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
# pega o valor/cotacao (data-value) do dolar
cotacao_dolar = navegador.find_element('xpath',
                      '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar)

# 2 - Pegar a cotação do euro
navegador = webdriver.Chrome()
navegador.get("https://google.com.br/")
navegador.find_element('xpath',
                      '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotacao euro")
navegador.find_element('xpath',
                      '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath',
                       '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_euro)

# 3 - Pegar a cotação do ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element('xpath',
                      '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",", ".")
print(cotacao_ouro)

navegador.quit()

# 4 - Atualizar a base de dados

import pandas as pd

tabela = pd.read_excel("Produtos.xlsx")
print(tabela)

# 5 - Recalcular os preços

# atualizar as cotações
# quando editar um item em específico de acordo com a coluna, usar o tabela.loc
tabela.loc[tabela["Moeda"]=="Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"]=="Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"]=="Ouro", "Cotação"] = float(cotacao_ouro)

# preço de compra = preço de original * cotação
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]
# preço de venda = preço de compra * margem
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]
           
print(tabela)

# 6 - Exportar a base de dados

tabela.to_excel("Produtos Novo.xlsx", index=False)
