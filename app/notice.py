from flask import Blueprint, render_template, request, redirect, url_for, current_app, send_from_directory
from db.connector import db, Notice
from werkzeug.utils import secure_filename
import os

# Blueprint 정의
notice_bp = Blueprint('notice_bp', __name__)

@notice_bp.route('/notice_write', methods=['GET', 'POST'])
def notice_write():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        title = request.form.get('title')
        content = request.form.get('content')

        file = request.files.get('file')  # 업로드된 파일 가져오기
        file_path = None

        if file:
            filename = secure_filename(file.filename)
            file_dir = os.path.join(current_app.root_path, 'static', 'uploads')  # 파일을 static/uploads 폴더에 저장
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)  # 폴더가 없으면 생성

            file_path = os.path.join('uploads', filename).replace("\\", "/")  # 경로 저장 및 슬래시 통일
            file.save(os.path.join(file_dir, filename))  # 파일을 실제 서버에 저장

        # 데이터베이스에 공지사항 정보 및 파일 경로 저장
        try:
            new_notice = Notice(user_id=user_id, title=title, content=content, file_path=file_path)
            db.session.add(new_notice)
            db.session.commit()
        except Exception as e:
            print(f"Error: {e}")
            db.session.rollback()

        return redirect(url_for('notice_bp.show_notice'))

    return render_template('notice_write.html')

@notice_bp.route('/notice')
def show_notice():
    posts = Notice.query.with_entities(Notice.id, Notice.user_id, Notice.title, Notice.writetime).all()
    return render_template('notice.html', posts=posts)

@notice_bp.route('/notice/<int:notice_id>', methods=['GET'])
def notice_detail(notice_id):
    notice = Notice.query.get_or_404(notice_id)
    return render_template('notice_detail.html', notice=notice)

@notice_bp.route('/delete_notice', methods=['POST'])
def delete_notice():
    notice_ids = request.form.getlist('notice_ids')
    if notice_ids:
        try:
            for notice_id in notice_ids:
                notice = Notice.query.get(notice_id)
                if notice:
                    db.session.delete(notice)
            db.session.commit()
        except Exception as e:
            print(f"Error during deletion: {e}")
            db.session.rollback()
    return redirect(url_for('notice_bp.show_notice'))

@notice_bp.route('/view_file/<filename>', methods=['GET'])
def view_file(filename):
    file_path = os.path.join('uploads', filename).replace("\\", "/")  # 파일 경로 생성 및 슬래시 통일
    return render_template('view_file.html', file_path=file_path)  # 파일 경로를 템플릿에 전달

@notice_bp.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    file_dir = os.path.join(current_app.root_path, 'static', 'uploads')  # 파일이 저장된 디렉토리
    return send_from_directory(file_dir, filename, as_attachment=True)  # 파일을 다운로드
