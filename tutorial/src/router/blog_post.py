from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional


router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]


@router.post("/new")
def create_blog(blog: BlogModel):
    return "ok"


from fastapi import APIRouter


router = APIRouter(
    prefix="/blog",
    tags=["blog"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
def create_blog():
    pass
