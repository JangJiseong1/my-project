from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
import os
import sys

# 프로젝트 루트 디렉터리를 파이썬 경로(sys.path)에 추가하여 app 모듈을 읽을 수 있게 함
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 우리가 만든 Base와 모델들을 임포트
from app.core.db.databases import Base
from app.models.user import User  # Alembic이 감지할 모델 파일들

# target_metadata를 None에서 Base.metadata로 변경
target_metadata = Base.metadata
*(팁: `target_metadata = None`으로 되어 있는 부분을 찾아서 `target_metadata = Base.metadata`로 수정하시면 됩니다.)*

---

### 4단계: `alembic.ini` 파일에서 DB 주소 연결하기
1. 프로젝트 루트에 있는 **`alembic.ini`** 파일을 엽니다.
2. `sqlalchemy.url`로 시작하는 줄을 찾아 데이터베이스 주소를 지정합니다.
   ```ini
   # 기존에 주석 처리되어 있거나 다른 값으로 된 부분을 아래처럼 수정
   sqlalchemy.url = sqlite:///./sql_app.db
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
