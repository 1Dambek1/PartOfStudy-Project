import datetime
import typing

from sqlalchemy import text
from sqlalchemy.orm import  Mapped, mapped_column

from ..db import Base


created_at = typing.Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('Europe/Moscow', now())"))]


class User(Base):
    
    __tablename__ = "user_table"

    id:Mapped[int] = mapped_column(primary_key=True)    

    # служебная инфа
    password:Mapped[bytes]
    created_at:Mapped[created_at]
    
    # user инфа
    email:Mapped[str] = mapped_column(unique=True)
    name:Mapped[str]
    surname:Mapped[str]
    dob:Mapped[datetime.date]

    
    
