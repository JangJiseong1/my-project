📚 Git & GitHub 핵심 총정리

1. 핵심 개념 및 용어 (Keywords)

Git과 GitHub

Git: 내 컴퓨터(로컬)에서 소스 코드의 버전을 관리해 주는 버전 관리 도구
GitHub: Git으로 관리하는 코드를 클라우드에 올려 공유하고 협업하는 웹 플랫폼

Repository (저장소)

프로젝트 파일과 변경 역사(History)가 모여 있는 공간 (로컬 저장소 / 원격 저장소)

Commit (커밋)

코드의 수정 사항을 저장소에 영구적으로 기록하는 세이브 포인트

Branch (브랜치)

기존 코드를 건드리지 않고 독립적으로 기능을 개발할 수 있는 나뭇가지(분기)
브랜치 전략 (Git Flow): main(최종 배포) / develop(개발 중심) / feature(기능 개발) / hotfix(긴급 수정) / release(배포 전 테스트)

Merge (병합) 방식

Fast-forward: 가지가 갈라진 후 기존 브랜치 변화가 없을 때 포인터만 앞으로 이동하는 병합
3-way merge: 양쪽 브랜치 모두 변경 사항이 있어 새로운 병합 커밋을 만드는 병합
Merge conflict (병합 충돌): 같은 파일의 같은 위치를 다르게 고쳤을 때 발생하며, 개발자가 직접 수정해서 해결해야 함

2. 필수 명령어 모음 (Commands)

🔹 기본 세팅 및 상태 확인
git config: 사용자 이름 및 이메일 등 환경 설정
git init: 현재 폴더를 Git 저장소로 초기화
git status: 현재 작업 디렉토리의 변경 상태 확인

🔹 코드 저장 흐름

git add <파일>: 커밋을 위해 변경된 파일을 임시 대기소(Staging Area)에 올림 (git add .은 전체)
git commit -m "메시지": 대기 중인 변경 사항을 저장소에 기록(세이브)
git push: 로컬 저장소의 커밋을 원격 저장소(GitHub)로 업로드
git pull: 원격 저장소의 최신 코드를 로컬로 다운로드 및 동기화

🔹 브랜치 관련

git branch: 브랜치 목록 확인
git branch <이름>: 새 브랜치 생성
git switch <이름> (또는 checkout): 지정한 브랜치로 이동

3. 주요 에러 해결 및 응용 (Troubleshooting)

error: remote origin already exists. (원격 저장소 중복 등록 에러)
원인: 이미 origin이라는 이름의 원격 저장소가 등록되어 있는데 다시 등록하려 할 때 발생

해결:

git remote -v: 현재 연결된 주소 확인
git remote set-url origin <새-주소>: 주소 변경
git remote remove origin: 연결 해제 후 다시 등록
GitHub에 올라간 기록 초기화 후 재적용 (강제 덮어쓰기)

로컬의 .git 폴더를 삭제하고 새로 시작한 뒤 강제로 푸시하는 방법:

Bash

rm -rf .git                    # Git 기록 삭제 (Windows는 rd /s /q .git)

git init                       # 다시 초기화

git add .

git commit -m           "초기 커밋"

git remote add origin           <GitHub-주소>

git branch -M main

git push -u origin main --force  # 원격 저장소를 내 코드로 강제 덮어쓰기

