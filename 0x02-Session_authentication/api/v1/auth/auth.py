#!/usr/bin/env python3
""" Define auth module """

from flask import request
from typing import List, TypeVar
import os


class Auth():
    """ create a class Auth """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Defines if the path requires authentication """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        for ex_path in excluded_paths:
            if ex_path.endswith('*'):
                if path.startswith(ex_path[:-1]):
                    return False
            elif path == ex_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Returns the authorization header """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current User """
        return None

    def session_cookie(self, request=None):
        """ Returns a cookie value from a request. """
        if request is None:
            return None

        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
