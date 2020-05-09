from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
limiter = Limiter(app, key_func=get_remote_address, default_limits=[])


@app.route("/", methods=["GET"])
@limiter.limit("30/minute")
def get_url_headers():
    url = request.args.get("url")
    if not url:
        return jsonify(error="URL Missing"), 400
    headers = dict(request.headers)
    response = requests.head(url, headers={"Origin": headers.get("Origin")})
    return jsonify(headers=dict(response.headers))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
