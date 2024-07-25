from app import create_app

# Flask 애플리케이션을 생성합니다.
app = create_app()

# 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True)
