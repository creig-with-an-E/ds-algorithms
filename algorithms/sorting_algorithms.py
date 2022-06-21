from copy import deepcopy
import math

# Bubble sort
def bubble_sort(x):
    # we will need 2 loops
    # compare the first element with the second in the list
    # outter loops ensures we come back and compare each element with all the others
    data_set = deepcopy(x)
    for i in range(len(data_set)):
        for j in range(len(data_set)-1):
            if data_set[j] > data_set[j+1]:
                data_set[j], data_set[j+1] = data_set[j+1], data_set[j]

    return data_set


def selection_sort(x): 
    # O(n^2)
    # scan the list and find the smallest item
    # move the smallest to beginning and start over
    for i in range(len(x)):
        min_indx = i
        for j in range(i+1, len(x)):
            if x[j] < x[min_indx]:
                min_indx = j

        x[i], x[min_indx] = x[min_indx], x[i]

    return x
                

class SortingAlgorithms:
    def bubble_sort(self, data_set):
        # we use two pointers left and right
        # compare the first (left) and next (right)
        # if right is smaller, switch them around
        # move the next iteration, compare next and next.next()
        
        for i in range(len(data_set)):
            for j in range(len(data_set)-1):
                if data_set[j+1] < data_set[j]:
                    data_set[j], data_set[j+1] = data_set[j+1], data_set[j] 
        return data_set
    
    def selection_sort(self, data_set):
        # iterate over the list keeping track of the smallest
        # this means? 2 pointers
        # pointer_1 -> smallest
        # pointer_2 -> holding pointer
        for i in range(len(data_set)):
            smallest_index = i
            temp = data_set[i]
            for j in range(i, len(data_set)):
                if data_set[j] < data_set[smallest_index]:
                    smallest_index = j
            data_set[i] = data_set[smallest_index]
            data_set[smallest_index] = temp

        return data_set
    
    def insertion_sort(self, arr):
        # ref: ====
        # https://realpython.com/sorting-algorithms-python/#:~:text=sorting%20large%20arrays.-,The%20Insertion%20Sort%20Algorithm%20in%20Python,it%20into%20its%20correct%20position.
        # =========
        # we compare each value with the rest of the list
        # loop from second element to the last
        # fast when data is fairly sorted
        # fast when dealing with small data sets
        # [29, 1, 5, 65, 9 , 31, 11]
        # start by comparing 29 and 1
        # [1, 29, 5, 65, 9, 31, 11]
        for i in range(1, len(arr)):
            # this is the element to position to the correct place
            key_item = arr[i]

            # initialize the variable that will point to 
            # each element on the left side
            j = i - 1

            # run through the list of items from the key_item to the vals on the left
            while j >= 0 and arr[j] > key_item:
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = key_item
           
        return arr

# end of elementary sorting algorithms with nested for-loops

    def merge_sort(self, arr):
        if len(arr) == 1:
            return arr
        
        # split arr in half
        length = len(arr)
        middle = math.floor(length/2)
        left = arr[0:middle]
        right = arr[middle: len(arr)]
        
        return self._merge(
            self.merge_sort(left),
            self.merge_sort(right))
    
    def _merge(self, left, right):
        result = []
        left_index = 0
        right_index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        
        result.extend(left[left_index: len(left)])
        result.extend(right[right_index:len(right)])
        return result