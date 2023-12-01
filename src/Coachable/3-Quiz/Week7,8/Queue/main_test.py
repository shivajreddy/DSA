from stencil import *


def test_queue_class():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.size() == 3
    assert q.get_items() == [1, 2, 3]

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.peek() == 1
    assert q.size() == 2

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.size() == 2
    assert q.get_items() == [2, 3]

    q = Queue()
    assert q.peek() is None
    assert q.dequeue() is None
    assert q.size() == 0
    assert q.get_items() == []
