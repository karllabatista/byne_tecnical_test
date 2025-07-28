from fastapi import FastAPI
from app.interface.controller.even_api import router

app = FastAPI()
app.include_router(router)