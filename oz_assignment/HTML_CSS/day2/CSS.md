📚 CSS 핵심 개념 총정리 노트
1. CSS란 무엇인가?
CSS (Cascading Style Sheets)는 HTML 문서의 텍스트 색상, 글꼴, 레이아웃, 배경 등 시각적 디자인과 스타일을 정의하는 스타일 시트 언어입니다.

HTML이 웹페이지의 뼈대(구조)를 만든다면, CSS는 옷을 입히고 꾸미는 역할을 담당합니다.

2. CSS 적용 방식 3가지 (Inline, Internal, External)
① Inline CSS (인라인 스타일)
HTML 태그 내부에 style 속성을 사용하여 직접 작성하는 방식입니다.

특징: 특정 요소에만 빠르게 적용할 수 있지만, 유지보수가 어렵고 재사용성이 떨어져 실무에서는 거의 권장하지 않습니다.

예시: <p style="color: red; font-size: 16px;">안녕하세요</p>

② Internal CSS (내부 스타일 시트)
HTML 문서 안의 <head> 태그 내부에 <style> 태그를 열고 그 안에 CSS 코드를 작성하는 방식입니다.

특징: 하나의 HTML 파일 안에서 스타일을 관리할 수 있지만, 다른 HTML 파일과 스타일을 공유할 수 없습니다.

예시:

HTML
<head>
    <style>
        p { color: blue; }
    </style>
</head>
③ External CSS (외부 스타일 시트) — (가장 권장되는 표준 방식)
스타일 코드를 별도의 .css 파일(resume_style.css 등)로 분리하고, HTML 문서의 <head> 태그 안에서 <link> 태그로 연결하는 방식입니다.

특징: 여러 개의 HTML 페이지가 동일한 스타일 파일을 공유할 수 있어 유지보수와 관리가 매우 편리합니다.

예시:

HTML
<head>
    <link rel="stylesheet" href="resume_style.css">
</head>

3. CSS Selector (선택자)
스타일을 적용할 HTML 요소를 선택(지정)하는 규칙입니다.
전체 선택자 (*): 문서 내의 모든 요소를 선택합니다.

CSS
* { margin: 0; padding: 0; }
태그 선택자 (태그명): 특정 태그 이름을 가진 모든 요소를 선택합니다.

CSS
p { color: #333; }
아이디 선택자 (#아이디명): id 속성값을 가진 유일한 요소를 선택합니다 (문서 내에서 중복 불가).

CSS
#main-title { font-size: 28px; }
클래스 선택자 (.클래스명): class 속성값을 가진 여러 요소를 동시에 선택할 수 있습니다 (중복 사용 가능).

CSS
.highlight { background-color: yellow; }

4. style 속성
주로 Inline CSS에서 HTML 태그 내부에 직접 스타일 규칙을 부여할 때 사용하는 속성명입니다.
여러 스타일 속성을 작성할 때는 세미콜론(;)으로 구분합니다.

예시: <div style="width: 100px; height: 100px; background-color: tomato;"></div>

5. 텍스트 관련 속성
글자의 크기, 두께, 정렬 등을 조절할 때 사용하는 대표적인 속성들입니다.

font-size: 글자 크기 지정 (예: 16px, 1.2rem, 100%)
font-weight: 글자 두께 지정 (예: normal, bold, 숫자 400, 700)
text-align: 텍스트 정렬 방식 지정 (left, right, center, justify)

(참고) color: 글자 색상 지정 / line-height: 줄 간격 지정 / font-family: 글꼴 지정

6. 박스 모델 (Box Model)
웹페이지의 모든 요소는 사각형 박스로 둘러싸여 있으며, 안쪽부터 바깥쪽까지 다음과 같은 구조로 이루어져 있습니다.

content (콘텐츠): 텍스트나 이미지가 실제로 들어있는 영역 (width와 height로 크기 조절)
padding (패딩): 콘텐츠와 테두리 사이의 안쪽 여백
border (테두리): 콘텐츠와 패딩을 감싸는 선
margin (마진): 테두리 바깥쪽과 다른 요소 사이의 바깥쪽 여백
width / height: 요소의 가로 및 세로 크기 지정
box-sizing: 박스 크기를 계산하는 기준을 정하는 속성
content-box (기본값): width와 height가 오직 content 영역만 지정하므로, padding과 border가 더해져 전체 박스 크기가 커집니다.
border-box: width와 height에 padding과 border가 포함되므로 레이아웃 크기를 직관적으로 관리할 수 있어 실무에서 주로 선호됩니다.