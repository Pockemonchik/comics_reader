import asyncio
from typing import AsyncGenerator
from fastapi.testclient import TestClient
from pydantic_settings import BaseSettings

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from pathlib import Path

from src.main import app
from src.db import DatabaseHelper, db_helper
from src.models import BaseModel
from src.core.config import settings


BASE_DIR = Path(__file__).parent


# DATABASE


@pytest.fixture(autouse=True, scope="session")
async def prepare_database():
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
    yield
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)


# SETUP
transport = ASGITransport(app=app)


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(transport=transport, base_url="http://test:8000") as ac:
        yield ac
