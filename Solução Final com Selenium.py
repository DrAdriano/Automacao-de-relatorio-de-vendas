from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import smtplib
import email.message

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service, options=options)


# Passo 1 - Entrando no sistema da empresa.

navegador.get("https://drive.google.com/drive/folders/1t5fxGDQ5BZe18EKEyRtM8yZAlog7b6ZB?usp=sharing")

# Passo 2 - Navegando no sistema e encontrando a base de vendas.

navegador.find_element(By.XPATH, '//*[@id=":1"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz/div/div/div/div').click()
time.sleep(2)

# Passo 3 - Fazendo o download da base de vendas.

navegador.find_element(By.XPATH, '//*[@id=":k"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz/div').click()
time.sleep(2)
navegador.find_element(By.XPATH, '/html/body/div[11]/div[4]/div/div[3]/div[2]/div[2]/div[3]').click()
time.sleep(2)

navegador.quit()

base = pd.read_excel(r"C:\Users\adria\Downloads\Vendas - Dia anterior.xlsx")

# Passo 5 - Calculando os indicadores da empresa.

faturamento = base["Valor Final"].sum()
quantidade = base["Quantidade"].sum()

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