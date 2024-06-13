#!/usr/bin/env python3
""" set up Flask application with a single route that returns a JSON payload.
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def welcome_message():
    """Return a JSON response with a welcome message."""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
