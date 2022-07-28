from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app import router


def main():
    app = FastAPI()
    app.include_router(router)
    app.mount("/", StaticFiles(directory="static", html=True), name="static")
    return app
