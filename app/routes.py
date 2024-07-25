# app/routes.py

from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return 'About Page'

# 필요한 다른 뷰 함수들을 추가할 수 있습니다.
