# implementing doubly linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return '<Node val=\'%s\'>' % (self.val)


class DoublyLinkedList:
    def __init__(self, val):
        self.head = Node(val)
        self.tail = self.head
        self.length = 1
    
    def _traverse_to_index(self, index):
        # TODO validate index
        # iterate till we reach the index
        # return node at index

        counter = 0
        current_node = self.head

        while counter != index:
            current_node = current_node.next
            counter += 1

        return current_node

    def __repr__(self):
        elements = []
        current_node = self.head

        while current_node is not None:
            elements.append(current_node.val)
            current_node = current_node.next

        return '<LinkedList elements=\'%s\' />' % elements

    def append(self, val):
        # add to the end
        # create the new node
        # new_node.prev = self.tail
        # self.tail.next = new_node
        # validate params
        node = Node(val)
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.length += 1
        return

    def prepend(self, val):
        # add beginning
        # we need to point new_node.next to self.head
        # self.head.prev = new_node
        # self.head = new_node

        node = Node(val)
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.length += 1

    def insert(self, val, index):
        # we need to find the preceding node
        # we still need a ref to preceding.next
        # link new_node.next to preceding.next
        # link preceding.next to new node

        # a - b - c [- d] - e

        if index == 0:
            return self.prepend(val)
        
        if index == self.length:
            return self.append(val)

        preceding_node = self._traverse_to_index(index-1)
        follower = preceding_node.next

        node = Node(val)

        preceding_node.next = node
        node.prev = preceding_node

        node.next = follower
        follower.prev = node

        self.length += 1
        return

    def remove(self, index):
        # a -> b -> c -> d -> e
        # get the unwanted node
        # using unwanted get the preceding, preceding = unwanted.prev
        # follower = unwanted.next
        # remove ref to unwanted

        # preceding.next = follower
        # follower.prev = preceding

        # what happens if it is first el or last without next or prev

        if index == 0:
            # removing head
            # get unwanted, unwanted = self.head
            # self.head = unwanted.next
            # what if there is no next?
            # can we have an empty linked list???

            unwanted_node = self.head
            self.head = unwanted_node.next
            self.head.prev = None
        
        elif index == self.length -1:
            # removing tail
            # set tail.next = None
            unwanted_node = self.tail
            self.tail = unwanted_node.prev
            self.tail.next = None

        else:
            # remove from middle O(n)
            unwanted_node = self._traverse_to_index(index)

            preceding_node = unwanted_node.prev
            follower_node = unwanted_node.next

            preceding_node.next = follower_node
            follower_node.prev = preceding_node

        self.length -= 1

        return unwanted_node

    def get_node_by_index(self, index):
        return self._traverse_to_index(index)


doubly_linked = DoublyLinkedList(1)
doubly_linked.prepend(0)
doubly_linked.append(2)
doubly_linked.append(3)
doubly_linked.insert(4, 4)

doubly_linked.remove(4)
print(doubly_linked.tail)
