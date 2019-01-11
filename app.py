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
    jsonObect = request.get_json(silent=True, force=True)

    intent = getIntent(jsonObject)
    params = getParameter(jsonObect)

    if(intent == "defineTerm"):
        response = defineTerm(params, jsonObject)


    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def getParameter(jsonObject):
    return jsonObject['queryResult']['parameters']

def getIntent(jsonObject):
    return jsonObject['queryResult']['intent']['displayName']

def defineTerm(desired_term, jsonObject):
    print(desired_term)
    defs = jsonObject['terms']

    if desired_term in defs:
        return {
            "fulfillmentText:" data['terms'][desired_term]
        }
    else:
        return "fulfillmentText": "Sorry, I don't know that one"

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


def defineTerm(desired_term, jsonObject):
    print(desired_term)
    defs = jsonObject['terms']

    if desired_term in defs:
        return {
            "fulfillmentText:" data['terms'][desired_term]
        }
    else:
        return "fulfillmentText": "Sorry, I don't know that one"


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
