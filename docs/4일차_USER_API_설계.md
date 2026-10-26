# 4일차 - User API 설계 명세서

## 1. 개요
본 문서는 흉부 X-Ray AI 진단 서비스의 사용자(User) 관련 기능 및 비기능 요구사항을 바탕으로 작성된 RESTful API 명세서입니다.

---

## 2. 공통 정의 및 비기능 요구사항 (NFR)

### 2.1 인증 및 인가 (NFR-USER-001)
* **JWT (Json Web Token) 구조**:
  * **Access Token**: 만료 시간 30분. Authorization Header (`Bearer <Token>`)로 전달.
  * **Refresh Token**: 만료 시간 7일. Client 접근 불가 쿠키(`HttpOnly`, `Secure`, `SameSite=Strict`)로 전달.
  * **Payload**: 최소 식별 정보인 `user_id`만 포함.
* **토큰 재발급 흐름**:
  * Access Token 만료 시, HttpOnly 쿠키의 Refresh Token을 검증하여 새로운 Access Token 재발급.
  * Refresh Token 만료 시, HTTP `401 Unauthorized` 응답을 반환하여 재로그인 유도.

### 2.2 공통 응답 포맷 및 성능 (NFR-USER-003)
* 모든 API 응답 시간은 최대 3초 이내 처리를 목표로 합니다.
* **성공 응답 구조**:
  ```json
  {
    "success": true,
    "message": "성공 메시지",
    "data": { ... }
  }

  에러 응답 구조:
  {
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "상세 에러 메시지"
  }

3. 권한 체계 (Role)
PENDING (대기자): 마이페이지 외 모든 서비스 접근 불가

STAFF (스태프): 내부 직원, 흉부 X-ray 관련 모든 읽기/쓰기/수정 작업 가능

ADMIN (어드민): 시스템 관리자, 모든 항목에 대한 데이터 액세스 및 회원 관리 가능

Domain,Method,Endpoint,Description,Permission
Auth,POST,/api/v1/auth/signup,회원가입,Public
Auth,POST,/api/v1/auth/login,로그인 및 토큰 발급,Public
Auth,POST,/api/v1/auth/logout,로그아웃 (토큰/쿠키 만료),Authenticated
Auth,POST,/api/v1/auth/refresh,Access Token 재발급,Public (Refresh Token)
User,GET,/api/v1/users/me,마이페이지 본인 정보 조회,Authenticated
User,PATCH,/api/v1/users/me,회원 정보 수정 (Partial),Authenticated
User,PATCH,/api/v1/users/me/password,비밀번호 변경,Authenticated
User,DELETE,/api/v1/users/me,회원 탈퇴 (Hard Delete),Authenticated
Admin,GET,/api/v1/admin/users,전체 회원 목록 조회 (검색/필터),ADMIN
Admin,PATCH,/api/v1/admin/users/{user_id}/role,회원 권한 변경,ADMIN

5. API 상세 명세
5.1 회원가입 (REQ-USER-001)
Endpoint: POST /api/v1/auth/signup

Access: Public

Request Body:
{
  "email": "user@hospital.com",
  "password": "Password123!",
  "name": "홍길동",
  "department": "MEDICAL",
  "gender": "M",
  "phone_number": "010-1234-5678"
}

Response (201 Created):
{
  "success": true,
  "message": "회원가입이 성공적으로 완료되었습니다.",
  "data": {
    "user_id": 1,
    "email": "user@hospital.com",
    "name": "홍길동",
    "role": "PENDING",
    "created_at": "2026-10-26T15:30:00Z"
  }
}

5.2 로그인 (REQ-USER-002, NFR-USER-001)
Endpoint: POST /api/v1/auth/login

Access: Public

Request Body:
{
  "email": "user@hospital.com",
  "password": "Password123!"
}


Response Header:

Set-Cookie: refresh_token=<JWT_REFRESH_TOKEN>; HttpOnly; Secure; SameSite=Strict; Max-Age=604800; Path=/

Response Body (200 OK):
{
  "success": true,
  "message": "로그인 성공",
  "data": {
    "access_token": "eyJhbGciOi...",
    "token_type": "Bearer",
    "expires_in": 1800
  }
}

5.3 로그아웃 (REQ-USER-003)
Endpoint: POST /api/v1/auth/logout

Access: Authenticated

Response Header:

Set-Cookie: refresh_token=; HttpOnly; Max-Age=0; Path=/

Response Body (200 OK):
{
  "success": true,
  "message": "로그아웃 되었습니다."
}

5.4 토큰 재발급 (NFR-USER-001)
Endpoint: POST /api/v1/auth/refresh

Access: Public (Cookie 내 refresh_token 전송)

Response Body (200 OK):
{
  "success": true,
  "message": "Access Token이 재발급되었습니다.",
  "data": {
    "access_token": "eyJhbGciOi...",
    "token_type": "Bearer",
    "expires_in": 1800
  }
}

5.5 마이페이지 조회 (REQ-USER-006)
Endpoint: GET /api/v1/users/me

Access: Authenticated

Response Body (200 OK):
{
  "success": true,
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

5.6 회원 정보 수정 (REQ-USER-007)
Endpoint: PATCH /api/v1/users/me

Access: Authenticated

Description: 부서 및 휴대폰 번호에 대한 선택적(Partial) 수정

Request Body:
{
  "department": "RESEARCH",
  "phone_number": "010-9876-5432"
}

Response Body (200 OK):
{
  "success": true,
  "message": "회원 정보가 수정되었습니다.",
  "data": {
    "user_id": 1,
    "department": "RESEARCH",
    "phone_number": "010-9876-5432"
  }
}

5.7 비밀번호 변경 (REQ-USER-008)
Endpoint: PATCH /api/v1/users/me/password

Access: Authenticated

Request Body:
{
  "current_password": "Password123!",
  "new_password": "NewPassword456!"
}

Response Body (200 OK):
{
  "success": true,
  "message": "비밀번호가 성공적으로 변경되었습니다."
}

5.8 회원 탈퇴 (REQ-USER-009)
Endpoint: DELETE /api/v1/users/me

Access: Authenticated

Description: DB에서 회원 관련 모든 정보를 즉시 삭제 (Hard Delete)

Response Body (200 OK):
{
  "success": true,
  "message": "회원 탈퇴가 완료되어 모든 정보가 삭제되었습니다."
}

5.9 회원 목록 조회 (REQ-USER-004)
Endpoint: GET /api/v1/admin/users

Access: ADMIN

Query Parameters:

search: 이메일 또는 이름 검색어 (Optional)

department: 부서 필터 (RESEARCH, MEDICAL, DEVELOPMENT) (Optional)

page: 페이지 번호 (Default: 1)

size: 페이지당 결과 수 (Default: 10)

Response Body (200 OK):
{
  "success": true,
  "data": {
    "items": [
      {
        "user_id": 1,
        "email": "user@hospital.com",
        "name": "홍길동",
        "department": "MEDICAL",
        "gender": "M",
        "phone_number": "010-1234-5678",
        "role": "STAFF",
        "is_active": true
      }
    ],
    "total": 1,
    "page": 1,
    "size": 10
  }
}

5.10 회원 권한 변경 (REQ-USER-005)
Endpoint: PATCH /api/v1/admin/users/{user_id}/role

Access: ADMIN

Request Body:
{
  "role": "STAFF"
}

Response Body (200 OK):
{
  "success": true,
  "message": "회원 권한이 성공적으로 변경되었습니다.",
  "data": {
    "user_id": 1,
    "role": "STAFF"
  }
}
