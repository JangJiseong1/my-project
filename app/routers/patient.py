from fastapi import APIRouter, HTTPException, UploadFile, File, Form, Query, status
from typing import List, Optional
from datetime import datetime
from app.schemas.patient import PatientCreate, PatientUpdate, PatientResponse, MedicalRecordResponse

router = APIRouter(prefix="/api", tags=["환자 및 진료기록 관리"])

# 가상의 인메모리 데이터베이스 (실제 DB 연동 시 ORM으로 대체)
fake_patients_db = []
fake_records_db = []
patient_id_counter = 1
record_id_counter = 1

# --- 1. 환자 정보 등록 (REQ-PTNT-001) ---
@router.post("/patients", response_model=PatientResponse, status_code=status.HTTP_201_CREATED)
def create_patient(patient: PatientCreate):
    global patient_id_counter
    new_patient = {
        "patientId": patient_id_counter,
        "name": patient.name,
        "age": patient.age,
        "gender": patient.gender,
        "phone": patient.phone,
        "createdAt": datetime.now(),
        "updatedAt": datetime.now()
    }
    fake_patients_db.append(new_patient)
    patient_id_counter += 1
    return new_patient

# --- 2. 환자 목록 조회 (REQ-PTNT-002) ---
@router.get("/patients", response_model=List[PatientResponse])
def get_patients(
    search: Optional[str] = Query(None, description="이름 기준 검색"),
    gender: Optional[str] = Query(None, description="성별 필터"),
    minAge: Optional[int] = Query(None, description="최소 나이"),
    maxAge: Optional[int] = Query(None, description="최대 나이")
):
    results = fake_patients_db
    if search:
        results = [p for p in results if search in p["name"]]
    if gender:
        results = [p for p in results if p["gender"] == gender]
    if minAge is not None:
        results = [p for p in results if p["age"] >= minAge]
    if maxAge is not None:
        results = [p for p in results if p["age"] <= maxAge]
    return results

# --- 3. 환자 정보 상세 조회 (REQ-PTNT-003) ---
@router.get("/patients/{patientId}", response_model=PatientResponse)
def get_patient(patientId: int):
    patient = next((p for p in fake_patients_db if p["patientId"] == patientId), None)
    if not patient:
        raise HTTPException(status_code=404, detail="환자를 찾을 수 없습니다.")
    return patient

# --- 4. 환자 정보 수정 (REQ-PTNT-004) ---
@router.put("/patients/{patientId}", response_model=PatientResponse)
def update_patient(patientId: int, update_data: PatientUpdate):
    patient = next((p for p in fake_patients_db if p["patientId"] == patientId), None)
    if not patient:
        raise HTTPException(status_code=404, detail="환자를 찾을 수 없습니다.")
    patient["name"] = update_data.name
    patient["phone"] = update_data.phone
    patient["updatedAt"] = datetime.now()
    return patient

# --- 5. 환자 정보 삭제 및 연관 진료기록 영구 삭제 (REQ-PTNT-005) ---
@router.delete("/patients/{patientId}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(patientId: int):
    global fake_patients_db, fake_records_db
    patient = next((p for p in fake_patients_db if p["patientId"] == patientId), None)
    if not patient:
        raise HTTPException(status_code=404, detail="환자를 찾을 수 없습니다.")
    # 환자 삭제
    fake_patients_db = [p for p in fake_patients_db if p["patientId"] != patientId]
    # 연관된 진료기록 및 X-Ray 이미지 데이터 함께 영구 삭제
    fake_records_db = [r for r in fake_records_db if r["patientId"] != patientId]
    return None

# --- 6. 진료기록 등록 (REQ-MDR-001) ---
@router.post("/patients/{patientId}/medical-records", response_model=MedicalRecordResponse, status_code=status.HTTP_201_CREATED)
async def create_medical_record(
    patientId: int,
    medicalInfo: str = Form(...),
    chartNumber: str = Form(...),
    symptoms: str = Form(...),
    xrayImage: UploadFile = File(...)
):
    global record_id_counter
    patient = next((p for p in fake_patients_db if p["patientId"] == patientId), None)
    if not patient:
        raise HTTPException(status_code=404, detail="존재하지 않는 환자입니다.")
    
    # 로컬 저장소 저장 시뮬레이션 (실제 구현 시 파일 저장 로직 추가)
    file_path = f"./uploads/{xrayImage.filename}"

    new_record = {
        "recordId": record_id_counter,
        "patientId": patientId,
        "medicalInfo": medicalInfo,
        "chartNumber": chartNumber,
        "symptoms": symptoms,
        "xrayImagePath": file_path,
        "createdAt": datetime.now()
    }
    fake_records_db.append(new_record)
    record_id_counter += 1
    return new_record

# --- 7. 진료기록 목록 조회 (REQ-MDR-002) ---
@router.get("/patients/{patientId}/medical-records", response_model=List[MedicalRecordResponse])
def get_medical_records(patientId: int):
    records = [r for r in fake_records_db if r["patientId"] == patientId]
    # 증상 100자 초과 시 ... 생략 형태 처리
    for r in records:
        if len(r["symptoms"]) > 100:
            r["symptoms"] = r["symptoms"][:100] + "..."
    return records

# --- 8. 진료기록 상세 조회 (REQ-MDR-003) ---
@router.get("/medical-records/{recordId}", response_model=MedicalRecordResponse)
def get_medical_record(recordId: int):
    record = next((r for r in fake_records_db if r["recordId"] == recordId), None)
    if not record:
        raise HTTPException(status_code=404, detail="진료기록을 찾을 수 없습니다.")
    return record