from sanic.response import json
from sanic import Blueprint

futurevbp = Blueprint('futurev_blueprint', url_prefix='/futurev')


@futurevbp.route('/')
async def contribp_root(request):
    return json({'my': 'blueprint'})
