import os
import json
import redis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

REDIS_URL = os.getenv("KV_URL")

r = redis.Redis.from_url(REDIS_URL, decode_responses=True)


@app.post("/api")
def enviar_mensagem():
    return {"status": "Mensagem salva no Redis!"}


@app.get("/mensagens")
def listar():
    mensagens_brutas = r.lrange("mensagens_blog", 0, -1)
    return [json.loads(m) for m in mensagens_brutas]
