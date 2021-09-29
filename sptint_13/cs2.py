n = int(input())
arr = [input().split() for i in range(n)]
arr1 = []
arr2 = []
arr3 = []
for i in arr:
    arr1.append(i[0])
    arr2.append(int(i[1]))
    arr3.append(int(i[2]))


def partition(array, begin, end):

    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)


for i in arr:
    s=i.pop(0)
    i[0]=-int(i[0])
    i[1]=int(i[1])
    i.insert(2,s)
#quicksort(arr)
#arr.sort(key=lambda arr:(arr[1]), reverse=True)
#for i in arr:
   # print(i[0])
print(arr)
quicksort(arr, begin=0, end=None)
print(arr)
