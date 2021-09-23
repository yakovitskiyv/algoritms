
# неустойчивая
def select_sort(A):
    for i in range(len(A)-1):
        for k in range(i+1, len(A)):
            if A[k] < A[i]:
                A[k], A[i] = A[i], A[k]
    print(A)

select_sort([11, 2, 9, 7, 1])
