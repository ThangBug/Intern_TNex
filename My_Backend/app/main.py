from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

# from jose import JWTError, jwt
# from datetime import datetime, timedelta
# from passlib.context import CryptContext
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


from . import crud, models, schemas
from .database import engine, get_db

app = FastAPI()

#
# SECRET_KEY = "thang"
# ALGORITHM = "T2002"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)

# def create_access_token(data: dict, expires_delta: timedelta = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt

# async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
#     credentials_exception = HTTPException(
#         status_code=HTTPException,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception
#     user = await crud.get_user_by_username(db, username=username)
#     if user is None:
#         raise credentials_exception
#     return user
#

# @app.on_event("startup"): Định nghĩa một sự kiện khởi động của FastAPI, sẽ được thực thi khi ứng dụng bắt đầu.
@app.on_event("startup")
async def startup():
    # async with engine.begin() as conn: Mở một kết nối với cơ sở dữ liệu.
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.create_all): Tạo tất cả các bảng từ các mô hình đã định nghĩa.
        await conn.run_sync(models.Base.metadata.create_all)

# @app.post("/items/"): Định nghĩa một endpoint HTTP POST để tạo một item mới. Sử dụng hàm create_item() từ CRUD operations.
@app.post("/items/", response_model=schemas.Item)
async def create_item(item: schemas.ItemCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_item(db, item)

# @app.get("/items/"): Định nghĩa một endpoint HTTP GET để lấy danh sách các item. Sử dụng hàm get_items() từ CRUD operations.
@app.get("/items/", response_model=List[schemas.Item])
async def read_items(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    items = await crud.get_items(db, skip=skip, limit=limit)
    return items

# @app.get("/items/{item_id}"): Định nghĩa một endpoint HTTP GET để lấy thông tin chi tiết về một item dựa trên ID. Sử dụng hàm get_item() từ CRUD operations và trả về lỗi 404 nếu không tìm thấy item.
@app.get("/items/{item_id}", response_model=schemas.Item)
async def read_item(item_id: int, db: AsyncSession = Depends(get_db)):
    db_item = await crud.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy item")
    return db_item

# @app.put("/items/{item_id}", response_model=schemas.Item): Định nghĩa endpoint PUT để cập nhật một item theo ID.
@app.put("/items/{item_id}", response_model=schemas.Item)
async def update_item(item_id: int, item: schemas.ItemUpdate, db: AsyncSession = Depends(get_db)):
    db_item = await crud.update_item(db, item_id, item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy item")
    return db_item

# Câu lệnh @app.delete("/items/{item_id}", response_model=schemas.Item) định nghĩa một API endpoint trong FastAPI để xóa một item trong cơ sở dữ liệu.
@app.delete("/items/{item_id}", response_model=schemas.Item)
async def delete_item(item_id: int, db: AsyncSession = Depends(get_db)):
    db_item = await crud.delete_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy item")
    return db_item


#
# @app.post("/register/", response_model=schemas.User)
# async def register_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
#     hashed_password = get_password_hash(user.password)
#     user.password = hashed_password
#     db_user = await crud.create_user(db, user)
#     return db_user

# @app.post("/token", response_model=schemas.Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
#     user = await crud.get_user_by_username(db, username=form_data.username)
#     if not user or not verify_password(form_data.password, user.hashed_password):
#         raise HTTPException(
#             status_code=400,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
#     return {"access_token": access_token, "token_type": "bearer"}

# @app.get("/users/me/", response_model=schemas.User)
# async def read_users_me(current_user: schemas.User = Depends(get_current_user)):
#     return current_user