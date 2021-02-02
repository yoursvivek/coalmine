import os

from flask import Flask, request

__version__ = "0.1.0"

app = Flask(__name__)


@app.route("/")
def index():
    headers = dict(request.headers)
    headers.update(
        {
            "version": __version__,
            "canary": os.getenv("CANARY") is not None,
        }
    )
    return headers
