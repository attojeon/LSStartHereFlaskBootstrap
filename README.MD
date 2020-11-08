# flask 웹앱을 만들 때 시작할 수 있는 템플릿
- 웹앱입니다.
- REST 서비스가 아닙니다.
- WSGI gunicorn + nginx Web Server + systemd 의 조합을 추천합니다.

### 사용법
- git clone 으로 전체 코드를 가져옵니다.

- folder 이름을 적절히 수정합니다. 
```{.bash}
$ mv  LSStartHereFlaskBoostrap MyNewProject
```

- 가상 환경을 설정한다.
```{.bash}
$ cd MyNewProject
$ python3.8 -m venv venv   
```

- 패키지 설치
```{.bash}
$ pip install -r requirements.txxt
```

- launch.json, settings.json 적절하게 수정
- F5 키로 디버그를 실행하면 됩니다. 

- 모든 코드 수정 후 gunicorn을 사용하여 WSGI + nginx + systemd 설정을 하면 웹앱 서비스 등록이 됩니다.

### 대체할 수 있는 block들
```{.python}
# css 추가 위치
{% block extra_head %}{% endblock %}            

# navbar에 메뉴 추가 위치
{% block extra_header %}{% endblock %}          

# search_bar 태그들 대체할 위치, 사용빈도 낮음. 사용시 주의 요망
{% block search_bar %}                          

# 사이트 탭의 제목 변경 위치, 기본사이트 제목을 변경할 경우에만 사용
{% block title %}

# 페이지의 제목 작성 위치
{% block content_title %}

# 페이지의 내용 작성 위치
{% block content %}

# 페이지의 자바스크립트 추가 위치
{% block extra_scripts %}
```

### database 사용하기
- 꼭 필요하지 않다면 파일 또는 json 파일을 사용하여 데이터 관리를 할 수 있습니다.
- db 설정은 database.py의 db_name, db_user, db_password를 수정합니다.
- orator 모듈을 기본적으로 사용합니다.