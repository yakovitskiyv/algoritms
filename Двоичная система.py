# получить бинарное число в виде массива чисел (бит)
num1 = [*map(int, input())]
num2 = [*map(int, input())]

# перевернуть числа для удобства выполнения операций
num1 = num1[::-1]
num2 = num2[::-1]

# дополнить числа нулями
size = max(len(num1), len(num2))

num1 += [0] * (size - len(num1))
num2 += [0] * (size - len(num2))

# сложить 2 числа
overflow = 0
res = []
for obj in zip(num1, num2):
    value = obj[0] + obj[1] + overflow
    overflow = value // 2
    res.append(value % 2)

# если флаг переполнения установлен - добавить бит в начало нового числа
if overflow == 1:
    res.append(1)

# перевернуть число назад
res = res[::-1]

print(''.join(map(str, res)))
