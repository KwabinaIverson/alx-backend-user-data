#!/usr/bin/env python3
"""A class to manage the API authentication."""

from flask import request
from typing import List, TypeVar


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
        # returns False - path and excluded_paths will be used later,
        # now, you don’t need to take care of them
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header.
        Arg:
            - request: Flask request object.
        Return:
            - String
        """
        # Return None for now
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user.
        Arg:
            - request: Flask request object.
        Return:
            - User object
        """
        # Return None for now
        return None
