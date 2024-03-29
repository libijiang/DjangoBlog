#coding:utf8
"""
Django settings for web_app project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sae.const
import info

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#sae

# 修改上传时文件在内存中可以存放的最大size为10m
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760
# sae的本地文件系统是只读的，修改django的file storage backend为Storage
DEFAULT_FILE_STORAGE = 'sae.ext.django.storage.backend.Storage'
# 使用blog这个bucket
STORAGE_BUCKET_NAME = 'blog'
# ref: https://docs.djangoproject.com/en/dev/topics/files/


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ["bijiang.sinaapp.com"]


# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'blog',
	'duoshuo',
	'DjangoUeditor',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'web_app.urls'

WSGI_APPLICATION = 'web_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if 'SERVER_SOFTWARE' in os.environ:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql',
			'NAME': sae.const.MYSQL_DB,
			'USER':sae.const.MYSQL_USER,
			'PASSWORD':sae.const.MYSQL_PASS,
			"HOST":sae.const.MYSQL_HOST,
			"PORT":sae.const.MYSQL_PORT,
		}
	}
else:  
	#local databases
	DATABASES={
		'default':{
			'ENGINE': 'django.db.backends.mysql',
			'NAME': 'web_app',
			'USER':USER,
			'PASSWORD':PASSWORD,
		}
	}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/


LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
MEDIA_ROOT= os.path.join(BASE_DIR,'storage')
MEDIA_URL= '/stor-stub/%s/' % STORAGE_BUCKET_NAME

STATIC_ROOT =os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'



