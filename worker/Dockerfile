FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip

# PyTorch CPU 버전 빠르게 설치
RUN pip install --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cpu

# AI 워커에 필요한 핵심 라이브러리 직접 설치 (패키지 빌드 에러 원천 차단!)
RUN pip install --no-cache-dir redis pydantic numpy Pillow sqlalchemy pymysql alembic

# 워커 소스 코드 복사
COPY worker/ ./worker/

CMD ["python", "-m", "worker.main"]