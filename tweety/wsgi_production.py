import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tweety.settings.product")

application = get_wsgi_application()
application = Cling(get_wsgi_application())
