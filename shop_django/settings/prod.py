from .common import *

# Nginx가 프록시 서버 역할을 하고있고, http://127.0.0.1:8000으로 리디렉션 하고있기에,
# 허용 API를 127.0.0.1로 설정함.
ALLOWED_HOSTS = ["127.0.0.1"]
CSRF_TRUSTED_ORIGINS = ["https://*.joje.link", "http://127.0.0.1:8000", "http://127.0.0.1"]
DEBUG = True

STATIC_ROOT = os.getenv("STATIC_ROOT")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shop_api_django',
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
    }
}
