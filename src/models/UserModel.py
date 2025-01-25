import datetime
import typing

from sqlalchemy import ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column,relationship

from src.db import Base

if typing.TYPE_CHECKING:
    from src.models.seller_models.SellerProductModel import SellerProduct
    from src.models.seller_models.SellerProfileModel import SellerProfile
    from src.models.seller_models.ReviewModel import Review
    from .OrdersModel import Orders

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
    
    profile_id:Mapped[int] = mapped_column(ForeignKey("seller_profile_table.id"), nullable=True)
    profile:Mapped["SellerProfile"] = relationship(back_populates="user", uselist=False)

    reviews:Mapped[list["Review"]] = relationship(uselist=True, back_populates="user")
    
    backet:Mapped[list["SellerProduct"]] = relationship(uselist=True, back_populates="backets", secondary="client_backet_table")


    orders:Mapped[list["Orders"]] = relationship(uselist=True, back_populates="user")