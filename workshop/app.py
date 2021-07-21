from fastapi import FastAPI
from . import api


app = FastAPI()

#
# @app.get('/')
# def root():
#     return{'messege': "hello"}

app.include_router(api.router)