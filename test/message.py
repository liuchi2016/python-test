import struct
#import binascii
import ctypes


class binarybase(object):
    def __init__(self):
        self.index = 0
        self._format = ''

    def size(self):
        return struct.Struct(self.format).size

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, value):
        if isinstance(value, str):
            self._format = value
        else:
            raise ValueError

    def __iter__(self):
        return self

    def next(self):
        if self.index == len(self._value):
            raise StopIteration
        else:
            self.index += 1
            return  self._value[self.index-1]


class frameheader(binarybase):
    def __init__(self, msg_id=0, operation=0, msg_type=0, message=''):
        super(frameheader, self).__init__()
        if message:
            self._value = [msg_id, operation, msg_type, len(message), message]
            self.format = 'iiii%ds' % len(message)
        else:
            self._value = [msg_id, operation, msg_type, 0]
            self.format = 'iiii'


def wrapptobinary(*args):
    fmt = 'i'
    result = ''
    length = 0
    for ar in args:
        length += ar.size()
    result = struct.pack('i', length)
    for ar in args:
        result += struct.pack('' + ar.format, *ar)
        fmt += ar.format
    return (fmt, result)


def test():
    header = frameheader(msg_id=1, message='hello world')
    (fmt, buf) = wrapptobinary(header)
    s = struct.Struct(fmt)
    print s.unpack_from(buf, 0)


if __name__ == '__main__':
    test()


