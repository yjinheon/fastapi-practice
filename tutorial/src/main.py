from fastapi import FastAPI
from router import blog_get
from router import blog_post
from router import blog_post
from typing import Optional

# logging
import logging

# logger = logging.getLogger(__name__)


app = FastAPI()
app.include_router(blog_get.router)


@app.get("/")
def index():
    #    logger.info(f"request / endpoint!")
    return {"Message": "Hello FastAPI"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
