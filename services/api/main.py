from fastapi import FastAPI
from services.api.router import blog_get, blog_get_with_prefix, blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_get_with_prefix.router)
app.include_router(blog_post.router)

@app.get("/")
def index():
    return {"message": "Hello World"}

