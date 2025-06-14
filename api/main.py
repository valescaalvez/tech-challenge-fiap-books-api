from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/predict")
def predict(input_data: dict):
    return {"result": f"Você enviou: {input_data}"}
