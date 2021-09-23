def bSort(array):
    # определяем длину массива
    length = len(array)
    #Внешний цикл, количество проходов N-1
    for i in range(length):
        # Внутренний цикл, N-i-1 проходов
        for j in range(0, length-i-1):
            #Меняем элементы местами
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    print(array)

bSort([11, 2, 9, 7, 1])
