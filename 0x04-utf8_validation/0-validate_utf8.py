#!/usr/bin/python3
"""Module for utf-8 validation.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing 1 byte of data each
    :return: True if data is a valid UTF-8 encoding, else return False
    """

    # Helper function to check if a number is a valid continuation byte
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    # Iterate through the data bytes
    i = 0
    while i < len(data):
        byte = data[i]

        # Check the number of leading 1s
        # to determine the length of the character
        if (byte & 0b10000000) == 0:  # 1-byte character
            pass
        elif (byte & 0b11100000) == 0b11000000:  # 2-byte character
            if i + 1 >= len(data) or not is_continuation(data[i + 1]):
                return False
            i += 1
        elif (byte & 0b11110000) == 0b11100000:  # 3-byte character
            if (i + 2 >= len(data) or
                    not is_continuation(data[i + 1]) or
                    not is_continuation(data[i + 2])):
                return False
            i += 2
        elif (byte & 0b11111000) == 0b11110000:  # 4-byte character
            if (i + 3 >= len(data) or
                    not is_continuation(data[i + 1]) or
                    not is_continuation(data[i + 2]) or
                    not is_continuation(data[i + 3])):
                return False
            i += 3
        else:
            return False  # Invalid leading byte

        i += 1

    return True
