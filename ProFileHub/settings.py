"""
Django settings for ProFileHub project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


SECRET_KEY  = set


DEBUG = True

#ALLOWED_HOSTS = ['35.238.135.221', '127.0.0.1', 'localhost', '*']

ALLOWED_HOSTS = ['mydevportfolio-444617.uc.r.appspot.com']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'PortfolioApp',
    'crispy_forms',
    'crispy_bootstrap5',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',


]

CACHE_MIDDLEWARE_SECONDS = 0  # Disable cache
CACHE_MIDDLEWARE_KEY_PREFIX = 'dev_cache'

ROOT_URLCONF = 'ProFileHub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
         'DIRS': [BASE_DIR / 'PortfolioApp/templates'],
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

WSGI_APPLICATION = 'ProFileHub.wsgi.application'


# allow django to recocnnise my bootstarp 5 
CRISPY_ALLOWED_TEMPLATES_PACKS ="bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5",


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


try:
    from PortfolioApp.gitconfig.gitconfig import (
        set,  
        DNAME,
        DUSER,
        DPASSWORD,
        DHOST,
        DPORT,
    )
except ImportError:
    # Fallback to environment variables or default values if gitconfig.py is not found
    set = os.getenv('SECRET_KEY', 'default_secret_key')  # Use an environment variable for the secret key
    DNAME = os.getenv('DB_NAME', 'default_db_name')
    DUSER = os.getenv('DB_USER', 'default_user')
    DPASSWORD = os.getenv('DB_PASSWORD', 'default_password')
    DHOST = os.getenv('DB_HOST', 'localhost')
    DPORT = os.getenv('DB_PORT', '5432')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DNAME,
        'USER': DUSER,
        'PASSWORD': DPASSWORD,
        'HOST':DHOST,
        'PORT':DPORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "PortfolioApp/static"),  # Dynamically resolve the absolute path
]

# Define STATIC_ROOT for collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")



# Google Cloud Storage Configuration
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'cloudcv'

# Credentials File
GS_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Media Settings
MEDIA_URL = f'https://storage.googleapis.com/cloudcv/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

