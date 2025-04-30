# fibonacci sequence 
def fibonacci(n: int) -> list[int]:
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]


print(fibonacci(10))

# factorial function 
def factorial(n: int):
    i = 1
    if n > 1:
        for n in range(1,n+1): 
            i = i*n
        return i

# no. possibilities of the order of cards when shuffling a deck of cards
print(factorial(52))

# fibonacci sequence recursively 
def fib_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fib_recursive(n-1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
    
print(fib_recursive(3))

# factorial function recursively
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1) 
    
print(factorial_recursive(5))

