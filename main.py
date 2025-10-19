
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple Microservice - Step1")

class MessageIn(BaseModel):
    name: str | None = "there"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello(name: str | None = None):
    if name:
        return {"message": f"Hello, {name}!"}
    return {"message": "Jai Ganesh..."}

@app.post("/greet")
def greet(data: MessageIn):
    return {"message": f"Hello, {data.name} — this response is from the microservice."}

