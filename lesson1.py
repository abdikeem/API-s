from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to my FastAPi"}

@app.get("/lesson2")
def lesson2():
    return {"Data": "Welcome to my FastAPi"}

@app.post("/createpost")
def createPost(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}
