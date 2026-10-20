# JavaScript DOM 조작법 및 Web API 정리

본 문서는 JavaScript를 활용한 웹 개발에서 필수적인 **Web API**와 **DOM 조작법**, 그리고 작업한 내용을 **Git/GitHub에 업로드하는 방법**을 정리한 가이드입니다.

---

## 1. Web API (Web Application Programming Interface)

### 1.1 Web API의 정의
- **Web API**는 웹 브라우저가 기본적으로 제공하는 자바스크립트용 인터페이스(함수, 객체, 이벤트 등) 모음입니다.
- 자바스크립트 언어 자체의 기능이 아닌, **브라우저 환경(Runtime Environment)**에서 제공하는 확장 기능입니다.
- 개발자는 Web API를 통해 브라우저 제어, 네트워크 요청, 데이터 저장, 그래픽 표현, 오디오/비디오 제어 등을 수행할 수 있습니다.

### 1.2 Web API의 예시
- **DOM API**: HTML 문서를 구조화하고 제어하는 인터페이스
- **Event API**: 사용자의 클릭, 키보드 입력, 마우스 이동 등 이벤트를 감지 및 처리하는 인터페이스
- **Timer API**: 일정 시간 후 또는 주기적으로 코드를 실행하는 인터페이스 (`setTimeout`, `setInterval`)
- **Storage API**: 브라우저 내에 데이터를 저장하는 인터페이스 (`localStorage`, `sessionStorage`)
- **Fetch API**: 서버와 비동기 네트워크 통신을 수행하는 인터페이스 (`fetch`)
- **Canvas / WebGL API**: 2D 및 3D 그래픽을 그리는 인터페이스
- **Geolocation API**: 사용자의 지리적 위치 정보를 가져오는 인터페이스

---

## 2. 주요 Web API 상세

### 2.1 DOM API (Document Object Model)
DOM은 HTML/XML 문서를 트리 구조의 객체(Object)로 표현하여 자바스크립트가 웹 페이지의 구조, 스타일, 내용 등을 동적으로 변경할 수 있게 해줍니다.

#### 주요 DOM 조작 메서드 및 속성
```javascript
// 1. 요소를 선택하는 DOM API
const title = document.getElementById('title');          // ID로 선택
const buttons = document.querySelectorAll('.tab-btn');   // CSS 선택자로 여러 개 선택

// 2. 요소 내용 변경
title.textContent = '실시간 암호화폐 가격 변동 추적기';     // 텍스트 변경
title.innerHTML = '<span>실시간</span> 암호화폐 추적기';   // HTML 포함 변경

// 3. 요소 생성 및 삭제
const newRow = document.createElement('tr');              // 새 요소 생성
document.querySelector('tbody').appendChild(newRow);     // 부모 요소에 추가
newRow.remove();                                         // 요소 삭제

// 4. 클래스(Class) 제어
title.classList.add('active');                           // 클래스 추가
title.classList.remove('active');                        // 클래스 제거
title.classList.toggle('active');                        // 클래스 토글
```

---

### 2.2 Event API
사용자의 동작(클릭, 입력, 스크롤 등)이나 브라우저의 상태 변화를 감지하고, 해당 이벤트가 발생했을 때 실행할 콜백 함수(이벤트 리스너)를 등록합니다.

#### 주요 이벤트 처리
```javascript
const btn = document.querySelector('#all-tab');
const input = document.querySelector('#search-input');

// 1. 클릭 이벤트
btn.addEventListener('click', (event) => {
  console.log('버튼이 클릭되었습니다.');
});

// 2. 입력 이벤트 (검색창)
input.addEventListener('input', (event) => {
  console.log('입력된 검색어:', event.target.value);
});

// 3. 페이지 로드 완료 이벤트
window.addEventListener('DOMContentLoaded', () => {
  console.log('DOM 트리가 완전히 로드되었습니다.');
});
```

---

### 2.3 Timer API
특정 시간이 지난 후에 코드를 실행하거나, 일정 시간 간격으로 코드를 반복 실행할 때 사용합니다.

#### 타이머 함수 사용법
```javascript
// 1. setTimeout: 일정 시간 후 1회 실행 (ms 단위)
const timeoutId = setTimeout(() => {
  console.log('3초 뒤에 실행됩니다.');
}, 3000);

// setTimeout 취소
clearTimeout(timeoutId);

// 2. setInterval: 일정 시간마다 반복 실행 (실시간 암호화폐 API 호출 시 사용)
const intervalId = setInterval(() => {
  console.log('1초마다 반복 실행됩니다.');
}, 1000);

// setInterval 취소
clearInterval(intervalId);
```

---

### 2.4 Storage API
클라이언트(브라우저)에 데이터를 `Key-Value` 쌍의 문자열 형태로 저장할 수 있는 스토리지입니다.

- **LocalStorage**: 브라우저를 닫았다 열어도 데이터가 영구적으로 보관됨 (관심 항목 저장용).
- **SessionStorage**: 탭 또는 브라우저 창을 닫으면 데이터가 삭제됨.

#### LocalStorage 활용법
```javascript
// 1. 데이터 저장 (JSON 문자열 형태로 저장)
const favorites = ['BTCUSDT', 'ETHUSDT'];
localStorage.setItem('favorites', JSON.stringify(favorites));

// 2. 데이터 가져오기 (문자열을 다시 객체/배열로 변환)
const savedFavorites = JSON.parse(localStorage.getItem('favorites')) || [];

// 3. 개별 데이터 삭제
localStorage.removeItem('favorites');

// 4. 전체 데이터 초기화
localStorage.clear();
```

---

### 2.5 Fetch API
서버에 네트워크 요청을 보내고 응답(Data)을 받아오는 비동기 통신 기술입니다. Promise 기반으로 동작하며, `async/await`와 함께 자주 사용됩니다.

#### Fetch API 활용 예시 (바이낸스 암호화폐 API)
```javascript
const API_URL = 'https://api.binance.com/api/v3/ticker/24hr';

// async/await 방식
async function fetchCryptoData() {
  try {
    // 1. GET 요청
    const response = await fetch(API_URL);
    
    // 2. 응답 성공 여부 확인
    if (!response.ok) {
      throw new Error(`HTTP 에러! 상태 코드: ${response.status}`);
    }

    // 3. JSON 변환
    const data = await response.json();
    console.log('가져온 데이터:', data);
  } catch (error) {
    console.error('데이터 요청 실패:', error);
  }
}

fetchCryptoData();
```

---