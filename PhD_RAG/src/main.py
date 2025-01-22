from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from PhD_RAG.src.database.router import init_app as init_database

app = FastAPI()


def init_routers(app: FastAPI) -> None:
    """Initialize all routers"""
    init_database(app)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_routers(app)


@app.get("/")
async def root():
    return {"message": "Hello World"}
