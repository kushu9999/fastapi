from fastapi import FastAPI
from router import blog_get, blog_get_with_prefix

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_get_with_prefix.router)

@app.get("/hello")
def index():
    return {"message": "Hello World"}

