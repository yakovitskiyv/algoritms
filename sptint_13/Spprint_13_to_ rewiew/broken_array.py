# ID: 53563772


def broken_search(nums, target) -> int:
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = (start + end)//2
        if nums[mid] == target:
            return mid
        if nums[start] <= nums[mid]:
            if target < nums[mid] and target >= nums[start]:
                end = mid-1
            else:
                start = mid+1
        else:
            if target > nums[mid] and target <= nums[end]:
                start = mid+1
            else:
                end = mid-1
    else:
        return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


test()
