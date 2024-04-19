#!/usr/bin/env python3
"""A class to manage the API authentication."""

from flask import request
from typing import List, TypeVar
from os import getenv



class Auth():
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Handles authentication.
        Args:
            - path (str): Path
            - excluded_paths: (List): Excluded paths
        Return:
            - Bool (True/False)
        """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        for ex_path in excluded_paths:
            if path[:ex_path.find('*')] in ex_path[:expath.find('*')]:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header.
        Arg:
            - request: Flask request object.
        Return:
            - String
        """
        if not request:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user.
        Arg:
            - request: Flask request object.
        Return:
            - User object
        """
        # Return None for now
        return None

    def session_cookie(self, request=None):
        """Return a cookie value from a request
        """
        if request:
            return request.cookies.get(getenv('SESSION_NAME'))
