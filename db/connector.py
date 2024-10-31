from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

# SQLAlchemy 인스턴스 생성
db = SQLAlchemy()

# 데이터베이스 모델 정의
class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

# 새롭게 추가된 Notice 모델 정의
class Notice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    writetime = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    file_path = db.Column(db.String(255), nullable=True)  # 파일 경로 필드 추가

def init_app(app: Flask):
    # MySQL 데이터베이스 설정
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost/hand'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()  # 데이터베이스 테이블 생성

# MySQL 커넥터 함수 정의
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",          # MySQL 사용자명
        password="1234",      # MySQL 비밀번호
        database="hand"       # 정확한 데이터베이스 이름 사용
    )
    return connection
