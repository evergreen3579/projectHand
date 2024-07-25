from flask import Flask, render_template


# Flask 애플리케이션을 생성하는 함수
def create_app():
    app = Flask(__name__)

    # 루트 URL('/')에 접근하면 index.html을 렌더링하는 뷰 함수를 정의합니다.
    @app.route('/')
    def index():
        return render_template('index.html')
    

    return app
