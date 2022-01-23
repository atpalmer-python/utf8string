from utf8string import utf8


def test_len():
    result = utf8('hello, world')
    assert len(result) == 12


def test_subscript():
    assert utf8('hello')[1] == utf8('e')


def test_subscript_slice_empty():
    assert utf8('hello')[2:1] == utf8('')


def test_subscript_slice():
    assert utf8('hello')[1:4] == utf8('ell')


def test_subscript_slice_skip():
    assert utf8('hello, world')[1:-1:2] == utf8('el,wr')


def test_subscript_slice_skip_back():
    assert utf8('hello, world')[-1:3:-3] == utf8('do,')

