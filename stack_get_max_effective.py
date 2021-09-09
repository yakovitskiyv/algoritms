class StackMaxEffective:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    def push(self, x):
        self.main_stack.append(x)
        if (len(self.main_stack) == 1):
            self.max_stack.append(x)
            return

        if (x > self.max_stack[-1]):
            self.max_stack.append(x)
        else:
            self.max_stack.append(self.max_stack[-1])

    def get_max(self):
        if len(self.main_stack) == 0:
            print(None)
            return None
        print(self.max_stack[-1])
        return self.max_stack[-1]

    def pop(self):
        if len(self.main_stack) == 0:
            print('error')
            return 'error'
        self.max_stack.pop()
        return self.main_stack.pop()


def input_data():
    stack = StackMaxEffective()
    command_num = int(input())
    commands = []
    for i in range(command_num):
        commands.append(input())

    for command in commands:
        com = command.split()

        if len(com) == 1:
            command = 'stack.'+command+'()'
            eval(command)

        if len(com) == 2:
            command, value = command.split()
            command = 'stack.'+command+'(' + value+')'
            eval(command)


input_data()
# test()
