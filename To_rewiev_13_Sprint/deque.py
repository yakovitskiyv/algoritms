# ID: 53109928


class My_deque_sized:
    def __init__(self, values_num):
        self.queue = [None] * values_num
        self.max_n = values_num
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_n

    def push_front(self, value):
        if self.is_full():
            raise IndexError
        self.head = (self.head - 1) % self.max_n
        self.queue[self.head] = value
        self.size += 1

    def push_back(self, value):
        if self.is_full():
            raise IndexError
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        pop_value = self.queue[self.head]
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return pop_value

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        pop_value = self.queue[self.tail-1]
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return pop_value


def input_data(file_name):
    with open(file_name, 'r') as data:
        command_num = int(data.readline().strip())
        values_num = int(data.readline().strip())
        data = data.read().splitlines()
        my_deque = My_deque_sized(values_num)

    COMMANDS = {
        'push_back': my_deque.push_back,
        'push_front': my_deque.push_front,
        'pop_front': my_deque.pop_front,
        'pop_back': my_deque.pop_back,
    }

    def print_result(value):
        if value is not None:
            print(value)

    for line in data:
        command, *argument = line.split()
        if command not in COMMANDS:
            print(f'Команда {command} не поддерживается.')
            break
        if argument:
            try:
                result = COMMANDS[command](*argument)
                print_result(result)
            except IndexError:
                print('error')
        else:
            try:
                result = COMMANDS[command]()
                print_result(result)
            except IndexError:
                print('error')


if __name__ == '__main__':
    input_data('input.txt')
