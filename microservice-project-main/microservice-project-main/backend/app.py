from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)


@app.route("/products")
def products():
    return jsonify({
        "products": ["Laptop", "Mobile", "Keyboard"],
        "served_by": socket.gethostname()
    })


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
