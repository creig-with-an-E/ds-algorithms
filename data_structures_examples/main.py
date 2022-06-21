def search_for_common(ar_1, ar_2):
    '''
    To confirm if there are common elements
    '''
    # there goes readability
    common_elements = set(ar_1).intersection(ar_2)

    return len(common_elements) > 0


response = search_for_common([1,3,4,5,6], [2,3,4,5])
print(response)


class OutOfBoundsException(Exception):
    pass


class CustomArray:
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def __str__(self):
        return ','.join(self.data.values())

    def __repr__(self):
        return ','.join(self.data.values())

    def lookup(self, index):
        # O(1)
        if index not in self.data:
            raise OutOfBoundsException('Index out of bounds')

        return self.data[index]
    
    def push(self, item):
        # O(1) constant time
        self.data[self.length] = item
        self.length += 1
        return item
    
    def pop(self):
        # O(1) linear time
        if self.length == 0:
            raise OutOfBoundsException('Index out of bounds')

        index = self.length-1
        item = self.data[index]
        del self.data[index]
        self.length -= 1

        return item

    
    def delete(self, index):
        # we delete at a certain index
        # move the rest of the elements to fill up the 
        # space from deleted element
        raise NotImplementedError()

        pass