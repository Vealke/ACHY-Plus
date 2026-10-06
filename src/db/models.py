from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from sqlalchemy import BIGINT

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    tgID: Mapped[int] = mapped_column(BIGINT, unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    bot_username: Mapped[str] = mapped_column(unique=True)
    type: Mapped[str]
    serv_num: Mapped[str]
    password: Mapped[str]