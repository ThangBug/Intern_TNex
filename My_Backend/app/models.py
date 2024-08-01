from sqlalchemy import Column, Integer, String # ForeignKey
from .database import Base
# from sqlalchemy.orm import relationship

# Base: Là cơ sở lớp cho các mô hình SQLAlchemy, được tạo bởi declarative_base().
class Item(Base):

    # __tablename__: Xác định tên bảng trong cơ sở dữ liệu.
    __tablename__ = "items"

    # Column(...): Xác định các cột trong bảng cơ sở dữ liệu với các kiểu dữ liệu và thuộc tính.
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     hashed_password = Column(String)