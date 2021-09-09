class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print('error')
            return 'error'
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if len(self.items) != 0:
            print(max(self.items))
            return max(self.items)
        print(None)
        return None


def test():
    stack = StackMax()
    stack.push(1)
    stack.push(2)
    stack.push(4)

    stack.get_max()
    # print(stack.peek())
    stack.size()
    stack.pop()
    stack.get_max()
    stack.pop()
    stack.get_max()
    stack.pop()
    stack.get_max()

    stack.pop()


#test()

def input_data():
    stack = StackMax()
    command_num = int(input())
    commands =[]
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
#test()