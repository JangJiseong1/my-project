from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite 사용 예시 (필요시 PostgreSQL 등으로 변경 가능)
DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
---

### 2단계: 테스트용 모델 작성하기 (`app/models/user.py`)
Alembic이 감지할 수 있도록 간단한 테이블 모델을 하나 만들어 보겠습니다.
`app/models/user.py` 파일을 만들고 아래 내용을 입력합니다.
```python
from app.core.db.databases import Base
from sqlalchemy import Column, Integer, String


class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  email = Column(String, unique=True, index=True)