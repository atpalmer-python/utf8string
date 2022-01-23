import pytest
from utf8string import utf8


def test_len():
    result = utf8('hello, world')
    assert len(result) == 12


def test_concat():
    result = utf8('hello') + utf8(', ') + utf8('world')
    assert 'hello, world' == str(result)


def test_concat_TypeError():
    with pytest.raises(TypeError, match=r"^can't concat str to utf8$"):
        utf8('hello') + 'world'


def test_repeat_zero():
    result = utf8('hello') * 0
    assert result == utf8('')


def test_repeat_five():
    result = utf8('hello') * 5
    assert result == utf8('hellohellohellohellohello')


def test_item_IndexError_too_small():
    with pytest.raises(IndexError):
        result = utf8('hello')[-6]


def test_item_ok_neg():
    result = utf8('hello')[-5]
    assert isinstance(result, utf8)
    assert result == utf8('h')


def test_item_IndexError_too_big():
    with pytest.raises(IndexError):
        result = utf8('hello')[5]


def test_item_ok_pos():
    result = utf8('hello')[4]
    assert isinstance(result, utf8)
    assert result == utf8('o')


def test_contains_bytes_True():
    assert b'ell' in utf8('hello')


def test_contains_bytes_False():
    assert b'hello' not in utf8('world')


def test_contains_string_True():
    assert 'ell' in utf8('hello')


def test_contains_string_False():
    assert 'hello' not in utf8('world')

