# ID: 52422549


def zero_dists(street_lenght, street_map):
    distance = street_lenght
    dist = []
    for land_area in street_map:
        if land_area == '0':
            distance = 0
            dist.append(distance)
        else:
            distance += 1
            dist.append(distance)
    return dist


if __name__ == '__main__':
    street_lenght = int(input())
    numbers = input().split()

    left_distance = zero_dists(street_lenght, numbers)
    right_distance = reversed(
        tuple(zero_dists(street_lenght, reversed(numbers))))

    print(*map(min, zip(left_distance, right_distance)))
