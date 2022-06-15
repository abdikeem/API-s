from hashlib import new
from typing import Optional
from click import option
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"message": "Welcome to my FastAPi"}

@app.get("/lesson2")
def lesson2():
    return {"Data": "Welcome to my FastAPi"}

@app.post("/createpost")
def createPost(post : Post):
    print(post.rating)
    print(post.dict())
    return {"data": post}

# title str, content str