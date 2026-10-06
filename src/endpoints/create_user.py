from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from typing import Annotated, Any

from src.db.models import User
from src.db.engine import localSession

router = APIRouter(prefix="/create", tags=["USER"])

class Schema(BaseModel):
    tgID: int
    username: str = Field(min_length=5, max_length=20)
    bot_username: str = Field(min_length=5, max_length=20)
    password: str = Field(min_length=5, max_length=20)
    type: str = Field(min_length=2, max_length=3)
    serv_num: int = Field(gt=0)

async def getDB():
    db = localSession()
    try:
        yield db
    finally:
        await db.close()

SessionDep = Annotated[AsyncSession, Depends(getDB)]

@router.post("/user")
async def create(schema: Schema,
                 db: SessionDep) -> Any:
    try:
        stmt = (
            select(User.tgID).
            where(User.tgID == schema.tgID)
        )

        value = await db.scalar(stmt)
        if not value:
            
            add_user = User(
                tgID = schema.tgID,
                username = schema.username,
                bot_username = schema.bot_username,
                password = schema.password,
                type = schema.type,
                serv_num = schema.serv_num
            )

            db.add(add_user)
            await db.commit()

    except Exception as e:
        print(e)