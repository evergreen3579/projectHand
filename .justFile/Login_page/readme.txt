________DB-TABLE-생성________
1. MINR_PRO1 데이터베이스 생성
CREATE DATABASE MINR_PRO1;

2. login 테이블 생성
login_id(int)
user_id(varchar)
user_pw(varchar)
user_name(varchar)

________로컬 서버 생성________
1. cmd 입력 - 설치
pip install flask mysql-connector-python

2. cmd 입력 - 이동
cd 프로젝트 경로

3. cmd 입력 - 실행
python app.py

4, cmd 확인 - 확인
예 : * Running on http://127.0.0.1:5000
확인 후 웹 브라우저로 접속