/**
 * 🚀 JavaScript 핵심 문법 및 개념 총정리
 */

// ==========================================
// 1. 자료형 (Data Types)
// ==========================================
console.log("=== 1. 자료형 ===");
let num = 10;           // number (숫자)
let str = "Hello";      // string (문자열)
let isTrue = true;      // boolean (참/거짓)
let emptyVal = null;    // null (값이 없음을 명시적으로 표현)
let undefVal;           // undefined (값이 할당되지 않은 상태)

console.log(typeof num, typeof str, typeof isTrue, typeof emptyVal, typeof undefVal);


// ==========================================
// 2. 변수 선언 (Variable Declaration)
// ==========================================
console.log("\n=== 2. 변수 선언 ===");
let variableName = "재할당 가능";
variableName = "값 변경됨";

const constantName = "재할당 불가능 (상수)";
// constantName = "에러 발생"; // const는 값을 바꿀 수 없음


// ==========================================
// 3. 연산 방법 및 Math 내장 객체
// ==========================================
console.log("\n=== 3. 연산 방법 및 Math ===");
let a = 10, b = 3;
console.log(a + b); // 13 (더하기)
console.log(a - b); // 7  (빼기)
console.log(a * b); // 30 (곱하기)
console.log(a / b); // 3.3333333333333335 (나누기)
console.log(a % b); // 1  (나머지 연산)

// Math 내장 객체 활용
console.log(Math.abs(-5));    // 절대값: 5
console.log(Math.round(4.6)); // 반올림: 5
console.log(Math.floor(4.9)); // 버림: 4
console.log(Math.ceil(4.1));  // 올림: 5
console.log(Math.random());   // 0 이상 1 미만의 무작위 수


// ==========================================
// 4. 비교 연산 및 타입 확인 (typeof)
// ==========================================
console.log("\n=== 4. 비교 연산 및 타입 확인 ===");
console.log(5 > 3);   // true (대소 비교: <, >, <=, >=)
console.log(5 == "5");  // true (동등 연산자: 값만 비교, 타입은 자동 변환)
console.log(5 === "5"); // false (일치 연산자: 값과 타입 모두 비교 - 실무에서 권장)

console.log(typeof 123);     // "number"
console.log(typeof "hello"); // "string"


// ==========================================
// 5. 논리 연산
// ==========================================
console.log("\n=== 5. 논리 연산 ===");
console.log(true && false); // false (AND: 둘 다 참이어야 참)
console.log(true || false); // true  (OR: 둘 중 하나만 참이어도 참)
console.log(!true);         // false (NOT: 참/거짓 반전)


// ==========================================
// 6. 문자열 연산 및 Python과 차이점
// ==========================================
console.log("\n=== 6. 문자열 연산 ===");
let firstName = "John";
let lastName = "Doe";
console.log(firstName + " " + lastName); // 문자열 이어붙이기: "John Doe"

// 템플릿 리터럴 (백틱 ` 와 ${변수명} 활용)
let age = 25;
console.log(`제 이름은 ${firstName}이고 나이는 ${age}살입니다.`);

// [Python과 JavaScript의 number + string 연산 차이점]
// - Python: "5" + 3 을 하면 타입이 달라서 TypeError(에러)가 발생합니다.
// - JavaScript: 숫자를 자동으로 문자열로 바꿔서(묵시적 형변환) 이어붙여 버립니다.
console.log(5 + "3"); // 결과: "53" (문자열)


// ==========================================
// 7. 조건문 (if, else if, else)
// ==========================================
console.log("\n=== 7. 조건문 ===");
// 주의: Python에는 'elif'가 있지만, JavaScript는 'else if'를 사용합니다!
let score = 85;
if (score >= 90) {
    console.log("A 학점");
} else if (score >= 80) {
    console.log("B 학점");
} else {
    console.log("C 학점 미만");
}


// ==========================================
// 8. 반복문 (for, while)
// ==========================================
console.log("\n=== 8. 반복문 ===");
console.log("-- for 반복문 --");
for (let i = 0; i < 3; i++) {
    console.log(`for문 숫자: ${i}`);
}

console.log("-- while 반복문 --");
let count = 0;
while (count < 2) {
    console.log(`while문 카운트: ${count}`);
    count++;
}


// ==========================================
// 9. 배열 (Array) 사용법 및 활용
// ==========================================
console.log("\n=== 9. 배열 (Array) ===");
let fruits = ["사과", "바나나", "포도"];
console.log(fruits[0]);     // 첫 번째 요소 읽기: "사과"
console.log(fruits.length); // 배열의 길이: 3

fruits.push("딸기");        // 배열 맨 뒤에 요소 추가
console.log(fruits);

let lastFruit = fruits.pop(); // 배열 맨 뒤 요소 제거 후 반환
console.log(`제거된 과일: ${lastFruit}`);


// ==========================================
// 10. 객체 자료형 (Object)
// ==========================================
console.log("\n=== 10. 객체 (Object) ===");
// 객체 선언
let user = {
    name: "김철수",
    age: 30,
    isMarried: false
};

// 속성 읽기 (Dot notation / Bracket notation)
console.log(user.name);     // "김철수"
console.log(user["age"]);   // 30

// 속성 추가하기
user.job = "개발자";
console.log(user.job);      // "개발자"

// 속성 수정하기
user.age = 31;
console.log(user.age);      // 31

// 속성 제거하기
delete user.isMarried;
console.log(user.isMarried); // undefined (삭제됨)

// 속성이 객체에 존재하는지 확인하기 (in 연산자)
console.log("name" in user);   // true
console.log("height" in user); // false