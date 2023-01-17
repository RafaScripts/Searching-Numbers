# Seaching numbers

Web scrapping construido em python para varrer sites de numeros gratuitos para sms e coletar os mesmos e salvar em um arquivo .csv

## funcionamento

importa-se as blibiotecas requests e bs4 para requisição do site e coleta de seu html.

~~~ python
import requests
from bs4 import BeautifulSoup
~~~

declara-se um array de urls dos sites aos quais serão acessados e um header para se passar como um computador acessando.

~~~python
urls = [
    "https://receive-smss.com/",
    "https://www.freereceivesms.com/en/br/"
]

headers = {
"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
~~~

após isso é iniciado um loop for que acessa os sites e mapeia todas as tags h4

~~~python
for ge in urls:
    site = requests.get(ge, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    h4s = soup.find_all('h4')

    for x in h4s:
        if "+55" in x.getText():
            if " " in x.getText():
                sp = x.getText().split(" ")
                jn = "".join(sp)
                with open('numerosBr.csv', 'a', newline='', encoding='UTF-8') as f:
                    f.write(jn + ';')
            else:
                with open('numerosBr.csv', 'a', newline='', encoding='UTF-8') as f:
                    f.write(x.getText() + ';')
        else:
            if "+" in x.getText():
                with open("numerosOutrosPaises.csv", 'a', newline='', encoding='UTF-8') as w:
                    w.write(x.getText() + ';')
~~~

neste mesmo loop à um outro loop para mapear todo o texto retornado do array de tags h4 e buscar entre eles os textos com DDI "+55" e escreve-los em um arquivo .csv. Caso haja espaçamento concatena-se para que fique no formato "+55XX9XXXXXXXX".

a terceira condição é para mapear os numeros de outros paises e salva-los em um arquivo .csv diferente.

para rodar o codigo execute a instalação das blibiotecas (caso não tenha):

~~~
pip install requests
pip install bs4
~~~

após isso rode:

~~~
python3 main.py
~~~

<p style="color: blueviolet">desenvolvidor por: <a href="https://github.com/rafascripts">RafaScripts</a></p>