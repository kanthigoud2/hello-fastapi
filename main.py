from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"message": "Hello Srikanth"}
@app.get("/balance")
def get_balance():
    return {"user": "Srikanth", "balance": 1250}
