# ID: 52414802


def zero_dists(street_lenght, map):
    distance = street_lenght
    dist = []
    for n in map:
        if n == '0':
            distance = 0
            dist.append(distance)
        else:
            distance += 1
            dist.append(distance)
    return dist


street_lenght = int(input())
numbers = input().split()

left_distance = zero_dists(street_lenght, numbers)
right_distance = reversed(tuple(zero_dists(street_lenght, reversed(numbers))))

print(*map(min, zip(left_distance, right_distance)))
