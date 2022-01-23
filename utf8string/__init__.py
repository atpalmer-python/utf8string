

class utf8(bytes):
    def __new__(cls, value):
        if isinstance(value, cls):
            return value
        if isinstance(value, str):
            value = value.encode('utf8')
        if not isinstance(value, bytes):
            return cls(str(value))
        return super().__new__(cls, value)

    @classmethod
    def _try_tuple_items(cls, value):
        if isinstance(value, tuple):
            return tuple(cls(x) for x in value)
        else:
            return cls(value)

    def __str__(self):
        return self.decode('utf8')

    def __repr__(self):
        return repr(str(self))

    def _code_point_len(self, index):
        '''Returns the length in bytes of a code point beginning with the given index.
        Raises IndexError if the specified index is not the beginning of a valid code point.'''
        def has_bits(headbyte, bits):
            return (headbyte & bits) == bits
        headbyte = super().__getitem__(index)
        # UTF-8 encoding uses the first byte of a sequence to indicate the total number of bytes
        if has_bits(headbyte, 0b11110000):
            return 4
        elif has_bits(headbyte, 0b11100000):
            return 3
        elif has_bits(headbyte, 0b11000000):
            return 2
        elif has_bits(headbyte, 0b10000000):
            # 0b10... indicates a 2nd, 3rd, or 4th byte of a multi-byte sequence
            raise IndexError(f"Byte '0x{headbyte:x}' does not begin a valid code point")
        else:
            # 0-bit indicates ASCII-compatible single-byte representation
            return 1

    def code_point(self, index):
        '''Returns the Unicode code point at the given index or raises IndexError'''
        return self.__class__(
            super().__getitem__(
                slice(index, index + self._code_point_len(index))))

    def code_point_iter(self):
        '''Iterator for Unicode code-points.
        Use __iter__ to iterate over bytes.'''
        i = 0
        while i < len(self):
            result = self.code_point(i)
            yield result
            i += len(result)

    def __iter__(self):
        yield from (self.__class__(chr(b)) for b in super().__iter__())

    def __contains__(self, value):
        value = self.__class__(value)
        return super().__contains__(value)

    def __getitem__(self, key):
        item = super().__getitem__(key)
        if isinstance(item, int):
            return self.__class__(chr(item))
        else:
            return self.__class__(item)

    def __add__(self, other):
        return self.__class__(super().__add__(other))

    def isprintable(self):
        return self.decode().isprintable()

    isprintable.__doc__ = str.isprintable.__doc__

    def startswith(self, prefix, *args, **kwargs):
        prefix = self._try_tuple_items(prefix)
        return super().startswith(prefix, *args, **kwargs)

    def endswith(self, prefix, *args, **kwargs):
        prefix = self._try_tuple_items(prefix)
        return super().endswith(prefix, *args, **kwargs)

    def count(self, sub, *args, **kwargs):
        return super().count(self.__class__(sub), *args, **kwargs)

    def find(self, sub, *args, **kwargs):
        return super().find(self.__class__(sub), *args, **kwargs)

    def rfind(self, sub, *args, **kwargs):
        return super().rfind(self.__class__(sub), *args, **kwargs)

    def index(self, sub, *args, **kwargs):
        return super().index(self.__class__(sub), *args, **kwargs)

    def rindex(self, sub, *args, **kwargs):
        return super().rindex(self.__class__(sub), *args, **kwargs)

    def strip(self, *args):
        args = (self.__class__(arg) for arg in args)
        return super().strip(*args)

    def lstrip(self, *args):
        args = (self.__class__(arg) for arg in args)
        return super().lstrip(*args)

    def rstrip(self, *args):
        args = (self.__class__(arg) for arg in args)
        return super().rstrip(*args)

