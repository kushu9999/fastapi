from fastapi import FastAPI
from enum import Enum
from typing import Optional
app = FastAPI()

@app.get("/hello")
def index():
    return {"message": "Hello World"}

################################################################
#--------------------PATH PARAMETERS----------------------------
################################################################

# provide all blogs, order is imp so for all we've to write in top of id
@app.get("/blog/all")
def get_blog_order_imp():
    return {"message": "All Blogs Provided"}

# take uservalue in api path -> id
@app.get("/blog/{id}")
def get_blog_with_uservalue(id):
    return {"message": f"Blog with {id}"}

# uservalue validation -> must be an integer
@app.get("/blog2/{id}")
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
@app.get("/blog/type/{type}")
def get_blog_with_predifined_values(type: Blogtype):
    return {"message": f"Blog with {type}"}

################################################################
#---------------------QUERY PAARAMETERS-------------------------
################################################################

# which are the parameters not in path are called queryn parameters
@app.get("/blog3/alls")
def get_all_blog_with_query_parameter(page=1, page_size=10):
    return {"message": f"All {page_size} Blogs on page {page}"}
    
@app.get("/blog4/alls")
def get_all_blog_with_optional_query_parameter(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} Blogs on page {page}"}

################################################################
#---------------------PATH & QUERY PAARAMETERS------------------
################################################################

@app.get("/blog5/{id}/comments/{comment_id}")
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f'blog id = {id}, comment_id = {comment_id}, valid = {valid}, username = {username}'}




