class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    
    def __repr__(self):
        return '<Node value=\'%s\' right=\'%s\' left=\'%s\' />' % (self.value, self.right, self.left)


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        #            9              * check that we have a root node? if not make root node
        #        /       \          * check that val is greater than root? yes-> node will be on the right, else left
        #       4         12        * after determing side of node, check that root.[side] is None? if so make that current node, else
        #      / \       /  \       * compare current node to [side].value and assign left if smaller else assign right
        #     1   5     11  13 
        
        # steps
        # 1 create the new node
        # 2 check root node, if not make root_node: EXIT
        # 3 start iterating on tree starting at current_node = self.root
        #   check that value is less than current_node.value
        #   if less go left. else right

        node = Node(value)
        if self.root is None:
            self.root = node
            return self
        
        current_node = self.root
        while True:
            if value < current_node.value:
                # go left
                if current_node.left is None:
                    current_node.left = node
                    return self
                else:
                    # update the current_node
                    current_node = current_node.left
            else:
                # right
                if current_node.right is None:
                    current_node.right = node
                    return self
                else:
                    # update current_node -> current_node.right
                    current_node = current_node.right

    def lookup(self, value):
        # confirm that root is not None
        # starting from current_node = self.root
        # iterate over tree
        # checking that value is greater or less than current_value
        # if less than we search left
        # else search right
        if self.root is None:
            return None
        
        current_node = self.root
        while current_node is not None:
            # val < current_node: go left, else right
            if value < current_node.value:
                # left
                current_node = current_node.left
            elif value > current_node.value:
                # greater-> go right
                current_node = current_node.right
            elif value == current_node.value:
                # found the value
                return current_node
        return False

    def remove(self, value):
        # check that not empty, if empty return None
        # start traversing through list
        # keeping two pointers current_node & parent_node
        # if less than go left
        # if greater than go right
        # when we find the node, we keep ref to node
        # bypass the node and continue right, if plausible
        # then find the most left node and 
        if self.root is None:
            return None
        
        current_node = current_node
        parent_node = None
        while current_node is not None:
            if current_node.value < value:
                # less than
                current_node = current_node.left
            elif current_node > value:
                current_node = current_node.right
            elif current_node.value == value:
                # found node
                return

        return None
    
    def breadth_first_search(self):
        '''Iterative breadth first search'''
        current_node = self.root
        arr = []
        queue = []
        queue.append(self.root)

        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.value)
            arr.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            
        return arr


def traverse(node):
    tree = {'value': node.value}
    tree['left'] = traverse(node.left) if node.left else None
    tree['right'] = traverse(node.right) if node.right else None

    return tree