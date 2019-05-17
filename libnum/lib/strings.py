#-*- coding:utf-8 -*-
import codecs

def s2n(s):
    """
    String to number.
    """
    if not len(s):
        return 0
    return int(s.encode("utf-8").hex(), 16)


def n2s(n):
    """
    Number to string.
    """
    s = hex(n)[2:]
    if len(s) % 2 != 0:
        s = "0" + s
    return str(codecs.decode(s, 'hex'), 'utf-8')


def s2b(s):
    """
    String to binary.
    """
    ret = []
    for c in s:
        ret.append(bin(ord(c))[2:].zfill(8))
    return "".join(ret)


def b2s(b):
    """
    Binary to string.
    """
    ret = []
    b = b.zfill((len(b) + 7) // 8 * 8)
    for pos in range(0, len(b), 8):
        ret.append(chr(int(b[pos:pos + 8], 2)))
    return "".join(ret)
