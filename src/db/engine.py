from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
)

from src.db.config import settings

async_engine = create_async_engine(settings.psycopg_GET_DB, echo=True)
localSession = async_sessionmaker(async_engine)