# 🏥 AI 기반 의료 웹 서비스 프로젝트 (AI Healthcare Web Service)

진료 기록 및 의료 이미지 분석을 통해 복약 안내, 생활 습관 개선 가이드 자동 생성 및 질환 스크리닝을 제공하는 AI 웹 서비스 프로젝트입니다. 프로젝트의 기획부터 배포, QA까지의 전체 진행 과정(Stage 1 ~ 10)을 기록합니다.

---

## 📋 프로젝트 진행 단계 및 과정 총정리

### 1. Team Rule 정의
- **목표 및 규칙 수립**: 협업 및 1인 개발 환경에서의 체계적인 프로세스 시뮬레이션을 위한 그라운드 루루 설정
- **컨벤션 및 워크플로우**:
  - **Commit Message Convention**: `feat`, `fix`, `docs`, `refactor`, `style` 등 명확한 프리픽스 사용
  - **PR(Pull Request) 및 Code Review 규칙**: 기능 단위 개발 후 브랜치 병합 전 변경 사항 검증 원칙 수립

### 2. 사용자 요구사항 정의
- **서비스 핵심 기능**:
  - 환자 진료 기록 및 의료 데이터를 기반으로 한 복약 안내 및 생활 습관 개선 가이드 자동 생성
  - 딥라인 기반 의료 이미지(흉부 X-ray 등) 분류 및 Grad-CAM 시각화를 통한 예측 결과 해석 제공
- **타겟 사용자**: 의료 서비스 이용 환자 및 임상 보조 인력

### 3. API 명세서 작성
- **설계 방향**: RESTful API 디자인 원칙 준수
- **주요 엔드포인트 구성**:
  - 사용자 인증 및 권한 관리 라우터 (`/api/v1/auth`)
  - 환자 진료 기록 및 데이터 조회/저장 라우터 (`/api/v1/patients`)
  - AI 모델 인퍼런스 및 결과 반환 라우터 (`/api/v1/inference`)
- **문서화**: FastAPI 내장 Swagger UI (`/docs`) 및 ReDoc (`/redoc`)을 활용한 실시간 API 명세 연동

### 4. Git & Github Branch 전략 구성
- **Git Flow 기반 브랜치 구조화**:
  - `main`: 제품 배포용 안정 버전 브랜치
  - `develop`: 다음 버전 개발을 위한 통합 브랜치
  - `feature/*`: 개별 기능 구현 및 모듈 개발용 브랜치 (예: `feature/fastapi-setup`, `feature/ai-worker`)
- **병합 프로세스**: 기능 개발 완료 후 `feature` 브랜치에서 `develop` 브랜치로 Pull Request 생성 및 검증 후 병합

### 5. 프로젝트 세팅
- **개발 환경 구축**:
  - Python 가상 환경(`.venv`) 구성 및 `requirements.txt`를 통한 패키지 의존성 관리
  - Windows PowerShell 및 Visual Studio Code 기반 개발 환경 통일
- **디렉토리 구조 설계**:
  - FastAPI 백엔드 애플리케이션 (`app/`)
  - AI 인퍼런스 워커 및 모델 모듈 (`worker/`)
  - 데이터베이스 연동 및 마이그레이션 (`alembic/`, SQLite/SQL DB)

### 6. API 및 AI 워커 코드 작성 후 Branch 전략을 통한 코드 병합
- **백엔드 개발 (`feature/backend-api`)**:
  - FastAPI를 활용한 라우터 및 요청/응답 스키마(Pydantic) 구현
  - Alembic을 이용한 데이터베이스 스키마 마이그레이션 관리 (`sql_app.db`)
- **AI 인퍼런스 워커 개발 (`feature/ai-worker`)**:
  - `worker/model.py` 모듈 구축: PyTorch 기반 딥러닝 모델(EfficientNet / ResNet 등) 탑재
  - 민감도(Sensitivity) 최적화 및 Grad-CAM 시각화 로직 구현
- **코드 병합**: 기능별 브랜치에서 단위 테스트 및 디버깅 완료 후 `develop` 브랜치로 병합 수행

### 7. 아키텍처 설계 및 적용
- **시스템 아키텍처**:
  - **Client Layer**: 프론트엔드 정적 파일 및 UI 인터페이스 (`static/`)
  - **Application Layer**: FastAPI 웹 서버 (비동기 요청 처리 및 API 엔드포인트 제공)
  - **Worker Layer**: 독립된 AI 인퍼런스 워커 모듈 (무거운 이미지 분류 및 텍스트 분석 연산 처리)
  - **Data Layer**: 관계형 데이터베이스 및 마이그레이션 도구 연동

### 8. 도커 인프라 관련 파일 작성
- **컨테이너화 (Containerization)**:
  - 애플리케이션 실행 환경을 표준화하기 위한 `Dockerfile` 작성 (의존성 설치, Uvicorn 서버 구동 설정)
  - 서비스 간 오케스트레이션을 위한 `docker-compose.yml` 구성 (웹 서버와 백엔드/DB 볼륨 마운트 연동)

### 9. AWS 배포
- **클라우드 인프라 구성**:
  - AWS EC2 인스턴스 프로비저닝 및 보안 그룹(포트포워딩) 설정
  - 원격 서버 환경에서의 Docker 및 Docker Compose 구동
  - 환경 변수(`.env`) 및 보안 키 관리 적용을 통한 실서비스 배포 환경 구축

### 10. QA 진행
- **테스트 및 검증**:
  - API 엔드포인트별 응답 속도 및 예외 처리(Traceback 스택 추적 및 디버깅) 검증
  - AI 모델 추론 성능 평가 (Confusion Matrix, 민감도 지표 확인)
  - 배포 환경에서의 엔드투엔드(End-to-End) 시나리오 테스트 완료 후 최종 `main` 브랜치 병합