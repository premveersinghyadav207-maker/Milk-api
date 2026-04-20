from flask import Flask, request, jsonify
from db import get_conn

app = Flask(__name__)

@app.route("/")
def home():
    return "server is running"