class EmptyDequeException(Exception):
    pass

class Deque(object):
    def __init__(self):
        self._data = []
    def __len__ (self):
        return len(self._data)
    def is_empty(self):
        return len(self._data)==0
    def first(self):
        if len(self._data)!=0:
            return self._data[0]
        else:
            raise EmptyDequeException("Dek je prazan!")
    def last(self):
        if len(self._data)!=0:
            return self._data[-1]
        else:
            raise EmptyDequeException("Dek je prazan!")
    def add_first(self, value):
        self._data.insert(0, value)
    def add_last(self, value):
        self._data.append(value)
    def delete_first(self):
        if len(self._data)!=0:
            self._data.pop(0)
        else:
            raise EmptyDequeException("Dek je prazan!")
    def delete_last(self):
        if len(self._data)!=0:
            self._data.pop(-1)
        else:
            raise EmptyDequeException("Dek je prazan!")

if __name__ == '__main__':
    d = Deque()
    d.add_last(5)
    d.add_first(7)
    d.add_first(3)
    print(d.first())

    d.delete_last()
    print(len(d))

    d.delete_last()
    d.delete_last()
    d.add_first(6)
    print(d.last())

    d.add_first(8)
    print(d.is_empty())
    print(d.last())
