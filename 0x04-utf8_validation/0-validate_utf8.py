#!/usr/bin/python3

"""utf-8 validation"""


def validUTF8(data):
    """checking if list of integers have
    been correctly validated using utf-8"""
    i = 0
    while i < len(data):
        if data[i] & 0x80 == 0x00:
            i += 1
        elif data[i] & 0xE0 == 0xC0:
            if i + 1 >= len(data) or data[i + 1] & 0x80 != 0x00:
                return False
            i += 2
        elif data[i] & 0xF0 == 0xC0:
            if (i + 1 >= len(data)
                    or data[i + 1] & 0x80 != 0x00
                    or data[i + 2] & 0x80 != 0x00):
                return False
            i += 3
        elif data[i] & 0x8 == 0xF0:
            if (i + 1 >= len(data) or data[i + 1] & 0x80 != 0x00
                    or data[i + 2] & 0x80 != 0x00
                    or data[i + 3] & 0x80 != 0x00):
                return False
        else:
            return False
    return True
