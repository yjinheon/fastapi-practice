from fastapi import APIRouter
from fastapi import status
from fastapi import Response
from typing import Optional
from enum import Enum

router = APIRouter(
        prefix="/blog",
        tags=["blog"],
        responses={404: {"description": "Not found"}},
        )


class BlogType(str, Enum):
    short = "short"
    long = "long"
    howto = "howto"


# 경로가 고정되어 있기 때문에 값을 받는 operation 보다 먼저 정의되어야 한다.
@router.get(
    "/all",
    tags=["blog"],
    summary="Retrive all blogs",
    description="Retrive all blogs from database",
    response_description="List of available blogs",
)
def get_all_blogs(page=1, page_size: Optional[int] = None):
    # Union[int, None] = Optional[int] 와 같다.
    return {"Message": f"All blogs page is {page} and page_size is {page_size}"}


@router.get("/type/{type}", tags=["blog"])
def get_blog_type(type: BlogType):
    return {"Data": f"Blog type is {type}"}


# 특정 값을 중괄호 안에 받기 때문에 operation이다.
@router.get("/{id}", status_code=status.HTTP_404_NOT_FOUND, tags=["blog"])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "blog id not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"Message": f"blog id is {id}"}


@router.get("/{id}/comments/{comment_id}", tags=["blog", "comment"])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulate a blog comment : Descriotion 대신 사용할 수 있다.
    """
    return {
        "Message": f"blog id is {id} and comment id is {comment_id} and valid is {valid} and username is {username}"
    }

