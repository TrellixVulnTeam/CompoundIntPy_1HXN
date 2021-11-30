from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

@app.route('/')
@app.route('/<path:path>')
async def index(request, path=None):
    return json({'hello': 'world'})

@app.post('/')
async def interest(request):
    data = request.json
    P = data['P']
    r = data['r']
    n = data['n']
    t = data['t']
    response = json({
        'Total': (P(1+r/n) ^ (n*t))
    })
    return response

if __name__ == '__main__':
    app.run(host='0,0,0,0', port=8000)
