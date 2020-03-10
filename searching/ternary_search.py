def ternary_search(arr, l, r, x) :
    mid1 = l + (r - l) // 3
    mid2 = mid1 + (r - l) // 3
    
    if arr[mid1] == x :
        return mid1 
    
    if arr[mid2] == x :
        return mid2
    
    # search element is in left one-third of array
    if x < arr[mid1] :
        return ternary_search(arr, l, mid1 - 1, x)
    # search element is in right one-third of array
    elif x > arr[mid2] :
        return ternary_search(arr, mid2 + 1, r, x)
    # otherwise is in middle one-third array
    else :
        return ternary_search(arr, mid1 + 1, mid2 - 1, x)

    # if not found
    return -1

if __name__ == '__main__' :
    arr = input()
    x = input()
    arr = arr.split(' ')
    arr = [int(i) for i in arr]
    ind = ternary_search(arr, 0, len(arr) - 1, int(x))
    if ind == -1 :
        print('Element', x, 'not present in array')
    else :
        print('Element', x, 'present in array at index', ind)