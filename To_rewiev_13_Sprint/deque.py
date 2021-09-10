# ID: 52880611

class My_deque_sized:
    def __init__(self, values_num):
        self.queue = [None] * values_num
        self.max_n = values_num
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_front(self, value):
        if self.size != self.max_n:
            self.head = (self.head - 1) % self.max_n
            self.queue[self.head] = value
            self.size += 1
        else:
            print('error')

    def push_back(self, value):
        if self.size != self.max_n:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop_front(self):
        if self.is_empty():
            return 'error'
        pop_value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return pop_value

    def pop_back(self):
        if self.is_empty():
            return 'error'
        pop_value = self.queue[self.tail-1]
        self.queue[self.tail-1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return pop_value


def input_data(file_name):
    with open(file_name, 'r') as data:
        command_num = int(data.readline())
        values_num = int(data.readline())
        data = data.read().splitlines()
        d = My_deque_sized(values_num)

        for command in data:
            if 'pop_front' in command:
                print(d.pop_front())
            elif 'pop_back' in command:
                print(d.pop_back())
            elif 'push_front' in command:
                command = command.strip().split()
                d.push_front(int(command[1]))
            elif 'push_back' in command:
                command = command.strip().split()
                d.push_back(int(command[1]))


if __name__ == '__main__':
    input_data('input.txt')
