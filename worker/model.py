import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

class PneumoniaInferenceWorker:
    """
    흉부 X-ray 이미지를 받아 폐렴 여부(Normal / Pneumonia)를 예측하는 추론 클래스입니다.
    노트북에서 학습한 EfficientNet-B0 구조 및 전처리 파이프라인을 그대로 적용합니다.
    """
    def __init__(self, model_path: str = 'worker/models/best_model.pth'):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # 1. EfficientNet-B0 모델 아키텍처 정의 (노트북 구조와 동일)
        self.model = models.efficientnet_b0(weights=None)
        num_ftrs = self.model.classifier[1].in_features
        self.model.classifier[1] = nn.Linear(num_ftrs, 2)  # 이진 분류 (0: Normal, 1: Pneumonia)
        
        # 2. 학습된 가중치(.pth) 로드
        if os.path.exists(model_path):
            state_dict = torch.load(model_path, map_location=self.device)
            self.model.load_state_dict(state_dict)
        else:
            # 가중치 파일이 아직 없는 경우 경고 메시지 출력 (테스트용)
            print(f"[Warning] 모델 가중치 파일을 찾을 수 없습니다: {model_path}")
            
        self.model.to(self.device)
        self.model.eval()
        
        # 3. 이미지 전처리 파이프라인 (노트북 val_test_transforms와 동일)
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406], 
                std=[0.229, 0.224, 0.225]
            )
        ])

    def predict(self, image_input):
        """
        이미지 파일 경로(str) 또는 PIL Image 객체를 입력받아 예측 결과를 반환합니다.
        
        :param image_input: str 또는 PIL.Image.Image
        :return: dict (결과 클래스, 신뢰도, 클래스별 확률)
        """
        # 이미지 입력 타입 체크 및 RGB 변환
        if isinstance(image_input, str):
            image = Image.open(image_input).convert('RGB')
        elif isinstance(image_input, Image.Image):
            image = image_input.convert('RGB')
        else:
            raise ValueError("지원하지 않는 이미지 입력 형식입니다. (파일 경로 또는 PIL Image 필요)")
            
        # 전처리 및 배치 차원 추가 ([C, H, W] -> [1, C, H, W])
        tensor_img = self.transform(image).unsqueeze(0).to(self.device)
        
        # 추론 수행 (소프트맥스로 확률 산출)
        with torch.no_grad():
            outputs = self.model(tensor_img)
            probabilities = torch.softmax(outputs, dim=1)
            pred_class = torch.argmax(probabilities, dim=1).item()
            confidence = probabilities[0][pred_class].item()
            
        # 클래스 라벨 (0: Normal / 정상, 1: Pneumonia / 폐렴)
        class_names = ["Normal", "Pneumonia"]
        
        return {
            "result": class_names[pred_class],
            "confidence": round(confidence * 100, 2),
            "probabilities": {
                "Normal": round(probabilities[0][0].item() * 100, 2),
                "Pneumonia": round(probabilities[0][1].item() * 100, 2)
            }
        }

# 싱글톤 패턴: FastAPI 등 서버 애플리케이션에서 매번 모델을 다시 로드하지 않도록 메모리에 1회만 올려 재사용합니다.
_worker_instance = None

def get_pneumonia_worker():
    """
    PneumoniaInferenceWorker 싱글톤 인스턴스를 반환합니다.
    """
    global _worker_instance
    if _worker_instance is None:
        _worker_instance = PneumoniaInferenceWorker()
    return _worker_instance


# 스크립트 직접 실행 시 간단 테스트 예시
if __name__ == "__main__":
    # 테스트 코드는 가중치 파일과 샘플 이미지가 존재할 때 실행됩니다.
    print("Device in use:", torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
    print("worker/model.py 준비 완료.")