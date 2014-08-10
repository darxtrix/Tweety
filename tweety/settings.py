"""
Django settings for tweety project.

"""
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(__file__)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tweety.urls'

WSGI_APPLICATION = 'tweety.wsgi.application'

# Database
# Do not need a database for this project
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


############### ROOTS' #################

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static_collection')
# After running the static collector the static files are collected here
# to be served under a nignix or any static file server 
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
#uploaded files reside here in the media root or other mime type files

#########################################


############### DIRS for static files and templates ###########

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'templates'),
    )

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
    )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

################################################################

###############  Twitter API Credentials #######################

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

################################################################

print "###############################"
print API_SECRET,API_KEY,SECRET_KEY
print "###############################"