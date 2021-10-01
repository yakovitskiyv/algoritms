# ID: 53709100


from typing import List


def broken_search(nums: List[int], target: int) -> int:
    start: int = 0
    end: int = len(nums)-1
    while start <= end:
        mid = (start + end)//2
        if nums[mid] == target:
            return mid
        if nums[start] <= nums[mid]:
            if nums[mid] > target >= nums[start]:
                end = mid-1
            else:
                start = mid+1
        else:
            if nums[mid] < target <= nums[end]:
                start = mid+1
            else:
                end = mid-1
    return -1


def test():
    arr: List[int] = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


if __name__ == '__main__':
    test()
