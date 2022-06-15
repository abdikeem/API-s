from hashlib import new
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

@app.get("/")
def root():
    return {"message": "Welcome to my FastAPi"}

@app.get("/lesson2")
def lesson2():
    return {"Data": "Welcome to my FastAPi"}

@app.post("/createpost")
def createPost(new_post: Post):
    print(new_post)
    return {"data": "new_post"}

# title str, content str