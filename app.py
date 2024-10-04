from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    return {
        "message": "success"
    }

