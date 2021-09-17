arr =[1, 3, 5, 8]

def sum(n):
    if n == 0:
        return 0
    return n + sum(n- 1)

print(sum(10))
