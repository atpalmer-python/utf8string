import pytest
from utf8string import utf8


def test_count():
    target = utf8('hello, world')
    assert target.count(utf8('l')) == 3


def test_count_start():
    target = utf8('hello, world')
    assert target.count(utf8('l'), 10) == 1


def test_count_end():
    target = utf8('hello, world')
    assert target.count(utf8('l'), 0, 4) == 2


def test_count_str_unicode():
    target = utf8('🙂 🙃 🙂 🙂 🙃 🙂 🙂')
    assert target.count('🙂') == 5


def test_find():
    target = utf8('hello')
    assert target.find('lo') == 3


def test_find_with_start():
    target = utf8('hello')
    assert target.find('lo', 3) == 3


def test_find_missing():
    target = utf8('hello')
    assert target.find('lo', 0, 4) == -1


def test_index():
    target = utf8('hello')
    assert target.index('lo') == 3


def test_index_with_start():
    target = utf8('hello')
    assert target.index('lo', 3) == 3


def test_index_missing():
    target = utf8('hello')
    with pytest.raises(ValueError):
        return target.index('lo', 0, 4)


def test_isalnum_True():
    target = utf8('hello123')
    assert target.isalnum() == True


def test_isalnum_False():
    target = utf8('hello_123')
    assert target.isalnum() == False


def test_isalpha_True():
    target = utf8('hello')
    assert target.isalpha() == True


def test_isalpha_False():
    target = utf8('hello123')
    assert target.isalpha() == False


def test_isdigit_True():
    target = utf8('123')
    assert target.isdigit() == True


def test_isdigit_False():
    target = utf8('123.4')
    assert target.isdigit() == False


def test_islower_numeric():
    target = utf8('123')
    assert target.islower() == False


def test_islower_alnum_lc():
    target = utf8('hello123')
    assert target.islower() == True


def test_islower_alnum_uc():
    target = utf8('Hello123')
    assert target.islower() == False


def test_isprintable_True():
    target = utf8('hello, world')
    assert target.isprintable() == True


def test_isprintable_False():
    target = utf8(b'hello, world\x01')
    assert target.isprintable() == False


def test_isspace_empty():
    target = utf8('')
    assert target.isspace() == False


def test_isspace_True():
    target = utf8('\t\n ')
    assert target.isspace() == True


def test_isspace_False():
    target = utf8('hello, world\n')
    assert target.isspace() == False


def test_isupper_numeric():
    target = utf8('123')
    assert target.isupper() == False


def test_isupper_alnum_uc():
    target = utf8('HELLO123')
    assert target.isupper() == True


def test_isupper_alnum_lc():
    target = utf8('HELLo123')
    assert target.isupper() == False


def test_join():
    sep = utf8(', ')
    items = [utf8('hello'), utf8('world')]
    assert sep.join(items) == utf8('hello, world')


def test_lower():
    target = utf8('HELLO123')
    assert target.lower() == utf8('hello123')


def test_rfind():
    target = utf8('hello')
    assert target.rfind('o') == 4


def test_rfind_empty():
    target = utf8('hello')
    assert target.rfind('') == 5


def test_rfind_with_start():
    target = utf8('hello')
    assert target.rfind('lo', 3) == 3


def test_rfind_missing():
    target = utf8('hello')
    assert target.rfind('lo', 0, 4) == -1


def test_rindex():
    target = utf8('hello')
    assert target.rindex('o') == 4


def test_rindex_empty():
    target = utf8('hello')
    assert target.rindex('') == 5


def test_rindex_with_start():
    target = utf8('hello')
    assert target.rindex('lo', 3) == 3


def test_rindex_missing():
    target = utf8('hello')
    with pytest.raises(ValueError):
        return target.rindex('lo', 0, 4)


def test_strip_noargs():
    target = utf8('\r\n\n\n\t  hello, world  \t\r\n\n  ')
    assert target.strip() == utf8('hello, world')


def test_strip_None():
    target = utf8('\r\n\n\n\t  hello, world  \t\r\n\n  ')
    target.strip(None) == utf8('hello, world')


def test_strip_arg():
    target = utf8('hello, world')
    assert target.strip('held') == utf8('o, wor')


def test_lstrip_arg():
    target = utf8('hello, world')
    assert target.lstrip('held') == utf8('o, world')


def test_rstrip_arg():
    target = utf8('hello, world')
    assert target.rstrip('held') == utf8('hello, wor')


def test_partition():
    target = utf8('hello, world')
    result = (utf8('hello'), utf8(', '), utf8('world'))
    assert target.partition(utf8(', ')) == result


def test_partition_sep_not_found():
    target = utf8('hello, world')
    result = (utf8('hello, world'), utf8(''), utf8(''))
    assert target.partition(utf8(': ')) == result


def test_rpartition():
    target = utf8('hello, world')
    result = (utf8('hello, wor'), utf8('l'), utf8('d'))
    assert target.rpartition(utf8('l')) == result


def test_rpartition_sep_not_found():
    target = utf8('hello, world')
    result = (utf8(''), utf8(''), utf8('hello, world'))
    assert target.rpartition(utf8(': ')) == result


def test_split():
    assert utf8('hello, world').split(utf8(', ')) == [utf8('hello'), utf8('world')]
    assert utf8('1,2,3').split(utf8(',')) == [
        utf8('1'), utf8('2'), utf8('3')]
    assert utf8('hello, world').split() == [utf8('hello,'), utf8('world')]
    assert utf8('hello\t \n  world').split() == [utf8('hello'), utf8('world')]
    assert utf8('1,2,3').split(utf8(','), maxsplit=1) == [
        utf8('1'), utf8('2,3')]
    assert utf8('1   2   3').split(maxsplit=1) == [
        utf8('1'), utf8('2   3')]


def test_rsplit():
    assert utf8('hello, world').rsplit(utf8(', ')) == [utf8('hello'), utf8('world')]
    assert utf8('1,2,3').rsplit(utf8(',')) == [
        utf8('1'), utf8('2'), utf8('3')]
    assert utf8('hello, world').rsplit() == [utf8('hello,'), utf8('world')]
    assert utf8('hello\t \n  world').rsplit() == [utf8('hello'), utf8('world')]
    assert utf8('1,2,3').rsplit(utf8(','), maxsplit=1) == [
        utf8('1,2'), utf8('3')]
    assert utf8('1   2   3').rsplit(maxsplit=1) == [
        utf8('1   2'), utf8('3')]


def test_startswith():
    target = utf8('hello, world')
    assert target.startswith('hello,') is True


def test_startswith_tuple():
    target = utf8('hello, world')
    assert target.startswith(('ell','o'), 1) is True


def test_startswith_not():
    target = utf8('hello, world')
    assert target.startswith('world') is False


def test_startswith_with_start():
    target = utf8('hello, world')
    assert target.startswith('world', 7) is True


def test_startswith_with_start_and_end():
    target = utf8('hello, world')
    assert target.startswith('wo', 7, 8) is False


def test_endswith():
    target = utf8('hello, world')
    assert target.endswith('world') is True


def test_endswith_tuple():
    target = utf8('hello, world')
    assert target.endswith(('w','o', 'r', 'l'), 0, -1) is True


def test_endswith_not():
    target = utf8('hello, world')
    assert target.endswith('hello') is False


def test_endswith_with_start():
    target = utf8('hello, world')
    assert target.endswith('world', 8) is False


def test_endswith_with_start_and_end():
    target = utf8('hello, world')
    assert target.endswith('wo', 7, 9) is True


def test_upper():
    target = utf8('hello123')
    assert target.upper() == utf8('HELLO123')


def test_swapcase():
    target = utf8('hElLo, WoRlD 123')
    assert target.swapcase() == utf8('HeLlO, wOrLd 123')

