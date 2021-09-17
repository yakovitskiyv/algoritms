# ID: 53109596


import operator

OPERATORS = {'+': lambda x, y: operator.iadd(x, y),
             '-': lambda x, y: operator.isub(x, y),
             '*': lambda x, y: operator.imul(x, y),
             '/': lambda x, y: operator.ifloordiv(x, y),
             '%': lambda x, y: operator.imod(x, y),
             '^': lambda x, y: operator.pow(x, y)
             }


class Stack:
    def __init__(self):
        self.items = []

    def push(self, operand):
        self.items.append(operand)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError('Ошибка: попытка извлечения из пустого стека.')

    def size(self):
        return len(self.items)


def calculator(seq, operators=OPERATORS):
    stack = Stack()
    for symbol in seq.split():
        if symbol in operators:
            num2, num1 = stack.pop(), stack.pop()
            try:
                result = int(operators[symbol](num1, num2))
            except ZeroDivisionError:
                raise ZeroDivisionError(
                    f'Деление на 0 при вычислении {num1} / 0.')
            stack.push(result)
        else:
            stack.push(int(symbol))
    return stack.pop()


def input_data(file_name):
    with open(file_name, 'r') as data:
        seq = data.readline()
        print(calculator(seq))


if __name__ == '__main__':
    input_data('input.txt')
