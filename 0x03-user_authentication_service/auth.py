#!/usr/bin/env python3
""" Provide function to securely hash passwords using bcrypt
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt.

    Args:
        password (str): The password string to hash.

    Returns:
        bytes: The hashed password.
    """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password
