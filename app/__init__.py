from flask import Flask, render_template
from .views.maps import maps_bp  # 상대 경로로 수정

# Flask 애플리케이션을 생성하는 함수
def create_app():
    app = Flask(__name__)


    # 블루프린트 등록
    app.register_blueprint(maps_bp)

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

