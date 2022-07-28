#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install pyautogui


# In[12]:


import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

# 1 entrar no sistema da empresa (no nosso caso vai ser entrar no link)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
# site ta carregando
time.sleep(5)

# 2 navegar no sistema e encontrar a base de dados (entrar na pasta Exportar)
pyautogui.click(x=371, y=298, clicks=2)

# 3 download da base de dados
pyautogui.click(x=407, y=397)  # clicou no arquivo
pyautogui.click(x=1157, y=193) # clicou nos 3 pontinhos
pyautogui.click(x=894, y=557)  # baixou arquivo

# 4 calcular os indicadores (faturamento, quantidade de produtos)
import pandas as pd

tabela = pd.read_excel(r"C:\Users\nicol\Desktop\projetos\Hashtag\Aula 1-20220725T230452Z-001\Aula 1\Exportar\Vendas - Dez.xlsx")
display(tabela)

quantidade = tabela["Quantidade"].sum()
faturamento = tabela["Valor Final"].sum()
print(quantidade)
print(faturamento)

# 5 entrar no email
pyautogui.hotkey("ctrl", "t")                      # abrir nova aba
pyperclip.copy("https://outlook.live.com/mail/0/") # copiando link
pyautogui.hotkey("ctrl", "v")                      # colando link
pyautogui.press("enter")                           # entrando no site
time.sleep(7)

# 6 mandar um email para a diretoria com os indicadores

pyautogui.click(x=195, y=168)                # clicar no botao Nova Mensagem
time.sleep(4)
pyautogui.write("nicolasmonteirog@live.com") # escrever o destinatario
pyautogui.press("tab")                       # confirmar o email
pyautogui.press("tab")                       # entrar no assunto

# assunto
pyperclip.copy("Relatório de Vendas")       # escrever o assunto
pyautogui.hotkey("ctrl", "v")               # cola o assunto
pyautogui.press("tab")                      # entrar no texto

# corpo do texto

texto = f"""Prezados, bom dia

O faturamento de ontem foi de: R$ {faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

Abs
Nicolas Python"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# enviar o texto
pyautogui.hotkey("ctrl", "enter")


# In[24]:


# 4 calcular os indicadores (faturamento, quantidade de produtos)
import pandas as pd

tabela = pandas.read_excel(r"C:\Users\nicol\Desktop\projetos\Hashtag\Aula 1-20220725T230452Z-001\Aula 1\Exportar\Vendas - Dez.xlsx")
display(tabela)


# In[27]:


quantidade = tabela["Quantidade"].sum()
faturamento = tabela["Valor Final"].sum()
print(quantidade)
print(faturamento)


# In[ ]:


pyautogui.hotkey("ctrl", "t") #abrir nova aba
pyperclip.copy("https://outlook.live.com/mail/0/") # copiando link
pyautogui.hotkey("ctrl", "v") #colando link
pyautogui.press("enter") #entrando no site
time.sleep(7)


# In[30]:


#clicar no botao +
pyautogui.click(x=195, y=168)
# escrever o destinatario
pyautogui.write("nicolasmonteirog@live.com")
# escrever o assunto
# escrever o corpo do email
# enviar o email


# 

# In[29]:


time.sleep(6)
pyautogui.position()


# In[7]:


import pyautogui
import pyperclip
import time
# 5 entrar no email
pyautogui.hotkey("ctrl", "t")                      # abrir nova aba
pyperclip.copy("https://outlook.live.com/mail/0/") # copiando link
pyautogui.hotkey("ctrl", "v")                      # colando link
pyautogui.press("enter")                           # entrando no site
time.sleep(7)

# 6 mandar um email para a diretoria com os indicadores

pyautogui.click(x=195, y=168)                # clicar no botao Nova Mensagem
time.sleep(2)
pyautogui.write("nicolasmonteirog@live.com")
pyautogui.press("tab")                       # confirmar o email
pyautogui.press("tab")                       # entrar no assunto

# assunto
pyautogui.write("Relatório de Vendas")       # escrever o assunto
pyautogui.press("tab")                       # entrar no texto

# corpo do texto

texto = f"""Prezados, bom dia

O faturamento de ontem foi de: R$ {faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

Abs
Nicolas Python"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# enviar o texto
pyautogui.hotkey("ctrl", "enter")


# In[ ]:




