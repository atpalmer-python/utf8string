from utf8string import utf8


def test_eq():
    a = utf8('hello')
    b = utf8('hello')
    assert a is not b
    assert a == b


def test_neq():
    assert utf8('hello') != utf8('world')


def test_ne():
    assert utf8('hello') != utf8('world')


def test_lt():
    assert utf8('a') < utf8('b')
    assert utf8('a') < utf8('aa')


def test_le():
    assert utf8('a') <= utf8('a')
    assert utf8('a') <= utf8('b')


def test_gt():
    assert utf8('b') > utf8('a')
    assert utf8('aa') > utf8('a')


def test_ge():
    assert utf8('a') >= utf8('a')
    assert utf8('b') >= utf8('a')

