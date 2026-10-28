# [6일차] AI 폐렴 예측 API 설계서

## 1. 개요
본서는 흉부 X-ray 이미지 기반 폐렴 예측 AI 모델(EfficientNet-B0)을 활용하여, 진료 기록과 연계된 폐렴 예측 및 결과 조회 기능을 제공하는 FastAPI 기반 RESTful API 설계 명세서입니다.

---

## 2. 기능 요구사항 명세

### (1) REQ-PRED-001: AI 모델 활용 폐렴 예측
* **설명**: 사내 의료인, 개발팀, 연구자 권한을 가진 유저는 진료기록 상세 페이지에서 AI 예측 결과 보기 버튼을 클릭하여 폐렴 예측 결과를 확인할 수 있습니다.
* **상세 규칙**:
  * X-ray 이미지는 진료기록 저장 시 업로드된 이미지를 활용합니다.
  * **캐싱 정책**: 이미 해당 진료기록으로 동일 모델을 사용하여 저장된 예측 결과가 존재하는 경우, 별도의 AI 추론 과정을 거치지 않고 DB에 저장된 데이터를 즉시 응답합니다.
  * **응답 데이터 구조**:
    * 폐렴 여부 (`is_pneumonia`: boolean / True, False)
    * 신뢰도 (`confidence`: float, %)
    * 히트맵 이미지 URL (`heatmap_url`: string, 선택사항)

### (2) REQ-PRED-002: AI 모델 활용 폐렴 예측 결과 조회
* **설명**: 진료기록 상세 페이지의 AI 예측 결과 섹션에서 해당 환자의 X-Ray 사진 및 예측 결과 목록을 조회합니다.
* **목록 필드 항목**:
  * 고유 ID (`prediction_id`)
  * 폐렴 여부 (`is_pneumonia`)
  * 신뢰도 (`confidence`)
  * 히트맵 이미지 URL (`heatmap_url`)
  * 예측 수행 일시 (`predicted_at`)
  * 사용한 모델명 (`model_name`, 예: `EfficientNet-B0`)

---

## 3. 비기능 요구사항 명세

### (1) NFR-PRED-001: AI 모델 평가 기준
* **혼동 행렬(Confusion Matrix) 정의**:
  * **TP (True Positive)**: 폐렴 환자를 폐렴으로 진단
  * **FP (False Positive)**: 정상인이지만 폐렴으로 오진
  * **FN (False Negative)**: 폐렴 환자인데 정상으로 오진 (**⚠️ 가장 위험**)
  * **TN (True Negative)**: 정상인임을 올바르게 진단
* **성능 지표**:
  * **Recall (민감도) ≥ 0.90 ~ 0.95 (최소 0.90)**: 실제 폐렴 환자를 놓치지 않는 지표 (`TP / (TP + FN)`)
  * **Accuracy (정확도) ≥ 0.80 ~ 0.90**: 전체 표본 대비 모델 예측 정확도 (`(TP + TN) / 전체 표본 수`)

### (2) NFR-PRED-002: API 성능
* **응답 속도**: 모든 API 요청은 **3초 이내**에 응답을 완료해야 합니다.

---

## 4. API 엔드포인트 설계 초안

| Method | Endpoint | Description | Request Body / Params | Response |
| :--- | :--- | :--- | :--- | :--- |
| **POST** | `/api/v1/diagnoses/{diagnosis_id}/predict` | AI 폐렴 예측 실행 (또는 기존 결과 조회) | `diagnosis_id` (Path) | 예측 결과 객체 (is_pneumonia, confidence 등) |
| **GET** | `/api/v1/diagnoses/{diagnosis_id}/predictions` | 해당 진료기록의 AI 예측 결과 이력 조회 | `diagnosis_id` (Path) | 예측 결과 목록 리스트 |