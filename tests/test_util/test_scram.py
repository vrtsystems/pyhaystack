#!/usr/bin/env python
# vim: set sw=4 ts=4 et tw=78:


"""
SCRAM utility library tests.
"""

from pyhaystack.util import scram

# Unsigned integer to binary conversion

def test_pack_be_uint_negative():
    """
    Test that pack_be_uint rejects negative integers.
    """
    try:
        scram.pack_be_uint(-1)
        assert False, 'Negative numbers worked when they shouldn\'t'
    except ValueError:
        pass


def test_pack_be_uint_16bit():
    """
    Test that pack_be_uint can pack a small 16-bit number correctly.
    """
    assert scram.pack_be_uint(0x1234) == b'\x12\x34'


def test_pack_be_uint_128bit():
    """
    Test that pack_be_uint can pack a large 128-bit number correctly.
    """
    assert scram.pack_be_uint(0x1234567890abcdef0011223344556677) \
            == b'\x12\x34\x56\x78\x90\xab\xcd\xef' \
               b'\x00\x11\x22\x33\x44\x55\x66\x77'

# Binary to unsigned integer conversion

def test_unpack_be_uint():
    """
    Test the conversion of an arbitrary string to an unsigned integer.
    """
    assert scram.unpack_be_uint(b'Testing 1 2 3 4') \
            == 0x54657374696e672031203220332034
