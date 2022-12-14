import pyautogui
import pyperclip
import time
import pandas as pd

# Passo 1 - Entrando no sistema da empresa.

pyautogui.hotkey("ctrl", "t")
pyperclip.copy(
    "https://drive.google.com/drive/folders/1t5fxGDQ5BZe18EKEyRtM8yZAlog7b6ZB?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)

# Passo 2 - Navegando no sistema e encontrando a base de vendas.

pyautogui.click(x=323, y=289, clicks=2)

time.sleep(2)

# Passo 3 - Fazendo o download da base de vendas.

pyautogui.click(x=323, y=289)
pyautogui.click(x=1163, y=192)
time.sleep(1)
pyautogui.click(x=987, y=564)

time.sleep(5)

# Passo 4 - Importando a base de vendas pro Python.

tabela = pd.read_excel(r"C:\Users\adria\Downloads\Vendas - Dia anterior.xlsx")

# Passo 5 - Calculando os indicadores da empresa.

faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

# Passo 6 - Enviando o relatório por e-mail.

pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=78, y=180)
time.sleep(1.5)

pyautogui.write("pythonimpressionador@gmail.com")
time.sleep(0.5)
pyautogui.press("tab")
pyautogui.press("tab")
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

texto = f"""Bom dia,

Venho por meio dessa, expor o relatório de vendas de ontem. O faturamento total 
foi de R$ {faturamento:,.2f}, com um total de {quantidade:,} produtos vendidos.

Fico à disposição para qualquer dúvida.

Atenciosamente,
Adriano Jr. G. Gonçalves
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("ctrl", "enter")
