from fastapi import APIRouter, status, Response
from typing import Optional
from enum import Enum

router = APIRouter()
# prefix="/blog", tags=["blog"]

################################################################
#--------------------PATH PARAMETERS----------------------------
################################################################

# provide all blogs, order is imp so for all we've to write in top of id
@router.get("/blog/all")
def get_blog_order_imp():
    return {"message": "All Blogs Provided"}

# take uservalue in api path -> id
@router.get("/blog/{id}")
def get_blog_with_uservalue(id):
    return {"message": f"Blog with {id}"}

# uservalue validation -> must be an integer
@router.get("/blog2/{id}")
def get_blog_with_uservalue_validation(id: int):
    return {"message": f"Blog with {id}"}


################################################################
#---------------------PREDEFINED VALUES-------------------------
################################################################

class Blogtype(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

# tpredefined values
@router.get("/blog/type/{type}")
def get_blog_with_predifined_values(type: Blogtype):
    return {"message": f"Blog with {type}"}

################################################################
#---------------------QUERY PAARAMETERS-------------------------
################################################################

# which are the parameters not in path are called queryn parameters
@router.get("/blog3/alls")
def get_all_blog_with_query_parameter(page=1, page_size=10):
    return {"message": f"All {page_size} Blogs on page {page}"}
    
@router.get("/blog4/alls")
def get_all_blog_with_optional_query_parameter(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} Blogs on page {page}"}

################################################################
#---------------------PATH & QUERY PAARAMETERS------------------
################################################################

@router.get("/blog5/{id}/comments/{comment_id}")
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f'blog id = {id}, comment_id = {comment_id}, valid = {valid}, username = {username}'}


################################################################
#---------------------STATUS CODE PARAMETERS--------------------
################################################################

@router.get("/blog6/{id}",  status_code=status.HTTP_200_OK)
def get_blog_with_statuscode(id:int, response: Response):
    if id > 5:
        # response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with {id}"}
    else :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"Blog with {id} not found"}


################################################################
#------------------------TAG PARAMETERS-------------------------
################################################################

@router.get("/blog7/{id}", tags=['blog7'])
def get_blog_with_tag(id: int):
    return {'message':"this is blog tag"}

@router.get("/blog7/{id}/comments/{comment_id}", tags=['blog7','comments'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f'blog id = {id}, comment_id = {comment_id}, valid = {valid}, username = {username}'}

################################################################
#----------------SUMMARY AND DESCRIPTION------------------------
################################################################

@router.get("/blog8/all", tags=['summary and description'], summary="Retrieve All Blogs", description="This api simulates fetching all blogs")
def get_blog_with_summary():
    return {'message': 'This api simulates fetching all blogs'}

@router.get("/blog5/{id}/comments/{comment_id}", tags=['summary and description'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    simulates retriving blogs

    - **id** mandatody path parameter
    - **comment** mandatody path parameter
    - **valid** query parameter
    - **username** optional query parameter
    """
    return {'message': f'blog id = {id}, comment_id = {comment_id}, valid = {valid}, username = {username}'}


################################################################
#-------------------Response Description------------------------
################################################################

@router.get("/blog9/all", tags=['response description'], summary="Response description", description="This api simulates fetching all blogs", response_description="The list of available blogs")
def get_blog_with_summary():
    return {'message': 'This api simulates fetching all blogs'}
