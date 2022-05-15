from .common import *

# Nginx가 프록시 서버 역할을 하고있고, http://127.0.0.1:8000으로 리디렉션 하고있기에,
# 허용 API를 127.0.0.1로 설정함.
ALLOWED_HOSTS = ["127.0.0.1"]
DEBUG = False

# Todo: STATIC, MEDIA 서빙 설정
