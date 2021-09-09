row_num = int(input())
column_num = int(input())
mat = []
index=[]
mat_rev= []

for i in range(row_num):
    numbers = input().split()
    mat += numbers

count=0

for n in range(column_num):
    count=n
    for num in range (row_num):
        index.append(count)
        mat_rev.append(mat[count])
        count=count+column_num

for num in range(column_num):
    string_row =''
    for nn in range(row_num):
        string_row += mat_rev[nn+row_num*num]+' '
    print(string_row)     
