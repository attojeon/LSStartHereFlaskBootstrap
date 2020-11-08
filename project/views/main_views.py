import functools

from datetime import datetime

from flask import (Flask, flash, redirect, render_template, request, Response, session, url_for, Blueprint, current_app)
from flask import send_file
from project.database import db

bp = Blueprint('main', __name__, url_prefix='/', template_folder='templates')

@bp.route('/')
def index():
    search_query = request.args.get('q')
    if search_query:
        flash('Comming Soon(곧 소개될 예정입니다...).', 'warning')
        return redirect(url_for('main.index'))
    else:
        pass

    return render_template( 'index.html' )


@bp.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@bp.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@bp.route('/post', methods=['GET'])
@bp.route('/post/<int:uid>', methods=['GET'])
def post(uid=1):  # 기본값 처리
    new_name = 'ATO-' + str(uid)
    print(new_name)
    return render_template('post.html', name_id=new_name)


@bp.route('/content/<uid>')
def content(uid):
    return f"수업내용({uid}): "

