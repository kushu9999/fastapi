from fastapi import APIRouter

router = APIRouter(prefix="/prefixblog", tags=["prefix"])
# prefix="/blog", tags=["blog"]

################################################################
#--------------------PATH PARAMETERS----------------------------
################################################################

# provide all blogs, order is imp so for all we've to write in top of id
@router.get("/all")
def get_blog_order_imp():
    return {"message": "All Blogs Provided"}

# take uservalue in api path -> id
@router.get("/{id}")
def get_blog_with_uservalue(id: int):
    return {"message": f"Blog with {id}"}
