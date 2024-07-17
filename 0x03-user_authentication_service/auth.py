#!/usr/bin/env python3
""" Define Hash_password method """

import bcrypt


def _hash_password(password: str) -> str:
    """ Hashes a password using bcrypt """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password
