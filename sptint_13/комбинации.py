def text_button(input_data):

    key_letters ={
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
            }

    for num in input_data:
        print(int(num))
        for letter in key_letters[int(num)]:
            print(letter)
            



def input_data(file_name):
    with open(file_name, 'r') as data:
        input_data = data.readline().strip()
        print(input_data)
        text_button(input_data)


if __name__ == '__main__':
    input_data('input.txt')