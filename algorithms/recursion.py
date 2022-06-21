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