
def input_data(file_name):
    with open(file_name, 'r') as data:
        commands = []
        n = data.readline()
        data = data.read().splitlines()
        

        for command in data:
            commands.append(command.split())
            #command = 'deque.' + command
            
            print(commands)

if __name__ == '__main__':
    input_data('input.txt')
    # test()