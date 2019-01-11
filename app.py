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
    # Opens JSON database file
    with open('data.json') as file:
        jsonData = json.load(file)

    # Gets JSON request object
    jsonRequest = request.get_json(silent=True, force=True)

    intent = getIntent(jsonRequest)
    params = getParameter(jsonRequest)

    if(intent == "defineTerm"):
        response = defineTerm(params, jsonData)
    elif(inten == "loanCalculator")
        response = calculateInterest(params)


    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

# Gets entity of an intent
def getParameter(jsonObject):
    return jsonObject['queryResult']['parameters']

# Gets the intent
def getIntent(jsonObject):
    return jsonObject['queryResult']['intent']['displayName']

# Gets definition from data.json for desired_term if it is availible
def defineTerm(desired_term, jsonObject):
    print(desired_term)
    defs = jsonObject['terms']

    if desired_term in defs:
        return {
            "fulfillmentText:" data['terms'][desired_term]
        }
    else:
        return "fulfillmentText": "Sorry, I don't know that one"

# Calculates Interest from user given length, principle, interest
def calculateInterest(parameters):
    print(parameters)

    length = parameters["blah"]
    principle = parameters["blah"]
    interest = parameters["blah"]

    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
