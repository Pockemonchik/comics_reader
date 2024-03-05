from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from db import db_helper
from models import BaseModel
from routing.routers import all_routers

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title="API для SteamFriendsBot",lifespan=lifespan)
for router in all_routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)