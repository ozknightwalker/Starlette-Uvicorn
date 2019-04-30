from __future__ import unicode_literals

from starlette.applications import Starlette
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.routing import Router

import uvicorn

from App import settings, urls

app = Starlette()
urls.initialize_routes(app)
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_HOSTS)
app.add_middleware(
    GZipMiddleware, minimum_size=1000)
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY)

if __name__ == '__main__':
    uvicorn.run(
        app, debug=settings.DEBUG, host=settings.HOST, port=settings.PORT)
