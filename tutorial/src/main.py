from fastapi import FastAPI
from router import blog_get
from typing import Optional

app = FastAPI()
app.include_router(blog_get.router)

@app.get("/")
def index():
    return {"Message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


