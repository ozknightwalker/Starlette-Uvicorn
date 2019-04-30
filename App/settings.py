from __future__ import unicode_literals

from starlette.config import Config
from starlette.datastructures import Secret

config = Config('.env')

DEBUG = config('DEBUG', cast=bool, default=False)
SECRET_KEY = config('SECRET_KEY', cast=Secret, default='local-secret')

HOST = config('HOST', cast=str, default='0.0.0.0')
PORT = config('PORT', cast=int, default=8081)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=list, default=['*'])
