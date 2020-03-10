def exp_search(arr, x) :
    # check if first element of array is the search element.
    if arr[0] == x :
        return 0

    # find a power of 2 (say i) such that the search element 
    # is at an index less than that.
    i = 1
    while i < len(arr) and arr[i] <= x :
        i *= 2
    
    # the search element will be between (i // 2) and i 
    # because we already checked upto (i // 2) and search element
    # was less than that.
    return binary_search_rec(arr, i // 2, min(i, len(arr)), x)
    
def binary_search_rec(arr, l, r, x) :
    mid = l + (r - l) // 2
    if r >= l :
        if x == arr[mid] :
            return mid
        elif x > arr[mid] :
            return binary_search_rec(arr, mid + 1, r, x)
        else :
            return binary_search_rec(arr, l, mid - 1, x)
    else : 
        return -1

if __name__ == '__main__' :
    arr = input()
    x = input()
    arr = arr.split(' ')
    arr = [int(i) for i in arr]
    ind = exp_search(arr, int(x))
    if ind == -1 :
        print('Element', x, 'not present in array')
    else :
        print('Element', x, 'present in array at index', ind)