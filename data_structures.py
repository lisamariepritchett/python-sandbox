class Node:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self.value)
    def update(self, value):
        self.value = value


class RootNode(Node):
    def __init__(self, value):
        super().__init__(value)


class Branch():
    def __init__(self, node1, node2):
        if not isinstance(node1, Node):
            node1 = Node(node1)
        if not isinstance(node2, Node):
            node2 = Node(node2)
        self.node1 = node1
        self.node2 = node2
        self.branch = (node1, node2)


class Tree:
    def __init__(self, root:RootNode):
        self.root = root
        self.branches = []

    def add_branch(self, branch:Branch):
        self.branches.append(branch)

    @property
    def nodes(self):
        nodes = set()
        for branch in self.branches:
            nodes.add(branch.node1)
            nodes.add(branch.node2)
        return nodes

def test__tree_and_node():
    # TODO::
        # level of node: distance from root
        # parent of node: a connected node that is of lower level
        # children of node: a connected node that is of higher level
        # siblings of nod; a connected node that is of the same level or that shares a parent
        # degree of node: number of children a node has
        # subtree given tree and node: given a tree and node return the subtree 
        # leaf node: a node with no children
        # internal node: a node that is not a root node nor a leaf node
        # add tests
    root = RootNode('root node')
    node1 = Node('node 1')
    tree= Tree(root)
    branch1 = Branch(root, node1)
    tree.add_branch(branch1)
    nodes=tree.nodes


class Stack:
    """A stack is a data structure that allows for the last element added to be the first element removed."""
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.size() == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

class Queue:
    """A queue is a data structure that allows for the first element added to be the first element removed."""
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.size() == 0 

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)

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
    print("All stack push tests pass")

def test_stack_pop():
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    assert my_stack.pop() == 2
    assert my_stack.size() == 1
    assert my_stack.pop() == 1
    assert my_stack.size() == 0
    assert my_stack.pop() == None
    print("All stack pop tests pass")

def test_queue_enqueue():
    my_queue = Queue()
    assert my_queue.size() == 0
    my_queue.enqueue(1)
    assert my_queue.size() == 1
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    assert my_queue.size() == 3
    print("All queue enqueue tests pass")

def test_queue_dequeue():
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    assert my_queue.dequeue() == 1
    assert my_queue.size() == 1
    assert my_queue.dequeue() == 2
    assert my_queue.size() == 0
    assert my_queue.dequeue() == None
    print("All queue dequeue tests pass")
