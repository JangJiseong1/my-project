# 5일차 진료기록 및 환자 관리 API 설계서

## 1. 개요
본 문서는 제공된 사용자 요구 사항 정의서(환자 관리 및 진료기록 관리)를 바탕으로 작성된 백엔드 API 명세서입니다.

---

## 2. 공통 및 비기능 요구사항
- **API 성능 (NFR-PTNT-001, NFR-MDR-001)**: 모든 유저 API는 요청 접수부터 응답 반환까지 **최대 3초 이내**에 로직을 처리하고 응답해야 함.
- **인증 및 권한 (RBAC)**:
  - **사내 의료인 (Medical Staff)**: 환자 등록/수정/삭제, 진료기록 등록/조회/수정/삭제
  - **사내 개발진 (Developer)** / **의료 실무진 (Practical Medical Staff)** / **연구진 (Researcher)**: 환자 정보 및 진료기록 조회/수정/삭제

---

## 3. 환자 관리 API 명세

### 3.1. 환자 정보 등록 (REQ-PTNT-001)
- **HTTP Method & URL**: `POST /api/patients`
- **권한**: 사내 의료인
- **설명**: 모달을 통해 입력받은 환자 정보를 시스템에 등록합니다.
- **Request Headers**:
  - `Content-Type: application/json`
- **Request Body**:
  ```json
  {
    "name": "홍길동",
    "age": 35,
    "gender": "M",
    "phone": "010-1234-5678"
  }
  ```
  - `name` (String, 필수): 환자 이름
  - `age` (Integer, 필수): 환자 나이
  - `gender` (String, 필수): 성별 (`M` / `F`)
  - `phone` (String, 필수): 연락처 (휴대폰 번호)
- **Response (201 Created)**:
  ```json
  {
    "patientId": 1,
    "name": "홍길동",
    "age": 35,
    "gender": "M",
    "phone": "010-1234-5678",
    "createdAt": "2026-10-27T10:00:00Z"
  }
  ```

---

### 3.2. 환자 목록 조회 (REQ-PTNT-002)
- **HTTP Method & URL**: `GET /api/patients`
- **권한**: 로그인 된 사내 개발진, 의료 실무진, 연구진, 사내 의료인
- **설명**: 환자 목록을 조회하며, 이름 검색 및 성별/나이 범위 필터링을 제공합니다.
- **Query Parameters**:
  - `search` (String, 선택): 이름 기준 검색 키워드
  - `gender` (String, 선택): 성별 필터 (`M` / `F`)
  - `minAge` (Integer, 선택): 최소 나이 범위
  - `maxAge` (Integer, 선택): 최대 나이 범위
  - `page` (Integer, 선택, 기본값: `0`)
  - `size` (Integer, 선택, 기본값: `10`)
- **Response (200 OK)**:
  ```json
  {
    "content": [
      {
        "patientId": 1,
        "name": "홍길동",
        "age": 35,
        "gender": "M",
        "phone": "010-1234-5678",
        "createdAt": "2026-10-27T10:00:00Z",
        "updatedAt": "2026-10-27T10:00:00Z"
      }
    ],
    "page": 0,
    "size": 10,
    "totalElements": 1,
    "totalPages": 1
  }
  ```

---

### 3.3. 환자 정보 상세 조회 (REQ-PTNT-003)
- **HTTP Method & URL**: `GET /api/patients/{patientId}`
- **권한**: 로그인 된 사내 개발진, 의료 실무진, 연구진, 사내 의료인
- **설명**: 특정 환자의 상세 정보를 조회합니다.
- **Path Parameter**:
  - `patientId` (Long, 필수): 환자 고유 ID
- **Response (200 OK)**:
  ```json
  {
    "patientId": 1,
    "name": "홍길동",
    "age": 35,
    "gender": "M",
    "phone": "010-1234-5678",
    "createdAt": "2026-10-27T10:00:00Z",
    "updatedAt": "2026-10-27T10:00:00Z"
  }
  ```

---

### 3.4. 환자 정보 수정 (REQ-PTNT-004)
- **HTTP Method & URL**: `PUT /api/patients/{patientId}`
- **권한**: 로그인 된 사내 개발진, 의료 실무진, 연구진, 사내 의료인
- **설명**: 환자의 이름 및 연락처 정보를 수정합니다.
- **Path Parameter**:
  - `patientId` (Long, 필수): 환자 고유 ID
- **Request Body**:
  ```json
  {
    "name": "홍길동",
    "phone": "010-9876-5432"
  }
  ```
  - `name` (String, 필수): 수정할 이름
  - `phone` (String, 필수): 수정할 연락처
- **Response (200 OK)**:
  ```json
  {
    "patientId": 1,
    "name": "홍길동",
    "gender": "M",
    "phone": "010-9876-5432",
    "age": 35,
    "updatedAt": "2026-10-27T11:00:00Z"
  }
  ```

---

### 3.5. 환자 정보 삭제 (REQ-PTNT-005)
- **HTTP Method & URL**: `DELETE /api/patients/{patientId}`
- **권한**: 로그인 된 사내 개발진, 의료 실무진, 연구진, 사내 의료인
- **설명**: 환자 정보를 삭제합니다. 연관된 진료기록 및 X-Ray 이미지도 서버 로컬 저장소 및 DB에서 영구 삭제됩니다.
- **Path Parameter**:
  - `patientId` (Long, 필수): 환자 고유 ID
- **Response (204 No Content)**

---

## 4. 진료기록 관리 API 명세

### 4.1. 진료기록 등록 (REQ-MDR-001)
- **HTTP Method & URL**: `POST /api/patients/{patientId}/medical-records`
- **권한**: 사내 의료인
- **설명**: 환자의 진료 정보 및 흉부 X-Ray 이미지를 등록합니다. 이미지 파일은 서버 환경의 로컬 저장소에 저장됩니다.
- **Request Headers**:
  - `Content-Type: multipart/form-data`
- **Path Parameter**:
  - `patientId` (Long, 필수): 환자 고유 ID
- **Request Body (FormData)**:
  - `chartNumber` (String, 필수): 진료 차트 넘버 (예: "C-2026-001")
  - `symptoms` (String, 필수): 진료된 증상 내용
  - `xrayImage` (File, 필수): 흉부 X-ray 이미지 파일
- **Response (201 Created)**:
  ```json
  {
    "recordId": 101,
    "patientId": 1,
    "chartNumber": "C-2026-001",
    "symptoms": "기침 및 발열 증세",
    "xrayImageUrl": "/uploads/xray/20261027_101.jpg",
    "createdAt": "2026-10-27T12:00:00Z"
  }
  ```

---

### 4.2. 진료기록 목록 조회 (REQ-MDR-002)
- **HTTP Method & URL**: `GET /api/patients/{patientId}/medical-records`
- **권한**: 로그인 된 사내 개발진, 의료 실무진, 연구진, 사내 의료인
- **설명**: 특정 환자의 진료기록 목록을 확인합니다. 증상이 100자를 초과할 경우 `...`으로 생략 처리하여 반환합니다.
- **Path Parameter**:
  - `patientId` (Long, 필수): 환자 고유 ID
- **Response (200 OK)**:
  ```json
  [
    {
      "recordId": 101,
      "chartNumber": "C-2026-001",
      "symptoms": "기침 및 발열 증세...",
      "createdAt": "2026-10-27T12:00:00Z"
    }
  ]
  ```

---

### 4.3. 진료기록 상세 조회 (REQ-MDR-003)
- **HTTP Method & URL**: `GET /api/medical-records/{recordId}`
- **권한**: 로그인 된 사내 개발진, 의료 실무진, 연구진, 사내 의료인
- **설명**: 진료기록의 상세 내용과 저장된 흉부 X-Ray 이미지 경로를 조회합니다.
- **Path Parameter**:
  - `recordId` (Long, 필수): 진료 기록 ID
- **Response (200 OK)**:
  ```json
  {
    "recordId": 101,
    "chartNumber": "C-2026-001",
    "symptoms": "기침 및 발열 증세가 3일간 지속됨. 환자 호소에 따른 경과 관찰 필요.",
    "xrayImageUrl": "/uploads/xray/20261027_101.jpg",
    "createdAt": "2026-10-27T12:00:00Z"
  }
  ```