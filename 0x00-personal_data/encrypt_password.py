#!/usr/bin/env python3
"""
    Import bcrypt and encryption password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Expects one string argument name password and returns
       a salted, hashed password, which is a byte string.

    Args:
        password (str): password

    Returns:
        bytes: Encrypted password
    """
    if password:
        return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates password

    Args:
        hashed_password (bytes): Hashed password
        password (str): Password

    Returns:
        bool: true or false
    """
    if hashed_password and password:
        return bcrypt.checkpw(str.encode(password), hashed_password)