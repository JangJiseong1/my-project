function calculate(expression) {
    // 공백을 제거하고 숫자와 연산자(*, /, +, -) 단위로 토큰 분리
    const tokens = expression.match(/(\d+|\+|\-|\*|\/)/g);
    if (!tokens) return 0;

    let numbers = [];
    let operators = [];

    // 1단계: 우선순위가 높은 곱셈(*)과 나눗셈(/)을 먼저 처리
    for (let i = 0; i < tokens.length; i++) {
        let token = tokens[i];

        if (!isNaN(token)) {
            numbers.push(parseFloat(token));
        } else if (token === '*' || token === '/') {
            let prev = numbers.pop();
            let next = parseFloat(tokens[++i]);

            if (token === '*') {
                numbers.push(prev * next);
            } else {
                if (next === 0) throw new Error("0으로 나눌 수 없습니다.");
                numbers.push(prev / next);
            }
        } else {
            operators.push(token);
        }
    }

    // 2단계: 남은 덧셈(+)과 뺄셈(-)을 순서대로 처리
    let result = numbers[0];
    for (let i = 0; i < operators.length; i++) {
        let op = operators[i];
        let nextNum = numbers[i + 1];

        if (op === '+') {
            result += nextNum;
        } else if (op === '-') {
            result -= nextNum;
        }
    }

    return result;
}

// VS Code (Node.js) 환경에서 실행 테스트
console.log("결과 1:", calculate("3 + 5 * 2"));         // 13
console.log("결과 2:", calculate("10 - 4 / 2 + 3 * 5")); // 23