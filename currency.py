import os

from flask import Flask
from flask import request
from flask import jsonify

from converter import convert

app = Flask(__name__)


@app.route("/usd2rub")
def usd2rub():
    """Convert usd to rub"""
    try:
        value = float(request.args.get('value'))
    except (ValueError, TypeError):
        return jsonify({'error': 'wrong value type'})
    answer = convert(value)
    return jsonify({'result': answer})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv('LISTEN_PORT', 5000)), debug=True)
