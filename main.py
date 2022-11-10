from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def index():
    return {"message": "Hello World"}

################################################################
#--------------------PATH PARAMETERS----------------------------
################################################################


# take int in api path -> id
@app.get("/blog/{id}")
def get_bog(id):
    return {"message": f"Blog with {id}"}