from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# 회원가입 요청 스키마
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, description="비밀번호 (8자 이상)")
    name: str
    department: str = Field(..., description="연구, 의료, 개발 중 택일")
    gender: str = Field(..., pattern="^[MF]$", description="성별 M 또는 F")  # regex -> pattern으로 변경
    phone_number: str

# 로그인 요청 스키마
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# 회원 정보 수정 요청 스키마 (Partial)
class UserUpdate(BaseModel):
    department: Optional[str] = None
    phone_number: Optional[str] = None