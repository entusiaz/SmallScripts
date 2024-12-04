#!/usr/bin/env python3
from flask import Flask, request, jsonify
from pprint import pprint

app = Flask(__name__)

@app.route("/webhooks/inbound-message", methods=['POST'])
def inbound_message():
    if request.is_json:
        data = request.get_json()
    	pprint(data)
    else:
        data = dict(request.form) or dict(request.args)
        pprint(data)

    return "200"

if __name__ == '__main__':
    app.run(host="" port=3000)