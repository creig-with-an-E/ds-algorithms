# implementing queues and stacks using Python

# stacks can be implemented using Array and LinkedList

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        return '<Node value=\'%s\' />' % self.value


class Stack:
    # top and the bottom which is debatable considering
    # logic for a stack is to access the top element
    def __init__(self):
        self.top = None
        self.length = 0

    def __repr__(self):
        elements = []
        current_node = self.top
        while current_node is not None:
            elements.append(current_node.value)
            current_node = current_node.next
        return '<Stack length=\'%s\' elements=\'%s\' >'\
            % (self.length, elements)

    def push(self, val):
        '''Add new element to stack'''
        # create a new node
        # if stack is empty then set top to new_node
        # else get prev_top
        #   top = new_node
        #   top.next = prev_top
        # increase counter
        node = Node(val)
        if self.top is None:
            self.top = node
        else:
            holding_pointer = self.top
            self.top = node
            self.top.next = holding_pointer

        self.length += 1

        return self

    def peek(self):
        '''View top element'''
        return self.top.value

    def pop(self):
        '''Removes the top element'''
        # what if empty???
        # delete top element
        # get ref of top element
        # set top to top_e.next
        # reduce counter
        # return top_e

        if self.top is None:
            # raise error?
            return None

        node_to_delete = self.top
        self.top = node_to_delete.next
        self.length -= 1

        return node_to_delete


# test the implementation
browser_history = Stack()
browser_history.push('YouTube')
browser_history.push('Google')
browser_history.push('Facebook')


class StackArrayImplementation:
    def __init__(self):
        self.array = []

    def push(self, val):
        self.array.push(val)

    def pop(self):
        return self.pop()

    def peek(self):
        return self.array[len(self.array)-1]


class Queue:
    # FIFO: First In First Out
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        '''Adds to the back of queue'''
        # first in first out
        # create new node
        # if list empty then we make new_node the first and last
        # else make the new_node the last
        # self.last.next = new_node
        # self.last = new_node
        # increase the counter

        # first                   last
        # \                     /
        #  1 -- 2 -- 3 -- 4 -- 5
        node = Node(value)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1
        return self

    def deque(self):
        '''Removes the first one'''
        # check if queue is empty: do nothing or show error
        # one item in queue?? set first and last to null
        # decrement counter
        # if multiple in queue, remove first and next becomes first

        removed_node = None

        if self.first is None:
            return None

        removed_node = self.first
        if removed_node is self.last:
            self.last = None

        self.first = self.first.next
        self.length -= 1

        return removed_node

    def peek(self):
        '''See first element'''
        if self.first is None:
            return None
        return self.first.value
