from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

# Đường dẫn đến tệp cơ sở dữ liệu SQLite. 
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# create_async_engine(DATABASE_URL, echo=True): Tạo một engine bất đồng bộ cho SQLAlchemy để kết nối đến cơ sở dữ liệu SQLite. Tham số echo=True sẽ in ra các lệnh SQL thực thi ra console.
engine = create_async_engine(DATABASE_URL, echo=True) 

# sessionmaker(...): Tạo một factory để tạo các phiên làm việc (Session). AsyncSession cho phép các phiên làm việc bất đồng bộ.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# declarative_base(): Cung cấp một cơ sở lớp cơ sở dữ liệu để định nghĩa các mô hình.
Base = declarative_base()

# async def get_db(): Một hàm tạo phiên làm việc cơ sở dữ liệu để sử dụng trong các route của FastAPI.
async def get_db():
    async with SessionLocal() as session:
        yield session