from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Milk Management API Running"

@app.route("/test")
def test():
    return {"message": "API working"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))