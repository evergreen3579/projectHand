from flask import Flask, render_template, request, redirect, flash, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# 데이터베이스 연결
db = mysql.connector.connect(
    host="localhost",
    user="SQL 아이디",
    password="SQL 비밀번호",
    database="MINR_PRO1"
)

cursor = db.cursor()

# 테이블이 존재하는지 확인
cursor.execute("""
CREATE TABLE IF NOT EXISTS login (
    login_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(10) NOT NULL,
    user_pw VARCHAR(15) NOT NULL,
    user_name VARCHAR(50) NOT NULL
)
""")
db.commit()

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user_pw = request.form['user_pw']
        cursor.execute("SELECT * FROM login WHERE user_id=%s AND user_pw=%s", (user_id, user_pw))
        user = cursor.fetchone()
        if user:
            return redirect('/index')
        else:
            flash('로그인 실패! 아이디와 비밀번호를 확인해주세요.')
            return redirect('/login')
    return render_template('login.html')

@app.route('/membership', methods=['GET', 'POST'])
def membership():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user_pw = request.form['user_pw']
        user_name = request.form['user_name']
        cursor.execute("INSERT INTO login (user_id, user_pw, user_name) VALUES (%s, %s, %s)",
                       (user_id, user_pw, user_name))
        db.commit()
        flash('회원가입이 완료되었습니다')
        return redirect(url_for('login'))
    return render_template('membership.html')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
