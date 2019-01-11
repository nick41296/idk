from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)

    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(data):
    print(data)
    data = data['queryResult']['parameters']
    dataLength = data['duration'][0]['amount']
    dataPayments = data['unit-currency'][0]['amount']
    dataInt = data['percentage'][0]
    if type(dataInt) is str:
        dataInt = dataInt[0:len(dataInt)-1]
    total = dataPayments * dataLength * 1.1
    response = "ayy that would cost like "  + str(total)
    return {
        "fulfillmentText": response
    }




if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
