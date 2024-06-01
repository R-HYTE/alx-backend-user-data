#!/usr/bin/env python3
"""
This module provides a function to filter and obfuscate specified fields in
log messages. It replaces the values of specified fields with a
redaction string using regular expressions.
"""

import logging
import os
import mysql.connector
import re
from typing import List, Tuple

PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connects to the MySQL database using environment variables for credentials.

    Returns:
        mysql.connector.connection.MySQLConnection:
                Connection object to the database.
    """
    # Get database credentials from environment variables
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    # Connect to the database
    db = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )
    return db


def main():
    """
    Main function to retrieve all rows in the users table and display each row
    under a filtered format.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
            "SELECT name, email, phone, ssn, password, ip, last_login"
            ",user_agent FROM users;"
    )

    logger = get_logger()
    for row in cursor:
        log_record = (
                f"name={row[0]}; email={row[1]}; phone={row[2]}; "
                f"ssn={row{[3]}; password={row[4]}; ip={row[5]}; "
                f"last_login={row[6]}; user_agent={row[7]}"
        )
        log_entry = logging.LogRecord(
                name="user_data", level=logging.INFO, pathname="",
                lineno=0, msg=log_record, args=(), exc_info=None
        )
        logger.handle(log_entry)

    cursor.close()
    db.close()


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger named "user_data".

    The logger logs up to logging.INFO level and does not propagate messages
    to other loggers. It uses a StreamHandler with RedactingFormatter.

    Returns:
        logging.Logger: The configured logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=list(PII_FIELDS))
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


if __name__ == "__main__":
    main()
