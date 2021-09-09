row_num = int(input())
column_num = int(input())
mat = []


for i in range(row_num):
    numbers = input().split()
    mat += numbers

count = 0
string_row = ''
for n in range(column_num):
    string_row = ''
    count = n
    for num in range(row_num):
        string_row =string_row+mat[count] + ' '
        count = count+column_num
    print(string_row)
