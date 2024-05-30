import re
from typing import List
"""
This module provides a function to filter and obfuscate specified fields in
log messages. It replaces the values of specified fields with a
redaction string using regular expressions.
"""


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (list of str): The list of field names to be obfuscated.
        redaction (str): The string to replace the field values with.
        message (str): The log message containing fields to be obfuscated.
        separator (str): The character that separates fields in the log message

    Returns:
        str: The log message with specified field values obfuscated.
    """
    pattern = f"({'|'.join(fields)})=([^{separator}]+)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
