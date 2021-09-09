"""
n = int(input())
m = int(input())

matrix = [list(map(int, input(f'строка {i}: ').split()))
          for i in range(int(n))]

y = int(input())
x = int(input())

res = []
try:
    res.append(matrix[y][x+1])
    print('1', res)
except:
    pass
try:
    res.append(matrix[y][x-1])
    print('2', res)
except:
    pass
try:
    res.append(matrix[y+1][x])
    print('3', res)
except:
    pass
try:
    res.append(matrix[y-1][x])
    print('4', res)
except:
    pass

print(*sorted(res))
"""


def neighbors(matrix, y, x):
    h = []
    if x + 1 < len(matrix[0]):
        h.append(matrix[y][x + 1])
    if x - 1 >= 0:
        h.append(matrix[y][x - 1])
    if y + 1 < len(matrix):
        h.append(matrix[y + 1][x])
    if y - 1 >= 0:
        h.append(matrix[y - 1][x])
    return h


n = int(input())
m = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
y = int(input())
x = int(input())
print(*sorted(neighbors(matrix, y, x)))
