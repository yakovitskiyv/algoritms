
def num_strength(num_1, num_2):  # функция-компаратор
    num_1_strength = str(abs(num_1))
    num_2_strength = str(abs(num_2))
    return num_1_strength + num_2_strength < num_2_strength + num_1_strength

# воспользуемся уже знакомой сортировкой вставками
def insertion_sort_by_comparator(array, less):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
    # заменим сравнение item_to_insert < array[j-1] на компаратор less
        while j > 0 and less(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
            array[j] = item_to_insert
    return print_result(array)

def print_result(array):
    num = ''
    for i in reversed(array):
        num +=str(i)
    return num


def input_data(file_name):
    with open(file_name, 'r') as data:
        lenght_seq = int(data.readline().strip())
        seq = list(map(int, data.readline().split()))

        print(insertion_sort_by_comparator(seq, num_strength))

if __name__ == '__main__':
    input_data('input.txt')
