from fastapi import FastAPI

app = FastAPI()

# path operations are evaluated in order
# https://fastapi.tiangolo.com/tutorial/path-params/#order-matters


@app.get("/")
async def index():
    return {"message": "Hello World"}
