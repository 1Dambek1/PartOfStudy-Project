
import typing
from sqlalchemy.orm import  Mapped, mapped_column, relationship


from src.db import Base

if typing.TYPE_CHECKING:

    from src.models.UserModel import User
    from src.models.seller_models.SellerProductModel import SellerProduct
    
class SellerProfile(Base):
    __tablename__ = "seller_profile_table"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    
    shop_name:Mapped[str]
    number:Mapped[str]
    
    is_confirmed:Mapped[bool] = mapped_column(default=False)
    
    user:Mapped["User"] = relationship(back_populates="profile", uselist=False)
    
    products:Mapped[list["SellerProduct"]] = relationship(uselist=True, back_populates="sellerProfile")
    
    