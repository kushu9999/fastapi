from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/blog", tags=['blog'])

# created model for data input
class BlogModel(BaseModel):
    title: str
    content: str
    comments: int
    published: Optional[bool] 

# post request
@router.post("/new")
def create_blog(blog: BlogModel):
    return "ok"