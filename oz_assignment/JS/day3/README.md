# 자바스크립트 DOM 및 이벤트 개념 정리

---

## 1. DOM(Document Object Model) 이란?
- **개념**: 브라우저가 HTML 문서를 읽어 들여 웹 페이지의 모든 요소(태그, 속성, 텍스트 등)를 트리 구조의 객체(Object)로 표현한 것입니다.
- **역할**: 자바스크립트를 사용해 HTML 요소의 내용, 스타일, 구조를 동적으로 조작(추가, 수정, 삭제)할 수 있도록 연결해 주는 인터페이스 역할을 합니다.

---

## 2. Selector(선택자)로 DOM 요소 가져오기
자바스크립트에서 HTML 요소를 선택해 제어하기 위해 다양한 선택자 메서드를 사용합니다.

```javascript
// 1. 단일 요소 가져오기 (가장 흔하게 사용)
const elementByQuery = document.querySelector('.button'); // CSS 선택자로 첫 번째 요소 선택
const elementById = document.getElementById('header');     // ID로 요소 선택

// 2. 다중 요소 가져오기 (배열과 유사한 NodeList/HTMLCollection 반환)
const elementsByQueryAll = document.querySelectorAll('.item'); // 해당 클래스를 가진 모든 요소
const elementsByClass = document.getElementsByClassName('item');
```

---

## 3. Event 란?
- **개념**: 웹 페이지에서 일어나는 모든 유저의 행동이나 브라우저의 상태 변화를 의미합니다.
- **예시**:
  - 마우스 클릭 (`click`)
  - 키보드 입력 (`keydown`, `keyup`)
  - 마우스 이동 (`mousemove`, `mouseover`)
  - 폼 제출 (`submit`)
  - 페이지 로딩 완료 (`DOMContentLoaded`, `load`)

---

## 4. EventListener(이벤트 리스너)

### 4-1. EventListener(이벤트 리스너) 란?
특정 DOM 요소에서 **특정 이벤트가 발생했을 때 실행할 함수(콜백 함수)를 등록하고 대기하는 감시자** 역할을 합니다.

### 4-2. EventListener(이벤트 리스너)를 사용하는 목적 / 이유
1. **HTML과 JS의 분리 (관심사 분리)**: HTML 태그 내에 `onclick="..."` 스타일로 직접 작성하는 대신, 자바스크립트 파일에서 깔끔하게 관리할 수 있습니다.
2. **다중 핸들러 등록 가능**: 하나의 요소에 동일한 이벤트에 대한 여러 개의 함수를 등록할 수 있습니다.
3. **이벤트 제어 용이**: 필요에 따라 이벤트를 동적으로 제거(`removeEventListener`)하거나 옵션을 지정할 수 있습니다.

### 4-3. EventListener(이벤트 리스너) 정의하기
```javascript
// 문법: target.addEventListener(type, listener);

const btn = document.querySelector('#myBtn');

// 기본 함수 정의를 통한 이벤트 리스너 등록
btn.addEventListener('click', function() {
    alert('버튼이 클릭되었습니다!');
});
```

### 4-4. EventListener(이벤트 리스너) 응용
```javascript
const inputField = document.querySelector('#username');
const displayArea = document.querySelector('#result');

// 입력할 때마다 실시간으로 텍스트 반영하기
inputField.addEventListener('input', (event) => {
    displayArea.textContent = event.target.value;
});
```

---

## 5. 마우스 감지 (Mouse Events)

### 5-1. 마우스 감지란?
사용자가 마우스를 움직이거나, 특정 요소 위에 올리거나, 이탈시키는 등의 동작을 이벤트를 통해 알아채는 기법입니다.

### 5-2. 마우스 감지 사용 예시
```javascript
const box = document.querySelector('.box');

// 마우스가 요소 위에 올라갔을 때
box.addEventListener('mouseenter', () => {
    box.style.backgroundColor = 'blue';
});

// 마우스가 요소를 벗어났을 때
box.addEventListener('mouseleave', () => {
    box.style.backgroundColor = 'gray';
});

// 마우스가 이동할 때의 좌표 감지
document.addEventListener('mousemove', (event) => {
    console.log(`현재 마우스 위치 - X: ${event.clientX}, Y: ${event.clientY}`);
});
```

---

## 6. 화살표 함수 (Arrow Function)

### 6-1. 화살표 함수란?
ES6(2015)에서 도입된 문법으로, `function` 키워드 대신 `=>` (화살표)를 사용하여 함수를 더 짧고 간결하게 작성할 수 있는 표기법입니다.

### 6-2. 화살표 함수 사용 예시
```javascript
// 1. 기존 일반 함수 방식
function addStandard(a, b) {
    return a + b;
}

// 2. 화살표 함수 기본 방식
const addArrow = (a, b) => {
    return a + b;
};

// 3. 실행문이 단 한 줄일 경우 중괄호({})와 return 생략 가능
const addShort = (a, b) => a + b;

// 4. 이벤트 리스너에서의 화살표 함수 사용
const button = document.querySelector('button');

button.addEventListener('click', () => {
    console.log('화살표 함수를 사용한 클릭 이벤트!');
});
```