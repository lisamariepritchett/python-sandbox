from data_structures import Stack, Queue

def test_stack_push():
    my_stack = Stack()
    assert my_stack.size() == 0
    my_stack.push(1)
    assert my_stack.size() == 1
    assert my_stack.peek() == 1
    my_stack.push(2)
    my_stack.push(3)
    assert my_stack.peek() == 3
    assert my_stack.size() == 3

def test_stack_pop():
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    assert my_stack.pop() == 2
    assert my_stack.size() == 1
    assert my_stack.pop() == 1
    assert my_stack.size() == 0
    assert my_stack.pop() == None

def test_queue_enqueue():
    my_queue = Queue()
    assert my_queue.size() == 0
    my_queue.enqueue(1)
    assert my_queue.size() == 1
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    assert my_queue.size() == 3

def test_queue_dequeue():
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    assert my_queue.dequeue() == 1
    assert my_queue.size() == 1
    assert my_queue.dequeue() == 2
    assert my_queue.size() == 0
    assert my_queue.dequeue() == None
