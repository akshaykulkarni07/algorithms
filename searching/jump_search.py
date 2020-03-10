import math

def jump_search(arr, x) :
    # we jump m steps at a time in the array until the 
    # search element is lower than the last element of the 
    # sub-array of m elements.
    # Also, sqrt(len(arr)) is the optimum value of m.
    m = math.sqrt(len(arr))
    while arr[int(min(m, len(arr)) - 1)] < x :
        m += math.sqrt(len(arr))

    # once we find the sub-array of m elements containing 
    # the search element, we perform a linear search on it.
    for i in range(int(m - math.sqrt(len(arr))), int(m)) :
        if arr[i] == x : 
            return i
    
    return -1

if __name__ == '__main__' :
    arr = input()
    x = input()
    arr = arr.split(' ')
    arr = [int(i) for i in arr]
    ind = jump_search(arr, int(x))
    if ind == -1 :
        print('Element', x, 'not present in array')
    else :
        print('Element', x, 'present in array at index', ind)