import os

from flask import Flask, request, jsonify
from db import get_conn

app = Flask(__name__)

@app.route("/")
def home():
    return "Milk Managment API running"

@app.route("/test")
def test():
    rerun {"message": "API working"}

if __name__ == "__main__":
    app.run(host="0.0.0.0",
    port=int(os.environ.get("PORT", 10000)))