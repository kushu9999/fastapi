from fastapi import APIRouter, Body, Query
from pydantic import BaseModel
from typing import Optional, List

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

################################################################
#-----------------PATH, QUERY & BODY PARAMETERS-----------------
################################################################

@router.post("/new/{id}")
def create_blog(blog: BlogModel, id:int, version:int = 1):
    return {"id":id,
            "data": blog,
            "version": version}
################################################################
#-----------------PARAMETER METADATA ---------------------------
################################################################

@router.post("/new/{id}/comment")
def create_comment(blog: BlogModel, id:int, comment_id: int = Query(None, title="id of the comment", 
                                                                description="somedscription of comment",
                                                                alias="CommentID",
                                                                deprecated=True)):
    return {'blog': blog,
            'id': id,
            'comment_id': comment_id}

################################################################
#--------------------DATA VALIDATORS ---------------------------
################################################################


# content is non optional parameter
@router.post("/new1/{id}/comment")
def create_comment(blog: BlogModel, id:int, comment_id: int = Query(None, title="id of the comment", 
                                                                description="somedscription of comment",
                                                                alias="CommentID",
                                                                deprecated=True),
                                                                content: str = Body(..., min_length=5, max_length=50, regex='^[a-z\s]*$'),
                                                                v:Optional[List[str]] = Query(None)):
    return {'blog': blog,
            'id': id,
            'comment_id': comment_id,
            'content': content,
            'version': v}
