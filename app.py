import os

from flask import Flask, request, jsonify
from db import get_conn

app = Flask(__name__)

@app.route("/")
def home():
    return "server is running"

@app.route("/health")
def health():
    rerun {"status": "ok"}
    return "ok"
if __name__ == "__main__":
    app.run(host="0.0.0.0",
    port=int(os.environ.get("PORT", 1000)))