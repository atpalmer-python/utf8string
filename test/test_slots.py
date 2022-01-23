from utf8string import utf8


def test_new_from_bytes():
    assert utf8(b'hello, world') == utf8('hello, world')


def test_new_from_int():
    assert utf8(1) == utf8('1')


def test_new_from_float():
    assert utf8(1.00) == utf8('1.0')


def test_new_from_utf8():
    assert utf8(utf8('hello, world')) == utf8('hello, world')


def test_str():
    result = utf8('hello, world')
    assert str(result) == 'hello, world'


def test_repr():
    assert repr(utf8('"hello" "world" 🙂')) == repr('"hello" "world" 🙂')


def test_hash():
    a = utf8('hello')
    b = utf8('hello')
    assert a is not b
    assert set((a, b)) == set((a,)) == set((b,))

