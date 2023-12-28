from fastapi import FastAPI
from router import blog_get
from router import blog_post
from typing import Optional

# logging
import logging

#logger = logging.getLogger(__name__)


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/")
def index():
#    logger.info(f"request / endpoint!")
    return {"Message": "Hello FastAPI"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


# @app.on_event("startup")
# async def startup_event():
#      logger = logging.getLogger("uvicorn access")
#      handler = logging.FileHandler(filename="access.log", encoding="utf-8")
#      handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s"))
#      logger.addHandler(handler)
