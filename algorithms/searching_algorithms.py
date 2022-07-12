from math import floor

def binary_search(arr, element, start, end):
    # works when our data is sorted
    # find the middle
    # if element == arr[middle] return arr[middle]
    # elif element < arr[middle] return binary_search(arr, element, start, middle-1)
    # elif element > arr[middle] return binary_search(arr, element, middle-1, len(arr))
    if start > end: return -1

    middle = floor((start + end)/2)
    if element == arr[middle]:
        return middle
    
    if element < arr[middle]:
        return binary_search(arr, element, start, middle-1)
    elif element > arr[middle]:
        return binary_search(arr, element, middle+1, end)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []
nodes_in_queue = []

def breadth_first_search(visited, graph, node):
    # uses more memory that depth fist search
    # we will be using a queue data structure
    # which allows us to keep a reference to nodes
    # we want to come back to.
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    pass


def depth_first_search():
    pass