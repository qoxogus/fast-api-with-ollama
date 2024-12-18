from fastapi import FastAPI
from controller import embedding_controller, completion_controller

app = FastAPI()

app.include_router(embedding_controller.router)
app.include_router(completion_controller.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}