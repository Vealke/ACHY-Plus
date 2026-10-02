from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    ...