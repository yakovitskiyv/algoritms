class Stack:
    def __init__(self):
        self.operands = []

    def push(self, operand):
        self.operands.append(operand)
        print(self.operands)

    def pop(self):
        try:
            return self.operands.pop()
        except IndexError:
            raise IndexError('Недостаточно операндов для вычисления.')

    def size(self):
        return len(self.operands)


def calculator():
    pass


def input_data(file_name):
    s = Stack()
    with open(file_name, 'r') as data:
        seq = data.readline()
        for symbol in seq.split():
            if symbol in '0123456789':
                s.push(symbol)


if __name__ == '__main__':
    input_data('input.txt')
