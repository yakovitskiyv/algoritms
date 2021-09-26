def merge(arr, lf, mid, rg):
	# Your code
	# “ヽ(´▽｀)ノ”
	pass


def merge_sort(arr, lf, rg):
	# Your code
	# “ヽ(´▽｀)ノ”
	pass


def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0, 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected


import operator
def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
array = [78, 41, 4, 27, 3, 27, 8, 39, 19, 34, 6, 41, 13, 52, 16]
print(merge_sort(array))