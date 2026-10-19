let isPowerOn = true; // 전원 상태 (기본 켜짐)
let currentInput = "0"; // 현재 화면에 입력 중인 수식

// 전원 ON/OFF 버튼
function togglePower() {
    const display = document.getElementById("display");
    isPowerOn = !isPowerOn;
    
    if (!isPowerOn) {
        currentInput = "";
        display.value = "";
    } else {
        currentInput = "0";
        display.value = "0";
    }
}

// C(Clear) 버튼 - 초기화
function clearDisplay() {
    if (!isPowerOn) return;
    currentInput = "0";
    document.getElementById("display").value = currentInput;
}

// 숫자 및 소수점(.) 버튼
function appendNumber(number) {
    if (!isPowerOn) return;
    const display = document.getElementById("display");

    // 처음에 "0"일 때 숫자를 누르면 "0"을 지우고 새 숫자로 대체
    if (currentInput === "0" && number !== ".") {
        currentInput = number;
    } else {
        currentInput += number;
    }
    display.value = currentInput;
}

// 연산자(+, -, *, /) 버튼
function appendOperator(operator) {
    if (!isPowerOn) return;
    const display = document.getElementById("display");
    
    currentInput += operator;
    display.value = currentInput;
}

// Enter(=) 버튼 - 계산 수행
function performCalculate() {
    if (!isPowerOn) return;
    const display = document.getElementById("display");
    
    try {
        // eval 함수를 이용해 문자열 수식을 계산
        let result = eval(currentInput);
        display.value = result;
        currentInput = result.toString(); // 계산된 결과 이어서 계산 가능하게 설정
    } catch (error) {
        display.value = "오류";
        currentInput = "0";
    }
}