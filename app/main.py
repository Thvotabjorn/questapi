from fastapi import FastAPI

from config import GlobalConstants

from config import PG_URL

constants = GlobalConstants()
app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


