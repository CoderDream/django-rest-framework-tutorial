"""
Django settings for tutorial project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p$@$+##=*#5$adf)7m212+&6!upiw8h2oj_=dmuvy#2gq8x2(x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'quickstart',
    'snippets',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tutorial.urls'

WSGI_APPLICATION = 'tutorial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

db_name = "django-tutorial"
name = "root"
pwd = "1234"
host = "127.0.0.1"
port = "3306"

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# from os import environ
# debug = not environ.get("APP_NAME", "")
# if debug:
#     # LOCAL
#     db_name = "django-tutorial"
#     name = "root"
#     pwd = "1234"
#     host = "127.0.0.1"
#     port = "3306"
# else:
#     # SAE
#     import sae.const
#     db_name = sae.const.MYSQL_DB
#     name = sae.const.MYSQL_USER
#     pwd = sae.const.MYSQL_PASS
#     host = sae.const.MYSQL_HOST
#     port = sae.const.MYSQL_PORT
#     host_s = sae.const.MYSQL_HOST_S

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': db_name,  # Or path to database file if using sqlite3.
        'USER': name,  # Not used with sqlite3.
        'PASSWORD': pwd,  # Not used with sqlite3.
        'HOST': host,  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': port,  # Set to empty string for default. Not used with sqlite3.
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
