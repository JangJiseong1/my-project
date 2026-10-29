from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.routers import auth, patient, user, prediction

# FastAPI 앱 인스턴스 생성
app = FastAPI(
    title="흉부 X-Ray AI 진단 서비스 API",
    version="1.0.0",
    description="User API 구현 명세",
)

# 1. 정적 파일 디렉토리 연결 (./static 경로)
app.mount("/static", StaticFiles(directory="static"), name="static")


# 2. 메인 페이지('/') 접속 시 프론트엔드 HTML 반환
@app.get("/", summary="프론트엔드 메인 페이지")
def read_index():
  return FileResponse("static/index.html")


# 3. 서버 상태 확인용 헬스체크 (선택사항)
@app.get("/health", summary="서버 상태 확인")
def health_check():
  return {"status": "healthy", "service": "Chest X-Ray AI API"}


# 4. 모든 라우터 등록
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(patient.router)
app.include_router(prediction.router)