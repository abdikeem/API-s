from fastapi import FastAPI

app = FastAPI()

@app.get("/lesson2")
def root():
    return {"Data": "Welcome to my FastAPi"}
