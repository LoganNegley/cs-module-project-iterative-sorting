def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
arr = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    found = False
    while end >= start and not found:
        mid = (end + start) // 2
        if arr[mid] == target:
            found = True
            return arr.index(arr[mid])
        else:
            if arr[mid] > target:
                end = mid - 1
            if arr[mid] < target:
                start = mid + 1
    return -1  # not found

binary_search(arr, 8)