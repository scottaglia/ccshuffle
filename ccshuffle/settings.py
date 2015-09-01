"""
Django settings for ccshuffle project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys, traceback
import json
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Configuration file for the deployment. The default location is the file with the name 'ccshuffle.conf' in the
# base directory. If the environment variable 'CCSHUFFLE_CONF' is set, the value of the variable as path will be used.

CONF_FILE = os.environ['CCSHUFFLE_CONF'] if 'CCSHUFFLE_CONF' in os.environ else '%s/ccshuffle.conf' % BASE_DIR

# Development settings
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

try:
    with open(CONF_FILE, 'r', encoding='utf-8') as fp:
        conf = json.load(fp)
        # The secret key must be a large random value and it must be kept secret.
        SECRET_KEY = conf['SECRET_KEY']
        # True for development, False for production (the ALLOWED_HOSTs must be set then).
        DEBUG = conf['DEBUG'] if 'DEBUG' in conf else False
        if not DEBUG:
            # The hosts, which are allowed to use the service.
            ALLOWED_HOSTS = conf['ALLOWED_HOSTS']
            # The csrf cookie enforces to be transported over https.
            # https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-CSRF_COOKIE_SECURE
            CSRF_COOKIE_SECURE = conf['CSRF_COOKIE_SECURE'] if 'CSRF_COOKIE_SECURE' in conf else True
            # The session cookie enforces to be transported over https.
            # https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-SESSION_COOKIE_SECURE
            SESSION_COOKIE_SECURE = conf['SESSION_COOKIE_SECURE'] if 'SESSION_COOKIE_SECURE' in conf else True
        # Database
        # https://docs.djangoproject.com/en/1.8/ref/settings/#databases
        DATABASES = conf['DATABASES']
        # Jamendo Authentication
        # https://developer.jamendo.com/v3.0
        if 'JAMENDO_AUTH' in conf:
            JAMENDO_AUTH = conf['JAMENDO_AUTH']
            os.environ['JAMENDO_AUTH'] = JAMENDO_AUTH
        # Logging settings, which are optional.
        # https://docs.djangoproject.com/en/1.8/topics/logging/
        if 'LOGGING' in conf:
            LOGGING = conf['LOGGING']

except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback, limit=10, file=sys.stdout)
    print('The configuration file (%s) can\'t be loaded.' % CONF_FILE, file=sys.stderr)
    exit(1)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shuffle',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'ccshuffle.urls'

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

WSGI_APPLICATION = 'ccshuffle.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    'locale',
)

# Languages, which are supported by the service.
LANGUAGES = (
    ('de', _('German')),
    ('en', _('English')),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (BASE_DIR + "/static",)
