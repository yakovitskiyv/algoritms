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


    row_arr = []
    comb_arr =[]
    comb_word = ''

    for num in input_data:
        digit_letter = []
        for letter in key_letters[int(num)]:
            digit_letter.append(letter)
        row_arr.append(digit_letter)
        arr=len(row_arr)

    #comb_word += row_arr[0][0]
    for i in range(arr):
        print('i', i)
        comb_word += row_arr[i][0]

    comb_arr.append(comb_word)

    print(comb_arr)    


 



def input_data(file_name):
    with open(file_name, 'r') as data:
        input_data = data.readline().strip()
        text_button(input_data)


if __name__ == '__main__':
    input_data('input.txt')
