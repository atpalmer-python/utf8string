from utf8string import utf8


def test_iter():
    itor = iter(utf8('hello, world 🙂'))
    assert next(itor) == b'h'
    assert next(itor) == b'e'
    assert next(itor) == b'l'
    assert next(itor) == b'l'
    assert next(itor) == b'o'
    assert next(itor) == b','
    assert next(itor) == b' '
    assert next(itor) == b'w'
    assert next(itor) == b'o'
    assert next(itor) == b'r'
    assert next(itor) == b'l'
    assert next(itor) == b'd'
    assert next(itor) == b' '
    assert next(itor) == utf8('🙂')[0]
    assert next(itor) == utf8('🙂')[1]
    assert next(itor) == utf8('🙂')[2]
    assert next(itor) == utf8('🙂')[3]


def test_code_point_iter():
    itor = utf8('hello, world 🙂').code_point_iter()
    assert next(itor) == b'h'
    assert next(itor) == b'e'
    assert next(itor) == b'l'
    assert next(itor) == b'l'
    assert next(itor) == b'o'
    assert next(itor) == b','
    assert next(itor) == b' '
    assert next(itor) == b'w'
    assert next(itor) == b'o'
    assert next(itor) == b'r'
    assert next(itor) == b'l'
    assert next(itor) == b'd'
    assert next(itor) == b' '
    assert next(itor) == utf8('🙂')

