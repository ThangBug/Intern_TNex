# Sử dụng thư viện pydantic để quản lý dữ liệu đầu vào và đầu ra
from pydantic import BaseModel
# from typing import Optional

class ItemBase(BaseModel):
    name: str
    description: str

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


# class UserBase(BaseModel):
#     username: str

# class UserCreate(UserBase):
#     password: str

# class User(UserBase):
#     id: int

#     class Config:
#         orm_mode = True

# class Token(BaseModel):
#     access_token: str
#     token_type: str

# class TokenData(BaseModel):
#     username: Optional[str] = None
