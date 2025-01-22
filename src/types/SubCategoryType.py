from pydantic import BaseModel

from .CategoryType import CategoryType
class SubCategoryType(BaseModel):
    
    id:int
    name:str
    
    category:CategoryType