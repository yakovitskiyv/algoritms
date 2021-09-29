
def quick_sort(arr,left,right):
    if left >= right:
        return
    mid = (left+right)//2
    sep = arr[mid]
    i = left
    j = right
    while True:
        while arr[i] < sep:
            i += 1
        while arr[j] > sep:
            j -= 1
        if (i <= j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        if (i > j):
            break
    quick_sort(arr, left, j)
    quick_sort(arr, i, right)


x = [4, 6, 2, 2, 4]


quick_sort(x, 0, len(x)-1)

print(x)
