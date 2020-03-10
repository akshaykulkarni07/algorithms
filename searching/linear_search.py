def linear_search(arr, x) :
    # go over every element of array until we find the 
    # search element
    for i in range(len(arr)) : 
        if x == arr[i] :
            return i
    
    return -1

if __name__ == '__main__' :
    arr = input()
    x = input()
    arr = arr.split(' ')
    ind = linear_search(arr, x)
    if ind == -1 :
        print('Element', x, 'not present in array')
    else :
        print('Element', x, 'present in array at index', ind)