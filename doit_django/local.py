from .settings import *

DEBUG = True

ALLOWED_HOSTS = ['193.123.255.112', '127.0.0.1']

INTERNAL_IPS = ["127.0.0.1"]

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
