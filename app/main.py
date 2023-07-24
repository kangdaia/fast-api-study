from .musics import musics_router
from .auth import users_router
from fastapi import FastAPI
import logging.config
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

logger = logging.getLogger("FAST API STUDY APP")

# Set logger name to project

logger.info("START Application")

# Tags for representative endpoints
tags = [
    {
        "name": "user",
        "description": "sample CRUD user",
    },
    {
        "name": "music",
        "description": "sample CRUD music by user",
    }
]

# Define Fast api and description
app = FastAPI(
    title="FAST API STUDY APP",
    description="fast api study app: music player",
    version="0.0.1",
    openapi_tags=tags,
)

# CORS (Cross-Origin Resource Sharing) Configuration
origins = [
    "http://localhost",
    "http://localhost:5173",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Add routers to main
app.include_router(users_router.router, prefix="/api/user")
app.include_router(musics_router.router, prefix="/api/musics")


# This path is for health check or test
@app.get("/")
async def root():
    return {"Connect"}
