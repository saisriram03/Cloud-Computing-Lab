from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

CATALOG_URL = os.getenv(
    "CATALOG_URL",
    "http://catalog-service:5000"
)


@app.route("/")
def home():
    return """
    <h1>Product Management Application</h1>
    <p>Frontend microservice is running.</p>
    <a href='/products'>View Products</a>
    """


@app.route("/products")
def products():
    try:
        response = requests.get(
            f"{CATALOG_URL}/products",
            timeout=5
        )
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as error:
        return jsonify({"error": str(error)}), 502


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
