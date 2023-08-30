from fastapi import APIRouter


router = APIRouter(
    prefix="/blog",
    tags=["blog"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
def create_blog():
    pass
