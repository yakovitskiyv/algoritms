class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        #self.tail = None

    def put(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def get(self):
        if self.head is None:
            return 'error'
        if self.head.next is None:
            temp = self.head.value
            self.head = None
            return temp
        temp = self.head.value
        n = self.head
        while n.next is not None:
            n = n.next
            n.prev.next = None
            return n.value

    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count+1
            temp = temp.next
        return count

    def first(self):
        return self.head.value

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def printqueue(self):
        print("queue elements are:")
        temp = self.head
        while temp is not None:
            print(temp.value, end="-> ")
            temp = temp.next


def input_data():
    command_num = int(input())
    commands = []
    for i in range(command_num):
        commands.append(input().split())

    # print(commands)
    q = Queue()
    for i in commands:

        if 'get' in i:
            print(q.get())

        elif 'size' in i:
            print(q.size())
        if 'put' in i:
            q.put(int(i[1]))
    # q.printqueue()


if __name__ == '__main__':
    input_data()
    # test()6
