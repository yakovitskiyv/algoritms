lenght= int(input())
form =  input().strip().split()
number = int(input())

num=''
for n in form:
    num += n
    
num = int(num)
num = num + number

num = str (num)
form = ''
for i in num:
    form +=i+ ' '
print(form)