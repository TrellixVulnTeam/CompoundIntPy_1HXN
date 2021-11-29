from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

# Sanic application route that calculates: 
#   Compound interest for a given principal using a specified compound rate and number of years with monthly contributions.
#   Compound interest is calculated using the formula: 
#       Total = Compound interest for principal + Future value of a series.
#       Compound interest for principal = P(1+r/n)^(nt)
#       Future value of a series = PMT * {[(1 + r/n)(nt) - 1] / (r/n)} * (1+r/n)^nt * (1+r/n)
#       Total = [ P(1+r/n)^(nt) ] + [ PMT * (((1 + r/n)^(nt) - 1) / (r/n)) * (1+r/n)]
#   where 
#       total = the future value of the investment/loan, including interest
#       P = the principal investment amount(the initial deposit or loan amount)
#       Pmt = the monthly payment
#       r = the annual interest rate(decimal)
#       n = the number of times that interest is compounded per year, or variable t. 
#           (365 = daily, 96 = 4× month or weekly, 48 = 3× month, 24 = 2× month, 12 = monthly, 4 = quarterly, etc.)
#       t = the time(in years representing how many months, years, etc) the money is invested or borrowed for
#
# The values are received through sanic app.route /calculate endpoint as JSON key values 
# and the result is returned in the same manner as a JSON object when the calculation is complete.
@app.post('/contribution')
async def contribution_handler(request):
    data = request.json
    P = data['P']
    Pmt = data['PMT']
    r = data['r']
    n = data['n']
    t = data['t']
    total = (P(1+r/n) ^ (n*t)) + (Pmt * (((1 + r/n) ^ (n*t) - 1) / (r/n)) * (1+r/n))
    diff = total - P
    pMonth = diff / n
    response = json({
        'Total': total,
        'Contributions p/Month': pMonth,
        'Difference': diff
    })
    return response

# This endpoint calculates the compound interest. 
# Formula is : interest = P(1+r/n)^(n*t)
@app.post('/interest')
async def interest_handler(request):
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
    app.run(host='0.0.0.0', port=8000)
