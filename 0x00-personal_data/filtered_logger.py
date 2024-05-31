#!/usr/bin/env python3
"""
This module provides a function to filter and obfuscate specified fields in
log messages. It replaces the values of specified fields with a
redaction string using regular expressions.
"""

import re
from typing import List
import logging


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    This class formats log messages and redacts sensitive information
    specified in the fields list.

    Attributes:
        REDACTION (str): The string used to redact sensitive information.
        FORMAT (str): The format of the log messages.
        SEPARATOR (str): Separator used to split the fields in the log message.
        fields (List[str]): List of fields to be redacted in the log messages.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initializes the RedactingFormatter with the specified fields to redact.

        Args:
            fields (List[str]): The list of field names to be redacted.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the log record and redacts specified sensitive fields.

        Args:
            record (logging.LogRecord): log record to be formatted and redacted

        Returns:
            str: The formatted and redacted log message.
        """
        original_message = super().format(record)
        redacted_message = filter_datum(
                self.fields, self.REDACTION, original_message, self.SEPARATOR
        )
        return redacted_message
