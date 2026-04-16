import redis
from fastapi import FastAPI
import os
import json

app = FastAPI()
REDIS_URL = os.getenv("KV_URL")

r = redis.Redis.from_url(REDIS_URL, decode_responses=True)

@app.get("/blog/mensagens")
def listar():
    mensagens_brutas = r.lrange("mensagens_blog", 0, -1)
    return [json.loads(m) for m in mensagens_brutas]