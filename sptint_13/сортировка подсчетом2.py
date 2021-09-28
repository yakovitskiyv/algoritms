
def counting_sort(item_num, alist, largest):
    c = [0]*(largest+1)
    for value in alist:
        c[value] += 1

    c[0] = c[0] - 1
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [0]*item_num

    for x in reversed(alist):
        result[c[x]] = x
        c[x] = c[x] - 1
    return result


def input_data(file_name):
    with open(file_name, 'r') as data:
        item_num = int(data.readline().strip())
        item_seq = list(map(int, data.readline().split()))
        res = (counting_sort(item_num, item_seq, 3))
        print(*res)


if __name__ == '__main__':
    input_data('input.txt')
