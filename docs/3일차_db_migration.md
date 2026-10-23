# 3일차 프로젝트: DB 모델 설계 및 마이그레이션

## 1. 데이터베이스 선정
- **사용 DB**: SQLite3 (로컬 개발 및 테스트 용이성 고려)
- **ORM / Migration 도구**: SQLAlchemy, Alembic

## 2. ERD 및 모델 구조
- **User 모델 (`app/models/user.py`)**: 사용자 정보 관리 (`id`, `email`, `name`)
- **Item 모델 (`app/models/item.py`)**: 사용자별 아이템/게시글 관리 (`id`, `title`, `description`, `owner_id`)

## 3. 마이그레이션 명령어 수행 결과
```bash
uv run alembic revision --autogenerate -m "create users and items tables"
uv run alembic upgrade head