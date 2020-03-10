def interpolation_search(arr, low, high, x) :
    # equation gives higher value to position if x is closer to arr[high]
    # and lower value to position if x is closer to arr[low]
    # Rest of the program is similar to binary search
    pos = int(low + ((x - arr[low]) * (high - low) / (arr[high] - arr[low])))
    if x == arr[pos] :
        return pos
    elif x < arr[pos] :
        return interpolation_search(arr, low, pos - 1, x)
    else :
        return interpolation_search(arr, pos + 1, high, x)
    
    return -1

if __name__ == '__main__' :
    arr = input()
    x = input()
    arr = arr.split(' ')
    arr = [int(i) for i in arr]
    ind = interpolation_search(arr, 0, len(arr) - 1, int(x))
    if ind == -1 :
        print('Element', x, 'not present in array')
    else :
        print('Element', x, 'present in array at index', ind)