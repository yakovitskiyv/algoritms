def buble_sort(lenght_array, array):
    count=0
    count_d = 0
    for i in range(lenght_array-1):
        flag =False
        count_d += 1
        for j in range(lenght_array-i-1):

            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = True
                count +=1
        #print('count', count, 'i', i, 'count_d', count_d)
        if  flag or (count == 0 and count_d+1==lenght_array):
            print(*array)

def input_data(file_name):
    with open(file_name, 'r') as data:
        lenght_array = int(data.readline().strip())
        input_data = list(map(int, data.readline().split()))
        buble_sort(lenght_array, input_data)


if __name__ == '__main__':
    input_data('input.txt')
