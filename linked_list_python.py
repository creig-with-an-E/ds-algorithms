class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return '<Node val=\'%s\' />' % self.val


class LinkedList:
    def __init__(self, val):
        newNode = Node(val)
        self.head = newNode
        self.tail = self.head
        self.length = 1

    def __repr__(self):
        elements = []
        current_node = self.head

        while current_node is not None:
            elements.append(current_node.val)
            current_node = current_node.next

        return '<LinkedList elements=\'%s\' />' % elements

    def _validate_index_val(self, index):
        if not isinstance(index, int):
            index_type = type(index)
            raise ValueError('Expected index of value type int, but got %s' % index_type)
        
        if index < 0 or index > self.length:
            raise IndexError('Index out of range')

        return True

    def traverse_to_index(self, index):
        '''
        
        '''
        # validate index
        # first we need a counter to know what index we are now at
        # we will traverse the list by finding current_node.next(i)
        self._validate_index_val(index)
        counter = 0
        current_node = self.head

        while counter != index:
            counter += 1
            current_node = current_node.next

        return current_node


    def append(self, val):
        '''
        Adds new node to the end of the list
        :param: `val`
        '''
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
    
    def prepend(self, val):
        '''
        Adds to the beginning of the list
        '''
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, val, index):
        '''insert new node in list'''
        # visualization
        # 1    3 - 4 - 5
        #   \ /
        #    2

        # --- steps
        # - validate params
        # - index is int, index < self.length -1
        # find the preceding node
        # link new_node.next to 
        # where 1 is the preceding
        # 3 is preceding.next

        # iterate till we find the preceding node

        if index >= self.length:
            return self.append(val)
        
        if index == 0:
            return self.prepend(val)

        preceding_node = self.traverse_to_index(index-1)

        node = Node(val)
        node.next = preceding_node.next
        preceding_node.next = node
        self.length += 1

    def remove(self, index):
        # this will be similar to insert O(n)
        # as we will need to traverse the list
        # validate index

        # visual representation
        #  1 -> 2 -> 3 -> 4
        # find the preceding node
        # where 1 in the preceding node
        # 2 is preceding.next
        # preceding to point to preceding.next.next

        if index == 0:
            unwanted_node = self.head
            self.head = self.head.next
            self.length -= 1
        
        elif index == self.length-1:
            unwanted_node = self.tail

            # find the preceding node and make it the tail
            preceding_node = self.traverse_to_index(index-1)
            preceding_node.next = None
        
        else:
            preceding_node = self.traverse_to_index(index-1)
            unwanted_node = preceding_node.next
            preceding_node.next = unwanted_node.next

        return unwanted_node
    
    def reverse_list(self):
        # check to see how many items in a list
        # 1 -> 2 -> 3 -> 4 -> null

        # start off by checking that this is not an empty list

        if self.head.next is None:
            return self

        # need 2 pointers
        current = self.head
        following = current.next

        # 2
        # set tail =  head
        self.tail = self.head

        # 3 iterate as long as following is not None
        while following is not None:
            # in our loop we keep track of the 3rd temp pointer
            # which is the next element in the sequence
            # temp = following.next
            # then we point [2] -> [1]
            # update current, curent = following
            # update following; following = temp
            # 
            temp = following.next
            following.next = current
            current = following
            following = temp

        self.head.next = None
        self.head = current

        return self


mylist = LinkedList(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.insert(100,4)


# print(mylist)
mylist.prepend(0)
mylist.insert('ZEROOO', 0)
# print(mylist)

mylist.remove(5)
# print(mylist)

print('reversed--------  ',mylist.reverse_list())