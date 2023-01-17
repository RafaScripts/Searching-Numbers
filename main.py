import requests
from bs4 import BeautifulSoup

urls = [
    "https://receive-smss.com/",
    "https://www.freereceivesms.com/en/br/"
]

headers = {
"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

allsText = []

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


print("done")
