import sys


def counting_sort(array, n, min=0, max=2):
    count = [0]*(max+1)
    for i in array:
        count[i] += 1
    result = []

    for j in range(min, max+1):
        result += [j] * count[j]
    return(result)


def input_data(file_name):
    with open(file_name, 'r') as data:
        item_num = int(data.readline().strip())
        item_seq = list(map(int, data.readline().split()))
        res = (counting_sort(item_seq, 3))
        print(*res)


if __name__ == '__main__':
    input_data('input.txt')
