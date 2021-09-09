class Node:

    def __init__(self, data):
        self.data = data  
        self.prev = None  
        self.next = None 
        
        
class Queue:

    def __init__(self):
        self.head = None
        self.last = None

    def put(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev = self.last
            self.last = self.last.next

    def get(self):
        if self.head is None:
            return 'error'
        else:
            if self.head.next is None:
                temp = self.head.data
                self.head = None
                self.last = None
                return temp

            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    def first(self):
        return self.head.data

    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count+1
            temp = temp.next
        return count

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def printqueue(self):
        print("queue elements are:")
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
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
