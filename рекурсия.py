def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)



def factorial(n):
    accumulator = 1
    i = n
    while i > 1:
        accumulator *= i
        i -= 1
    return accumulator 

print(factorial(4))