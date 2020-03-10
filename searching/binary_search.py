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