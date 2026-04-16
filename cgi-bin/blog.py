import os
import json
from fastapi import FastAPI
import datetime

app = FastAPI()

ARQUIVO_JSON = "mensagens.json"

def carregar_dados():
    if not os.path.exists(ARQUIVO_JSON):
        return []
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

@app.post("/blog/registrar")
def registrar(author: str, message: str):
    nova_mensagem = {
        "author": author,
        "message": message,
        "timestamp": str(datetime.datetime.now())
    }
    
    mensagens = carregar_dados()
    
    mensagens.insert(0, nova_mensagem)
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(mensagens, f, indent=4, ensure_ascii=False)
        
    return {"status": "Mensagem salva no arquivo JSON!"}

@app.get("/blog/mensagens")
def listar():
    return carregar_dados()