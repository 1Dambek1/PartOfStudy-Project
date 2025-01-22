from pydantic import BaseModel
from .SubCategoryType import SubCategoryType

class ProductType(BaseModel):
    
    id:int
    name:str
    description:str
    img: str | None
    subCategory:SubCategoryType