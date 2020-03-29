# Given an array of integers which is initially 
# increasing and then decreasing, find the maximum 
# value in the array.

# Sorting the array will take O(n logn) and we can
# get the maximum value in O(1), so overall O(n logn)

# simple linear search will give max element in O(n)

# modified binary search will work in O(logn)

def find(arr):
    l = 0
    r = len(arr) - 1
    while l <= r:
        # more stable version of (l + r) // 2
        mid = l + (r - l) // 2
        # if first element is the current element, then 
        # check if it is greater than next element, if it
        # is then it is the largest element i.e. corner case
        # of "no increasing part" 
        if mid == 0:
            if arr[mid] > arr[mid + 1]:
                return mid
        # if last element is the current element, then 
        # check if it is greater than previous element, if it
        # is then it is the largest element i.e. corner case
        # of "no decreasing part"
        elif mid == len(arr) - 1:
            if arr[mid] > arr[mid - 1]:
                return mid
        # if current element is greater than previous and next 
        # elements, then it is the largest element
        elif arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
        # if current element is smaller than previous element, but
        # greater than next element (implies it is in decreasing 
        # sequence), then the middle is to the left
        elif arr[mid] < arr[mid - 1] and arr[mid] > arr[mid + 1]:
            r = mid - 1
        # remaining case is that middle is to the right side 
        # of the current element
        else:
            l = mid + 1
    return -1

if __name__ == '__main__' :
    print('Input an array of integers initially increasing then decreasing: ')
    arr = input()
    arr = arr.split(' ')
    arr = [int(i) for i in arr]
    print(arr[find(arr)])