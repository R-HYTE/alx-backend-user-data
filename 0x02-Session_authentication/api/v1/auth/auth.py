#!/usr/bin/env python3
"""
Module for API authentication management.
"""
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """ Manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to determine if authentication is required
        Returns:
        True:
            * If `path` is None.
            * If `excluded_paths` is None or empty.
            * If `path` doesn't match any path in `excluded_paths`.
        False:
            * If `path` matches any path in `excluded_paths` (case-sensitive).
        """
        if path is None or (not excluded_paths):
            return True

        if path[-1] == '/':
            path = path[:-1]

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/'):
                excluded_path = excluded_path[:-1]

            if fnmatch.fnmatch(path, excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method to retrieve the authorization header
        Args:
            request (flask.Request, optional): The Flask request object.
            Defaults to None.

        Returns:
            str: The value of the Authorization header or None if not found.
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to retrieve the current user
        """
        return None
