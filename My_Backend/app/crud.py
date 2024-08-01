from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Item
from .schemas import ItemCreate, ItemUpdate
# from .import models, schemas

# get_item(): Lấy một item theo ID.
async def get_item(db: AsyncSession, item_id: int):
    result = await db.execute(select(Item).filter(Item.id == item_id))
    return result.scalar_one_or_none()

# get_items(): Lấy danh sách các item với phân trang (skip và limit).
async def get_items(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Item).offset(skip).limit(limit))
    return result.scalars().all()

# create_item(): Tạo một item mới và lưu vào cơ sở dữ liệu.
async def create_item(db: AsyncSession, item: ItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item

# update_item(): Cập nhật item
async def update_item(db: AsyncSession, item_id: int, item: ItemUpdate):
    db_item = await get_item(db, item_id)
    if db_item is None:
        return None
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    await db.commit()
    await db.refresh(db_item)
    return db_item

# delete(): Xóa item
async def delete_item(db: AsyncSession, item_id: int):
    db_item = await get_item(db, item_id)
    if db_item is None:
        return None
    await db.delete(db_item)
    await db.commit()
    return db_item


# async def create_user(db: AsyncSession, user: schemas.UserCreate):
#     db_user = models.User(username=user.username, hashed_password=user.password)
#     db.add(db_user)
#     await db.commit()
#     await db.refresh(db_user)
#     return db_user

# async def get_user_by_username(db: AsyncSession, username: str):
#     result = await db.execute(select(models.User).filter(models.User.username == username))
#     return result.scalars().first()