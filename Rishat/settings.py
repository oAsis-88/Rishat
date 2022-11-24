import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-b3k0#z$l57#5yp4++iw&)il0tengyoksabk&b)anuysv^zthf$'
STRIPE_PUBLISHABLE_KEY = 'pk_test_51M7CWsFhnuQnH2WSs5JDQmqsdbTNOSbZ93HqjX3qxi9DWGl4XM6Akk6Ypp0iYKmrqxhSmLbVMBVV0se0DlgXZdM000s50boPyR'
STRIPE_SECRET_KEY = 'sk_test_51M7CWsFhnuQnH2WSoY4k67VmJ0F6KGeHKrJm9b4I7qsjJSP4taTG994JHaN2nqhcMW6sIN5Rdq0oUQ3oEzSJPrw400aXz9spZw'
STRIPE_ENDPOINT_SECRET = 'whsec_7d1b6074d9028f494ac202a0d74e81de8490a263e3b7ad3154a1a8071795343a'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
INTERNAL_IPS = ['127.0.0.1', 'localhost']


INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bootstrap5',
    'debug_toolbar',  # Процесс отладки
    'PaySys.apps.PaysysConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'Rishat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Rishat.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Rishat/static'),
    os.path.join(BASE_DIR, 'PaySys/static'),
]

# Локально для тестирования

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
