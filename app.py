import os
from urllib.parse import unquote, urlparse
from django.http import JsonResponse
from django.urls import path

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = __name__
INSTALLED_APPS = []
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
parsed = urlparse(os.environ['DATABASE_URL'])
DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql', 'NAME': unquote(parsed.path.lstrip('/')),
    'USER': unquote(parsed.username or ''), 'PASSWORD': unquote(parsed.password or ''), 'HOST': parsed.hostname,
    'PORT': parsed.port or 5432, 'CONN_MAX_AGE': 60}}

def index(request):
    return JsonResponse({'application': 'Django starter', 'message': 'Your application is ready.'})

def health(request):
    from django.db import connection
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
            ready = cursor.fetchone()[0] == 1
    except Exception:
        ready = False
    return JsonResponse({'ok': ready}, status=200 if ready else 503)

urlpatterns = [path('', index), path('health', health)]
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
