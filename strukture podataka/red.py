class FullQueueException(Exception):
    pass

class EmptyQueueException(Exception):
    pass

class Queue(object):
    def __init__(self, limit):
        self._data = []
        self._limit = limit
    def enqueue(self, value):
        if len(self._data)!=self._limit:
            self._data.append(value)
        else:
            raise FullQueueException("Red je pun!")
    def dequeue(self):
        if len(self._data)!=0:
             return self._data.pop(0)
        else:
            raise EmptyQueueException("Red je prazan!")
    def __len__ (self):
        return len(self._data)
    def is_empty(self):
        return len(self._data)==0
    def first(self):
        return self._data[0]

if __name__ == '__main__':
    queue = Queue(15)
    queue.enqueue(3)
    queue.enqueue(8)
    queue.enqueue(1)
    print(len(queue))
    print(queue.first())

    queue.dequeue()
    print(len(queue))

    print(queue.first())
    print(queue.is_empty())
