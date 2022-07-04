from fastapi import FastAPI
from app import router

tutorial_app = FastAPI()
tutorial_app.include_router(router)
