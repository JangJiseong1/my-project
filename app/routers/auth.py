from fastapi import APIRouter, HTTPException, status, Response
from app.schemas.user import UserCreate, UserLogin

router = APIRouter(prefix="/api/v1/auth", tags=["Auth (인증)"])

@router.post("/signup", status_code=status.HTTP_201_CREATED, summary="회원가입")
def signup(user_data: UserCreate):
    # TODO: DB 중복 검사 및 비밀번호 암호화 후 저장 로직 구현
    return {
        "success": True,
        "message": "회원가입이 성공적으로 완료되었습니다.",
        "data": {
            "email": user_data.email,
            "name": user_data.name,
            "role": "PENDING"
        }
    }

@router.post("/login", status_code=status.HTTP_200_OK, summary="로그인")
def login(credentials: UserLogin, response: Response):
    # TODO: 이메일 및 비밀번호 검증 후 JWT 발행 로직 구현
    # 리프레시 토큰은 HttpOnly 쿠키로 세팅
    response.set_cookie(
        key="refresh_token", 
        value="mock_refresh_token_string", 
        httponly=True, 
        secure=True, 
        samesite="strict"
    )
    return {
        "success": True,
        "message": "로그인 성공",
        "data": {
            "access_token": "mock_access_token_string",
            "token_type": "Bearer",
            "expires_in": 1800
        }
    }