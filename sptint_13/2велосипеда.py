
def calculator(savings, bicycle_price, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if mid==1 and savings[mid-1] >= bicycle_price:
        return mid-1+1
    elif savings[mid] >= bicycle_price and savings[mid -1] < bicycle_price:
        return mid+1
    elif bicycle_price <= savings[mid] and bicycle_price <= savings[mid-1]:
        return calculator(savings, bicycle_price, left, mid)
    else: 
        return calculator(savings, bicycle_price, mid + 1, right)


def input_data(file_name):
    with open(file_name, 'r') as data:
        days_num = int(data.readline().strip())
        savings = list(map(int, data.readline().split()))
        bicycle_price = int(data.readline().strip())
        index1 = calculator(savings, bicycle_price, 0, len(savings))
        index2 = calculator(savings, bicycle_price*2, 0, len(savings))
        print(index1, index2 )

if __name__ == '__main__':
    input_data('input.txt')