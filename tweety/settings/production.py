from base import *


SECRET_KEY = os.getenv("SECRET_KEY")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

DEBUG = False
TEMPLATE_DEBUG = False

WSGI_APPLICATION = 'tweety.wsgi_production.application'