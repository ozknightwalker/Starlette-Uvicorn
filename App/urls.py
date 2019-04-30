from __future__ import unicode_literals

from starlette.routing import Route

from .views import homepage

routes = [
    Route('/', endpoint=homepage, methods=['GET']),
]


def initialize_routes(app):
    for route in routes:
        app.add_route(
            route.path, route.endpoint, methods=route.methods)
