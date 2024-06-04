#!/usr/bin/env python3
"""
Module for API authentication management.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to determine if authentication is required
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Method to retrieve the authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method to retrieve the current user
        """
        return None
