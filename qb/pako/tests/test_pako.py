from qb.pako import encode, decode


def test_encode():
    origin = '123456789'
    desired = '==gICUJDAIAVwe7M1EjNyQjMTxJe'

    assert encode(origin) == desired


def test_decode():
    origin = '==gICUJDAIAVwe7M1EjNyQjMTxJe'
    desired = '123456789'

    assert decode(origin) == desired
