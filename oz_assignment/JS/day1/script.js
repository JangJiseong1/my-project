// 1. 변수 선언과 출력
let userName = "장지성";
const courseName = "JavaScript Day 1";

console.log("=== 1. 변수 출력 ===");
console.log("수강생 이름:", userName);
console.log("수강 과정:", courseName);

// 2. 자료형 확인 (typeof)
console.log("\n=== 2. 자료형 확인 ===");
let score = 95;
let isCompleted = true;
let userMessage = "열공중입니다!";

console.log(typeof score, score);         // number 95
console.log(typeof isCompleted, isCompleted); // boolean true
console.log(typeof userMessage, userMessage); // string 열공중입니다!

// 3. 간단한 연산자 테스트
console.log("\n=== 3. 연산자 테스트 ===");
let x = 10;
let y = 3;
console.log("x + y =", x + y); // 13
console.log("x * y =", x * y); // 30
console.log("x === 10:", x === 10); // true