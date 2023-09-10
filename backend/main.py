from fastapi import FastAPI, Depends, HTTPException, APIRouter
# from sqlalchemy.orm import SessionS
from typing import List
# from model import Dynasty, Event
# from schema import DynastySchema, EventSchema
# from session import create_get_session
from starlette.middleware.cors import CORSMiddleware
# import random
# from sqlalchemy import func

from routers import news, users, auth

app = FastAPI()
router = APIRouter()

#: Configure CORS
origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Server is up and running!"}

app.include_router(
    news.router,
    tags=[
        "news"
    ],
)

app.include_router(
    auth.router,
    tags=[
        'auth'
    ],
)

app.include_router(
    users.router,
    tags=[
        'users'
    ],
)
