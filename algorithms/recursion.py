# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!
def factorialRecursiveCall(n):
    # O(n)
    if n == 2:
        return 2
    return n * factorialRecursiveCall(n-1)


def factorialIterative(n):
    # avoid wasting time with 1 and 2 which
    # always return themselves
    # O(n)
    answer = 1
    if n == 2:
        return 2
    
    for i in range(2, n+1):
        answer = answer * i

    return answer

# Fibonacci 
# 0, 1, 1, 2, 3, 5, 8

def fibonnaci_recursive(n):
    if n < 2:
        return n

    return fibonnaci_recursive(n-2) + fibonnaci_recursive(n-1)


def fibonacci_iterative(n):
    arr = [0,1]
    for i in range(2,n+1):
        arr.push(arr[i-2] + arr[i-1])
    return arr[n]


def reverse_string_iterative(input_string):

    return [input_string[i-1] for i in range(len(input_string),0,-1)].join('')


def reverse_string_recursive(input_string):
    if input_string == '':
        return ''
    
    return reverse_string_recursive(input_string[1]) + input_string[0]


# def merge_sort(self, arr):
#         # divide and conquor
#         # recursively split arr in half till we get to a single element
#         if len(arr) == 1:
#             return arr

#         middle = math.floor(len(arr)/2)
#         left = arr[0:middle]
#         right = arr[middle: len(arr)]

#         return self._merge(
#                     self.merge_sort(left),
#                     self.merge_sort(right)
#                 )

#     def _merge(self, left, right):
#         result = []
#         left_index = 0
#         right_index = 0
#         while left_index < len(left) and right_index < len(right):
#             if left[left_index] < right[right_index]:
#                 result.append(left[left_index])
#                 left_index += 1
#             else:
#                 result.append(right[right_index])
#                 right_index += 1
        
#         result.extend(left[left_index: len(left)])
#         result.extend(right[right_index:len(right)])
#         return result