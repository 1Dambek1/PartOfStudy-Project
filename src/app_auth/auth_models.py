import datetime
import typing

from sqlalchemy import text
from sqlalchemy.orm import  Mapped, mapped_column

from ..db import Base




class User(Base):
    
    __tablename__ = "user_table"

    id:Mapped[int] = mapped_column(primary_key=True)    

    # служебная инфа
    password:Mapped[bytes]
    
    # user инфа
    email:Mapped[str] = mapped_column(unique=True)
    name:Mapped[str]
    surname:Mapped[str]
    dob:Mapped[datetime.date]

    
    
