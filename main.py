# from sqlalchemy import (
#     create_engine,
#     databases
# )

# from sqlalchemy.databases import postgresql


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def say_hello():
    """Greeting"""
    return {"msg": "Hello World"}
