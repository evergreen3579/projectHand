# db/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy 객체를 생성합니다.
db = SQLAlchemy()

# Flask 애플리케이션을 생성하는 함수
def create_app():
    app = Flask(__name__)

    # 데이터베이스 설정을 Flask 애플리케이션에 적용합니다.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/minr_pro1'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # SQLAlchemy 초기화
    db.init_app(app)

    # 블루프린트 등록
    from app.routes import main_bp  # 이 위치에서 import 해야 합니다.

    app.register_blueprint(main_bp)

    return app
