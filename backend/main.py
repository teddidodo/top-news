from fastapi import FastAPI, Depends, HTTPException
from starlette.middleware.cors import CORSMiddleware
from routers import news, users, auth
app = FastAPI()

#: Configure CORS
origins = [
    "http://localhost:8080",
    "https://top-news-td.vercel.app",
    "https://top-news-hck015lyd-teddidodo.vercel.app/"
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
