from fastapi import APIRouter, UploadFile, File, HTTPException
from PIL import Image
import io
from worker.model import get_pneumonia_worker

router = APIRouter(
    prefix="/api/v1/predictions",
    tags=["AI Pneumonia Prediction"]
)

@router.post("/predict", summary="흉부 X-ray 이미지 폐렴 예측")
async def predict_pneumonia_image(file: UploadFile = File(...)):
    """
    사용자가 업로드한 흉부 X-ray 이미지 파일을 받아 
    EfficientNet-B0 모델로 폐렴 여부(Normal / Pneumonia)와 신뢰도를 예측합니다.
    """
    # 1. 파일 형식 검증 (이미지 파일 여부 확인)
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="이미지 파일(PNG, JPG 등)만 업로드 가능합니다.")
    
    try:
        # 2. 업로드된 바이트 데이터를 PIL Image 객체로 변환
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        
        # 3. Worker 모델을 통한 추론 수행
        worker = get_pneumonia_worker()
        result = worker.predict(image)
        
        # 4. 결과 반환
        return {
            "success": True,
            "filename": file.filename,
            "data": result
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI 예측 처리 중 오류가 발생했습니다: {str(e)}")