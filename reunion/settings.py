"""
Django settings for reunion project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

#I have installed django-crispy-forms and crispy-bootstrap5
#pip install django-crispy-forms

# pip install crispy-bootstrap5

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

#Good tutorial on gunicorn, nginx, and running site on Godaddy
# https://ybshankar010.medium.com/setting-up-your-django-website-with-gunicorn-nginx-and-godaddy-f53dfcec05df
#ecsrpvgqdjmyhpnb
from pathlib import Path
from . info import *   #for email confirmation
import os
from urllib.parse import urlparse
from django.core.management.utils import get_random_secret_key  #for secret key

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import os
from dotenv import load_dotenv
load_dotenv()

# Email conformation  See info.py
'''EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
#EMAIL_HOST_PASSWORD = 'ecsrpvgqdjmyhpnb'
#EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = EMAIL_PORT
######################################
'''
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ('reunionsitetester@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')             #evra lmic shaf keub
SECRET_KEY = "django-insecure-ko4e0kh-ti00p*-k@n^-@nst++965t7atbmmo)j!whwpr#6g5!"
SECRET_KEY = os.environ.get(SECRET_KEY,'')
#EMAIL_HOST_PASSWORD = 'Broth3rchoochoo!!'
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/


ALLOWED_HOSTS = ['localhost','127.0.0.1','192.241.151.142']


DEBUG = False




# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "authentication",
    "letter",
    "crispy_forms",
    "crispy_bootstrap5",
    "pollsapp",
    "events",
    "big_forum",
    "announcements",
    "gallery",
    "taggit",
    "tinymce",
    "ckeditor",
    "hitcount",
    ]

TAGGIT_CASE_INSENSITIVE = True

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "reunion.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "reunion.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

#DATABASES = {
#    "default": {
#        "ENGINE": "django.db.backends.sqlite3",
#        "NAME": BASE_DIR / "db.sqlite3",
#    }
#}


DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": 'newdb',
            "USER": 'hodges',
            "PASSWORD": 'Broth3r_choochoo',
            "HOST": 'localhost',
            "PORT": '',
        }
    }




# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

#

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR/'static'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/'media/photos'


#

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#from decouple import config

#STRIPE_PUBLIC_KEY = config('STRIPE_PUBLIC_KEY')
#STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY')
#STRIPE_WEBHOOK_SECRET= config('STRIPE_WEBHOOK_SECRET')



#BACKEND_DOMAIN = config("BACKEND_DOMAIN")
#PAYMENT_SUCCESS_URL = config("PAYMENT_SUCCESS_URL")
#PAYMENT_CANCEL_URL = config("PAYMENT_CANCEL_URL")


