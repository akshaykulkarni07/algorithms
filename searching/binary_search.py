# Recursive implementation of Binary Search
def binary_search_rec(arr, l, r, x) :
    # find the middle element for given left
    # and right indices
    mid = l + (r - l) // 2
    # right index must be larger than the left
    if r >= l :
        # check if search element is the middle element
        if x == arr[mid] :
            return mid
        # if search element is greater than middle element,
        # then it is present in right half
        elif x > arr[mid] :
            return binary_search_rec(arr, mid + 1, r, x)
        # otherwise it is present in left half
        else :
            return binary_search_rec(arr, l, mid - 1, x)
    # if left index becomes less than the right, element 
    # is not present in the array
    else : 
        return -1

# Iterative Implementation of Binary Search
# similar to recursive in logic, just different implementation.
def binary_search_iter(arr, x) :
    l = 0
    r = len(arr) - 1
    while l <= r :
        mid = l + (r - l) // 2 
        if x == arr[mid] :
            return mid 
        elif x < arr[mid] :
            r = mid - 1
        else :
            l = mid + 1
    
    return -1

if __name__ == '__main__' :
    arr = input()
    x = input()
    arr = arr.split(' ')
    arr = [int(i) for i in arr]
    # ind = binary_search_rec(arr, 0, len(arr) - 1, int(x))
    ind = binary_search_iter(arr, int(x))
    if ind == -1 :
        print('Element', x, 'not present in array')
    else :
        print('Element', x, 'present in array at index', ind)