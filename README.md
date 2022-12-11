# Automação de relatório de vendas

## Sumário

* [Sobre o projeto](#sobre-o-projeto)
* [About the project](#about-the-project)
* [Linguagens e tecnologias usadas](#linguagens-e-tecnologias-usadas)
* [Bibliotecas Python usadas](#bibliotecas-python-usadas)
* [Passo a passo do código](#passo-a-passo-do-código)
* [Conclusões](#conclusões)
* [Créditos](#créditos)
* [Contato](#contato)


<!---* [Captura de tela](#captura-de-tela)--->

## Sobre o projeto

Esse repositório contém uma solução para um desafio envolvendo automação e é organizado de maneira detalhada e acessível, podendo ser entendida por quem está iniciando na linguagem Python.

**Desafio:** Criar um código, usando Python, que acesse os dados de vendas de uma empresa fictícia, calcule o faturamento e a quantidade total de produtos vendidos no dia anterior e envie um e-mail com essas informações. Esse envio de relatório pode ser parte do trabalho diário de um analista de uma empresa.

Desse modo, estão disponibilizados neste repositório: a base de vendas, que contém informações do quantos itens o cliente comprou e quanto custou, por exemplo; a solução detalhada, em que estão explicações e um passo a passo; a solução final, sem a poluição visual dos comentários e adaptada para funcionar através do Visual Code Studio; e a pasta com a captura de tela de como ficou a mensagem do e-mail.

## About the project

This repository contains a solution to a challenge involving automation and is organized in a detailed and accessible way, which can be understood by those who are starting in the Python language.

**Challenge:** Create a code, using Python, that accesses the sales data of a fictitious company, calculates the revenue and the total quantity of products sold the previous day and sends an email with this information. This report submission can be part of the day-to-day work of a company analyst.

Thus, the following are available in this repository: the sales base, which contains information on how many items the customer purchased and how much it cost, for example; the detailed solution, in which there are explanations and a step by step; the final solution, without the visual pollution of comments and adapted to work through Visual Code Studio; and the folder with the screenshot with email message.

## Linguagens e tecnologias usadas

* [Jupyter Notebook](https://jupyter.org/)
* [Visual Studio Code](https://code.visualstudio.com/download)
* [Python 3.11](https://www.python.org/)
* [Markdown](https://www.markdownguide.org/)


## Bibliotecas Python usadas

* [Pandas](https://pandas.pydata.org/)
* [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
* [Pyperclip](https://pypi.org/project/pyperclip/)
* [Time](https://docs.python.org/3/library/time.html)

## Passo a passo do código

* Passo 1: Entrando no sistema da empresa
* Passo 2: Navegando no sistema e encontrando a base de vendas
* Passo 3: Fazendo o download da base de vendas
* Passo 4: Importando a base de vendas pro Python
* Passo 5: Calculando os indicadores
* Passo 6: Enviando o relatório por e-mail

<!---
## Captura de tela 

O e-mail enviado no final do código pode ser visto abaixo.

![Captura de tela](Captura de tela/e-mail.png)
--->

## Conclusões

O código conseguiu fazer o propósito dele, mas tem algumas limitações: Precisa fazer adaptações ao mudar de computador, por conta do comando 'pyautogui.click()'; Os tempos de espera, por serem arbitrários, podem ter situações que não sejam suficientes ou que sejam mais que o necessários, dependendo principalmente da velocidade de internet e do processamento do computador; O código não reconhece sozinho o arquivo correto para baixar, nem qual importar para o Python, se fosse um trabalho diário com um arquivo correto todos os dias, teria que fazer um processo de automação para essas etapas também.

Essa foi minha primeira experiencia com o PyAutoGUI, uma biblioteca que poderia ser melhorada ao disponibilizar maneiras de colocar caracteres especiais, talvez usando o mesmo método que o LaTex. Um ponto interessante dessa biblioteca é que seus bugs são comumente resolvidos dando um intervalo para a próxima linha de código. Além disso, as bibliotecas 'pyperclip' e 'time' combinaram muito bem com ela.

Podemos ainda pensar em algumas possibilidades de melhoria para o código, como otimizar o tempo de resposta, incluir a data no e-mail, incluir o arquivo excel e agendar o programa para executar automaticamente.


## Créditos 

O desafio, bem como muitos detalhes de sua resolução, se devem ao João Lira, do canal do Youtube [Hashtag Programação](https://www.youtube.com/@HashtagProgramacao).

## Contato

Criado por Adriano Jr. G. Gonçalves - Sinta-se
à vontade para contribuições, críticas e/ou sugestões.

<div  align="center"> 
  <a href="https://www.linkedin.com/in/sradriano/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
  <a href = "mailto:sradriano@uel.br"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
</div>