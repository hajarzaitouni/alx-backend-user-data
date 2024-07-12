#!/usr/bin/env python3
""" Define auth module """

from flask import request
from typing import List, TypeVar


class Auth():
    """ create a class Auth """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Defines if the path requires authentication """
        return False

    def authorization_header(self, request=None) -> str:
        """ Returns the authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current User """
        return None
