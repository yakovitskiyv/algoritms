class My_deque_sized:
    def __init__(self, values_num):
        self.queue = [None] * values_num
        self.max_n = values_num
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_front(self, x):
        #print('push_front called')
        if self.size != self.max_n:
            self.head = (self.head - 1) % self.max_n
            self.queue[self.head] = x

            self.size += 1
            # return x
        else:
            print('error')

    def push_back(self, x):
        #print('push_back called')
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
            # return x
        else:
            print('error')

    def pop_front(self):
        if self.is_empty():
            return 'error'
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            return 'error'
        x = self.queue[self.tail-1]
        self.queue[self.tail-1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return 'error'
        return self.queue[self.head]

    def q_size(self):
        return self.size


def input_data(file_name):
    with open(file_name, 'r') as data:
        #commands = []
        command_num = int(data.readline())
        values_num = int(data.readline())

        #print('command_num', command_num,'values_num', values_num)
        data = data.read().splitlines()

        d = My_deque_sized(values_num)
        for command in data:
            # commands.append(command.split())
            #command = 'deque.' + command
            # print(commands)
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
            #print('command', command, 'queue:', d.queue, 'HEAD', d.head, 'TAIL', d.tail)


if __name__ == '__main__':
    input_data('input.txt')
    # test()
