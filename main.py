from fastapi import FastAPI

app = FastAPI()

# read more about decorator
@app.get("/welcome")
def welcom():
    return {"Message": "Hello World!"}