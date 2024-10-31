from flask import Flask, render_template  # render_template를 Flask에서 임포트
from .views.maps import maps_bp  # 상대 경로로 블루프린트 가져오기
from .notice import notice_bp  # notice.py에서 블루프린트 가져오기
from db.connector import init_app  # 데이터베이스 초기화 함수 가져오기

# Flask 애플리케이션을 생성하는 함수
def create_app():
    app = Flask(__name__)

    # 데이터베이스 초기화
    init_app(app)

    # 형준 추가 파일 업로드 경로 설정 
    app.config['UPLOAD_FOLDER'] = 'static/uploads'

    # 형준 notice는 추가, 블루프린트 등록
    app.register_blueprint(maps_bp, name='maps_bp')  # 고유한 블루프린트 이름 'maps_bp' 지정
    app.register_blueprint(notice_bp, name='notice_bp')  # 고유한 블루프린트 이름 'notice_bp' 지정

    # 루트 URL('/')에 접근하면 index.html을 렌더링하는 뷰 함수를 정의합니다.
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/groupmeeting')
    def groupmeeting():
        return render_template('groupmeeting.html')

    @app.route('/maps')
    def maps():
        return render_template('maps.html')

    return app
