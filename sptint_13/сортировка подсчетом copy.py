
def counting_sort(size, array, k):

    output = [0] * size
    count = [0] * k

    for value in array:
        count[value] += 1

    for i in range(1, k):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
    return output

def input_data(file_name):
    with open(file_name, 'r') as data:
        item_num = int(data.readline().strip())
        item_seq = list(map(int, data.readline().split()))
        res = (counting_sort(item_num, item_seq, 3))
        print(*res)



if __name__ == '__main__':
    input_data('input.txt')
