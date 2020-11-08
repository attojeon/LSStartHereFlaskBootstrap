'''
Jinja2 : Flask 내장 Template 엔진
{{ ... }} : 변수나 표현식
{% ... %} : if나 for같은 제어문
{# ... #} : 주석
'''

from project import create_app

###################################################################
# 아래 주의 해야 함.
# 개발환경(flask 또는 python명령을 사용할 때): if 구문이 수행되고,
# 서비스환경(gunicorn으로 wsgi 서비스 수행할 때): else 구문이 수행된다.
#
# (venv)$ sudo apt-get install libmysqlclient-dev가 수행되지 않으면 gunicorn에서 알 수 없는 에러가 자꾸 발생함.
# 이유는 모름. 그런데 연관성이 없을 것 같은 에러가 발생함.
###################################################################
if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=9000)
else:
    app = create_app()


