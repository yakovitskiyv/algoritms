def fibonacci(n):
    cur = 1
    if n >= 2:
        cur = fibonacci(n-1) + fibonacci(n-2)
    return cur


element, k = map(int, input().split())

value = fibonacci(element)
print(str(value%10**k))
