import os
import datetime
import urllib.parse

documento = "blog.txt"

print("Content-type: text/html charset=utf-8\n")   

qs = os.environ["QUERY_STRING"]
list = urllib.parse.parse_qs(qs, encoding="latin-1")
var = list["author"][0]

dados ={}
if qs:
    dados["nome"] = var
    dados["mensagem"] = list["message"][0]

with open(documento, "a") as arquivo:
    arquivo.write(f"\n{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} \nUser: {var}\nMensagem: {list['message'][0]}\n")


with open(documento, "r") as arquivo:
    print()
    for linha in arquivo:
        print(f"""
            <span >{linha}</span><br>""")
print("</body></html>")