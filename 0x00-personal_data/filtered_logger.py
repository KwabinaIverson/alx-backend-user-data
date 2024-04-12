#!/usr/bin/env python3
"""filter_datum returns the log message obfuscated"""
import logging
from typing import List
import re

logger = logging.getLogger(__name__)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    `filter_datum` function returns the log message obfuscated

    Args:
        fields (list): A list of strings representing all fields to obfuscate.
        redaction (string): A string representing by what the
        field will be obfuscated
        message (string): A string representing the log line
        separator (string): A string representing by which character
        is separating all fields in the log line
    """
    return re.sub(r"(\w+)=([a-zA-Z0-9@\.\-\(\)\ \:\^\<\>\~\$\%\@\?\!\/]*)",
                  lambda match: match.group(1) + "=" + redaction
                  if match.group(1) in fields else match.group(0), message)