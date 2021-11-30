from sanic.response import json
from sanic import Blueprint

contribp = Blueprint('contribution_blueprint', url_prefix='/contribution')

@contribp.route('/')
async def contribp_root(request):
    return json({'my': 'blueprint'})
