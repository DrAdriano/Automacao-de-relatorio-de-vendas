import pyautogui
import pyperclip
import time
import pandas as pd
import smtplib
import email.message

pyautogui.PAUSE = 1

# Passo 1 - Entrando no sistema da empresa.

pyautogui.hotkey("win")
pyperclip.copy("Google Chrome")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")
pyperclip.copy("https://drive.google.com/drive/folders/1t5fxGDQ5BZe18EKEyRtM8yZAlog7b6ZB?usp=sharing")
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

def enviar_email():  
    mensagem_email = f""" <p>Bom dia,</p>

    <p>Venho por meio dessa mensagem gerada automaticamente com Python, expor o relatório de vendas de ontem. O faturamento total 
foi de R$ {faturamento:,.2f}, com um total de {quantidade:,} produtos vendidos.</p>
    <p>Fico à disposição para qualquer dúvida.</p>

    <p>Atenciosamente,</p>
    <p>Adriano Jr. G. Gonçalves</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Relatório de Vendas"
    msg['From'] = 'E-mail de origem'
    msg['To'] = 'E-mail de destino'
    password = 'Senha do Gmail para a Automação'  

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(mensagem_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado com sucesso!')

enviar_email()