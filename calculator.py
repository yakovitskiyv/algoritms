# ID: 53014109

import math


class Stack:
    def __init__(self):
        self.operands = []

    def push(self, operand):
        self.operands.append(operand)

    def pop(self):
        try:
            return self.operands.pop()
        except IndexError:
            raise IndexError('Недостаточно операндов для вычисления.')

    def size(self):
        return len(self.operands)


def my_int(value):
    if isinstance(value, str):
        return int(value)
    return math.floor(value)


def calculator(seq):
    s = Stack()
    for symbol in seq.split():
        if symbol in '-+*/':
            num2, num1 = my_int(s.pop()), my_int(s.pop())
            command = str(num1) + str(symbol) + str(num2)
            try:
                result = my_int(eval(command))
                s.push(result)
            except ZeroDivisionError:
                raise ZeroDivisionError(
                    f'Деление на 0 при вычислении {num1} / {num2}.')
        else:
            s.push(symbol)
    return s.pop()


def input_data(file_name):
    with open(file_name, 'r') as data:
        seq = data.readline()
        print(calculator(seq))


if __name__ == '__main__':
    input_data('input.txt')
