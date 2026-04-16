from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def hello_world():
    return {"message": "Olá, API Python na Vercel!"}

@app.get("/api/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}