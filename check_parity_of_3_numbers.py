

numbers = input().split()

if int(numbers[0]) % 2 == int(numbers[1]) % 2 == int(numbers[2]) % 2:
    print('WIN')
else:
    print('FAIL')

"""

input()
numbers = input().split()
num1 = numbers[0]
num2 = numbers[1]
num3 = numbers[2]
print(num1, num2, num3)
print("WIN") if(len(list(filter(lambda x: x % 2 == 0, [int(
    input("Value "+str(i+1)+":\n")) for i in range(3)]))) % 3 == 0) else print("FAIL")
"""
