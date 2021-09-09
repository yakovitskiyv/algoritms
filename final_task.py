# Эти 2 части перенести в if __name__ == "__main__"  и сделать def "snake_case"
from collections import Counter
"""
k = int(input()) * 2
matrix = []
for i in range(4):
    numbers = input()
    matrix += numbers
t = 1
score = 0

while t <= 9:
    count_t = matrix.count(str(t))
    if 0 < count_t <= k:
        score += 1  # Тут была идея сделать функцию sum() с условием, чтобы избавиться от лишних строк, но не знаю, нужно это или нет
    t += 1
print(score)

# 2
k = int(input())
c = Counter(int(x) for _ in range(4) for x in input() if x != ".")
result = sum(x <= 2 * k for x in c.values())
print(result)
"""
#3
import collections

k = int(input()) * 2
print(sum(                                      # 4
    1                                           # 4
    for key, v in collections.Counter(          # 2  
        c for _ in range(4) for c in input()    # 1
    ).items()                                   # 3
    if key.isdigit() and v <= k
))
