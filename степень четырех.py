num=int(input())

def Is_power_of_four():
    if num == 4 or num == 1:
        return(True)

    temp = 4
    while (temp<=num):
        if temp == num:
            return(True)
        temp *=4
    if num!=1:
        return(False)

print(Is_power_of_four())