import pytest
from utf8string import utf8


COUNT = 28


@pytest.fixture
def timer():
    import time
    def timefunc(func, *args, **kwargs):
        tik = time.perf_counter()
        func(*args, **kwargs)
        tok = time.perf_counter()
        return tok - tik
    return timefunc


def test_concat(timer):
    def run_concat(cls):
        s = cls('abc 🙂')
        for _ in range(COUNT):
            s += s

    results = {
        cls: timer(run_concat, cls)
        for cls in (utf8, str)
    }
    assert results[utf8] < results[str]
    
