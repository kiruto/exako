# -*- coding: utf-8 -*-
import functools
import config
import json
import binascii
from Crypto import Random
from Crypto.Cipher import AES


class Cryptor(object):

    from local_properties import AES_KEY
    # AES-256 key (32 bytes)
    KEY = AES_KEY
    BLOCK_SIZE = 16

    @classmethod
    def _pad_string(cls, in_string):
        """Pad an input string according to PKCS#7"""
        in_len = len(in_string)
        pad_size = cls.BLOCK_SIZE - (in_len % cls.BLOCK_SIZE)
        return in_string.ljust(in_len + pad_size, chr(pad_size))

    @classmethod
    def _unpad_string(cls, in_string):
        """Remove the PKCS#7 padding from a text string"""
        in_len = len(in_string)
        pad_size = ord(in_string[-1])
        if pad_size > cls.BLOCK_SIZE:
            raise ValueError('Input is not padded or padding is corrupt')
        return in_string[:in_len - pad_size]

    @classmethod
    def generate_iv(cls, size=16):
        return Random.get_random_bytes(size)

    @classmethod
    def encrypt(cls, in_string, in_key, in_iv=None):

        key = binascii.a2b_hex(in_key)

        if in_iv is None:
            iv = cls.generate_iv()
            in_iv = binascii.b2a_hex(iv)
        else:
            iv = binascii.a2b_hex(in_iv)

        aes = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
        return in_iv, aes.encrypt(cls._pad_string(in_string))

    @classmethod
    def decrypt(cls, in_encrypted, in_key, in_iv):

        key = binascii.a2b_hex(in_key)
        iv = binascii.a2b_hex(in_iv)
        aes = AES.new(key, AES.MODE_CFB, iv, segment_size=128)

        decrypted = aes.decrypt(binascii.a2b_base64(in_encrypted).rstrip())
        return cls._unpad_string(decrypted)


def aes_dict(function):
    """
    AES crypto by pycrypto 2.6.1
    https://pypi.python.org/pypi/pycrypto
    :param function:
    :return:
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if not config.ENCRYPT:
            return result
        try:
            from local_properties import AES_KEY
        except:
            return result
        data = json.dumps(result)
        iv, encrypted = Cryptor.encrypt(data, Cryptor.KEY)
        iv = iv.decode('utf-8')
        return iv[16:32] + binascii.b2a_base64(encrypted).rstrip().decode('utf-8') + iv[0:16]
    return wrapper
