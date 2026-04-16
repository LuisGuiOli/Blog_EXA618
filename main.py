import os
import redis
import json
from fastapi import FastAPI
from pydantic import BaseModel 
import datetime

app = FastAPI()

# Defina a estrutura que a API espera receber
class Mensagem(BaseModel):
    author: str
    message: str

REDIS_URL = os.getenv("KV_URL")
r = redis.Redis.from_url(REDIS_URL, decode_responses=True)

@app.post("/blog/registrar")
def registrar(item: Mensagem): # Use o modelo aqui
    nova_mensagem = {
        "author": item.author,
        "message": item.message,
        "timestamp": str(datetime.datetime.now())
    }
    
    r.lpush("mensagens_blog", json.dumps(nova_mensagem))
    return {"status": "Mensagem salva no Redis!"}

@app.get("/blog/mensagens")
def listar():
    mensagens = r.lrange("mensagens_blog", 0, -1)
    return [json.loads(m) for m in mensagens]