from fastapi import FastAPI
from app.routers import patient, user, prediction

# FastAPI 앱 인스턴스는 하나만 생성합니다.
app = FastAPI(
    title="흉부 X-Ray AI 진단 서비스 API",
    version="1.0.0",
    description="User API 구현 명세"
)

# 모든 라우터 등록
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(patient.router)
app.include_router(prediction.router)   

@app.get("/", summary="서버 상태 확인")
def health_check():
    return {"status": "healthy", "service": "Chest X-Ray AI API"}