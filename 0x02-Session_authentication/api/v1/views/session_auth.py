#!/usr/bin/env python3
""" Session authentication module for the API.
"""
from flask import request, jsonify, make_response
from api.v1.views import app_views
from models.user import User
import os


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login():
    """ Handle user login and create a session
    """
    from api.v1.app import auth

    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not email.strip():
        return jsonify({"error": "email missing"}), 400

    if not password or not password.strip():
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)

    user_json = user.to_json()

    response = make_response(jsonify(user_json))
    response.set_cookie(os.getenv("SESSION_NAME"), session_id)

    return response


@app_views.route(
        '/auth_session/logout', methods=['DELETE'], strict_slashes=False
)
def logout():
    """ Handles user logout by destroying session.
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
