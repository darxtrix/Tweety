from base import *
import sys

SECRET_KEY = os.getenv("SECRET_KEY")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

DEBUG = False
TEMPLATE_DEBUG = False

WSGI_APPLICATION = 'tweety.wsgi.application'

LOGGING = {
    'handlers': {
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'strm': sys.stdout
        },
        ...
    }
}