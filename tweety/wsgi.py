import os
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tweety.settings.production")

from dj_static import Cling # define this after setting the DJANGO_SETTINGS_MODULE environment variable
application = get_wsgi_application()
application = Cling(get_wsgi_application())
