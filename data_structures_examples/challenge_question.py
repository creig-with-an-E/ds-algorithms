# implement a queue using a stack

# stack is a last in first out mechanism

class MyQueue:
    def __init__(self):
        self.first = []
        self.last = []

    def __repr__(self):
        return '<MyQueue length=\'%s\' elements=\'%s\' />'\
            % (len(self.last), self.last)

    def push(self, value):
        for i in range(len(self.first)):
            self.last.append(self.first.pop())

        self.last.append(value)
        return self

    def pop(self):
        for i in range(len(self.last)):
            self.first.append(self.last.pop())
        self.first.pop()
        return self

    def peek(self):
        if len(self.last) > 0:
            return self.last[0]
        return self.first[len(self.first)-1]

    def empty(self):
        pass