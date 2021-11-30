from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

@app.route('/')
@app.route('/<path:path>')
async def index(request, path=None):
    return json({'hello': 'world'})

# Future value of a series = PMT * {[(1 + r/n)(nt) - 1] / (r/n)} * (1+r/n)^nt * (1+r/n)
@app.post('/')
async def interest_handler(request):
  return json({
    'total': request.json['PMT'] * (((1 + request.json['r']/request.json['n'])*(request.json['n'] * request.json['n']) - 1) / ((request.json['r']/request.json['n'])) * (1 + request.json['r']/request.json['n'])**(request.json['n'] * request.json['t']) * (1 + request.json['r'] / request.json['n']))
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
