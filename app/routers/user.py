from fastapi import APIRouter, Depends, status
from app.schemas.user import UserUpdate

router = APIRouter(prefix="/api/v1/users", tags=["User (사용자)"])

@router.get("/me", status_code=status.HTTP_200_OK, summary="마이페이지 본인 정보 조회")
def get_my_info():
    # TODO: JWT 토큰을 기반으로 현재 로그인된 유저 정보 반환
    return {
        "success": True,
        "data": {
            "user_id": 1,
            "name": "홍길동",
            "email": "user@hospital.com",
            "department": "MEDICAL",
            "gender": "M",
            "phone_number": "010-1234-5678",
            "role": "STAFF"
        }
    }

@router.patch("/me", status_code=status.HTTP_200_OK, summary="회원 정보 수정 (Partial)")
def update_my_info(update_data: UserUpdate):
    # TODO: 전달된 필드만 선택적으로 수정 (Partial Update)
    return {
        "success": True,
        "message": "회원 정보가 수정되었습니다.",
        "data": update_data.dict(exclude_unset=True)
    }