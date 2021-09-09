"""
n = int(input())
numbers = input().split()
for i in range(n):
    if numbers[i] != '0':
        l = 10**6
        for a in range(n):
            if numbers[i - a] == '0':
                if a <= i and l > a:
                    l = a
                if a > i and l > n - a:
                    l = n - a
            numbers[i] = l
print(*numbers)
"""

def zero_dists(start, seq):
    d = start
    for n in seq:
        if n == '0':
            d = 0
        else:
            d += 1
        yield d


input()
numbers = input().split()

to_left = zero_dists(len(numbers), numbers)
to_right = reversed(tuple(zero_dists(len(numbers), reversed(numbers))))

print(*map(min, zip(to_left, to_right)))
