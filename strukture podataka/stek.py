class EmptyStackException(Exception):
    pass

class FullStackException(Exception):
    pass

class Stack(object):
    def __init__(self, limit):
        self._data = []
        self._limit = limit
    def push(self, value):
        if len(self._data) == self._limit:
            raise FullStackException("Stek je pun!")
        else:
            self._data.append(value)
    def pop(self):
        if self.is_empty == True:
            raise EmptyStackException("Stek je prazan!")
        else:
            self._data.pop()
    def top(self):
        if self.is_empty == True:
            raise EmptyStackException("Stek je prazan!")
        else:
            if len(self._data)==1:
                return self._data[0]
            return self._data[-1]
    def is_empty(self):
        if len(self._data) == 0:
            return True
        else:
            return False
    def __len__(self):
        return len(self._data)

if __name__ == "__main__":
    s = Stack()
    s.push(2)
    print(s.top())
    print(len(s))

    s.pop()
    print(s.is_empty())
