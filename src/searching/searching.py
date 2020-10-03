# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Base case
    if end >= start:
        middle = start + (end - start) // 2

        # check if target is present in middle
        if arr[middle] == target:
            return middle

        # target is smaller than the middle, element is present on left side
        elif arr[middle] > target:
            return binary_search(arr, target, start, middle - 1)

        # else, the element is present on the right side
        else:
            return binary_search(arr, target, middle + 1, end)

    else:
        return - 1  # target not present in array

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


# def agnostic_binary_search(arr, target):
#     # Your code here
