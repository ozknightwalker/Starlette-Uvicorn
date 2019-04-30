from __future__ import unicode_literals

from starlette.responses import UJSONResponse


async def homepage(request):
    return UJSONResponse(dict(hello='world'))
