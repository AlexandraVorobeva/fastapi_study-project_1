from fastapi import FastAPI
from . import api


app = FastAPI(
    title='finance api'
)
app.include_router(api.router)