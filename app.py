import os

from flask import Flask, request, jsonify
from db import get_conn

app = Flask(__name__)

@app.route("/")
def home():
    return "server is running"

@app.route("/get_customers", methods=["GET"])
def get_customers():
    try:
        conn = get_conn()
        cur = conn.cursor()

        cur.execute("SELECT * FROM customers")
        rows = cur.fetchall()

        customer_list = []
        for row in rows:
            customer_list.append({
                "id": row[0],
                "name": row[1],
                "mobile": row[2],
                "address": row[3]
            })

        cur.close()
        conn.close()

        return jsonify({
            "status": "success",
            "data": customer_list
        }), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 1000)))power