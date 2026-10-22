from fastapi import APIRouter

# APIRouter 설정 (프리픽스와 태그 지정)
router = APIRouter(
    prefix="/practice",
    tags=["Practice API"]
)

@router.get("/")
def read_practice():
    return {"message": "FastAPI 연습용 API에 오신 것을 환영합니다!"}

@router.get("/{name}")
def say_hello(name: str):
    return {"message": f"안녕하세요, {name}님! GitHub Flow 실습 중입니다."}