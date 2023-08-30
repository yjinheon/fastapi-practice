from fastapi import FastAPI
from router import blog_get
from router import blog_post
from typing import Optional

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/")
def index():
    return {"Message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
