from logging.config import fileConfig
import os
import sys

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# 프로젝트 루트 경로를 파이썬 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# 1. 데이터베이스 Base 및 모델 임포트
from app.core.db.databases import Base
from app.models.user import User  

# Alembic 설정 객체
config = context.config

# 로깅 설정
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 2. target_metadata에 Base.metadata 연결
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
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
    """Run migrations in 'online' mode."""
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