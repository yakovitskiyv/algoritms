import math


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(self.items)

    def pop(self): 
        try:
            return self.items.pop()
            print(self.items)
        except IndexError:
            raise IndexError('Недостаточно операндов для вычисления.')

    def size(self):
        return len(self.items)


OPERATORS = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y,
             '%': lambda x, y: x % y,
             '^': lambda x, y: x ** y}

def MyInt(value):
    if isinstance(value, str):
        return int(value)
    return math.floor(value)

def calculator(line, stack=None, converter=int, operators=OPERATORS):
    stack = Stack() if stack is None else stack
    for element in line:
        if element in operators:
            el1, el2 = stack.pop(), stack.pop()
            try:
                stack.push(converter(operators[element](el2, el1)))
                #print(el1, el2,converter(operators[element](el2, el1)))
            except ZeroDivisionError:
                raise ZeroDivisionError(f'Деление на 0 при вычислении "{el2} {element} {el1}".')
            except TypeError:
                raise TypeError(f'Неподдерживаемая операция "{element}" для типа {converter.__name__}.')
        else:
            try:

                stack.push(converter(element))
            except:
                raise KeyError(f'Невозможно преобразовать "{element}" в {converter.__name__} или неподдерживаемая операция.')
    if stack.size() > 1:
        raise IndexError('Некорректное выражение - в стеке остались элементы.')
    return stack.pop()




def input_data(file_name):

    with open(file_name, 'r') as data:
        seq = data.readline().split()
        #calculator(seq)
        from decimal import Decimal
        #seq = line.split()
        for t in (MyInt,):
            print(f"{t.__name__:>10} = ", end='')
            try:
                print(calculator(seq, converter=t))
            except (KeyError, IndexError, ZeroDivisionError, TypeError) as err:
                print("Ошибка!", err)



if __name__ == '__main__':
    input_data('input.txt')