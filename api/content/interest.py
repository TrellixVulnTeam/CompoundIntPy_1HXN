from sanic.response import json
from sanic import Blueprint

interestbp = Blueprint('interest_blueprint', url_prefix='/interest')


@interestbp.route('/')
async def contribp_root(request):
    return json({'my': 'blueprint'})
