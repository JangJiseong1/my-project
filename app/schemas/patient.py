from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# --- 환자 관련 스키마 ---
class PatientCreate(BaseModel):
    name: str = Field(..., description="환자 이름")
    age: int = Field(..., description="나이")
    gender: str = Field(..., description="성별 (M/F)")
    phone: str = Field(..., description="연락처 (휴대폰 번호)")

class PatientUpdate(BaseModel):
    name: str = Field(..., description="수정할 이름")
    phone: str = Field(..., description="수정할 연락처")

class PatientResponse(BaseModel):
    patientId: int
    name: str
    age: int
    gender: str
    phone: str
    createdAt: datetime
    updatedAt: Optional[datetime] = None

    class Config:
        from_attributes = True

# --- 진료기록 관련 스키마 ---
class MedicalRecordResponse(BaseModel):
    recordId: int
    chartNumber: str
    symptoms: str
    xrayImagePath: Optional[str] = None
    createdAt: datetime

    class Config:
        from_attributes = True