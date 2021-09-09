import time


def find_element(numbers, x):
    for i in range(len(numbers)):  # проходим по всем элементам массива
        if numbers[i] == x:  # сравниваем их с иксом
            return i  # если нашли - возвращаем индекс
    return -1  # если не нашли - возвращаем -1


print(find_element((1, 2, 3, 6, 9), 9))


# visitors - массив номеров пассажиров.
# Каждый пассажир проехал столько раз, сколько раз встречается его номер
visitors = [0, 2, 3, 2, 0, 4, 1, 1, 2]
entries_by_visitor = [0] * 5
best_visitor = 0

for visitor in visitors:
    entries_by_visitor[visitor] += 1
    if entries_by_visitor[visitor] > entries_by_visitor[best_visitor]:
        best_visitor = visitor

print(best_visitor)


time_start = time.time()
i = 0
while i < 10:
    # Do nothing
    i += 1

time_finish = time.time()
time_span = time_finish - time_start
print(time_span, 'seconds')


def eratosthenes(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(2 * num, n + 1, num):
                numbers[j] = False
    return numbers


print(eratosthenes(9))
