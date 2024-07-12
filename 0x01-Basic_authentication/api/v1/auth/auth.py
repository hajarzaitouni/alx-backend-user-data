#!/usr/bin/env python3
""" Define auth module """

from flask import request
from typing import List, TypeVar


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
            if path == ex_path:
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
