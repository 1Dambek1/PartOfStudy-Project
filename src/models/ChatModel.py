import typing

from sqlalchemy import ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column,relationship

from src.db import Base

if typing.TYPE_CHECKING:
    from .UserModel import User
    
    

class Chat(Base):
    __tablename__ = "chat_table"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    
    user1_id:Mapped[int] = mapped_column(ForeignKey("user_table.id", ondelete="CASCADE"))
    user1:Mapped["User"] = relationship( uselist=False, foreign_keys=[user1_id])
    
    user2_id:Mapped[int] = mapped_column(ForeignKey("user_table.id", ondelete="CASCADE"))
    user2:Mapped["User"] = relationship( uselist=False, foreign_keys=[user2_id])
    
    messages:Mapped[list["Message"]] = relationship(back_populates="chat", uselist=True)
    
    
class Message(Base):
    __tablename__ = "message_table"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    
    text:Mapped[str]
    
    chat_id:Mapped[int] = mapped_column(ForeignKey("chat_table.id", ondelete="CASCADE"))
    chat:Mapped["Chat"] = relationship(back_populates="messages", uselist=False)
    
    
    
