from fastapi import FastAPI
from app.apis.practice_apis import router as practice_router

app = FastAPI(
    title="My Team Project",
    description="GitHub Flow 실습을 위한 FastAPI 프로젝트",
    version="1.0.0"
)

# practice_apis 라우터 추가
app.include_router(practice_router)

@app.get("/")
def root():
    return {"status": "Server is running successfully!"}