
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


x = [1, 2, 3, 1, 2, 3, 1, 2, 3, 22, -5, 12, 0]


quick_sort(x, 0, len(x)-1)

print(x)
