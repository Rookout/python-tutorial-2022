from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app import router


def main():
    import rook
    rook.start(
        token="[Your Rookout Token]",
        labels={"env": "dev"}
        # When using multiprocessing, enable fork support to load Rookout in all workers
        # , fork=True
    )
    app = FastAPI()
    app.include_router(router)
    app.mount("/", StaticFiles(directory="static", html=True), name="static")
    return app
