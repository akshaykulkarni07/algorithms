def insertion_sort(arr) :
    # iterate over all elements
    for i in range(len(arr)) :
        # store current variable in temporary variable
        curr = arr[i]
        j = i - 1
        # set j to element just before current one.
        # Iterate backwards over auxiliaryly sorted elements
        # until current element is larger 
        while j >= 0 and curr < arr[j] :
            # shift the elements one place to the right
            # to accomodate for smaller element insertion
            arr[j + 1] = arr[j]
            j -= 1
        # insert current element
        arr[j + 1] = curr
    
    return arr

if __name__ == '__main__' :
    arr = input()
    arr = arr.split(' ')
    arr = [int(i) for i in arr]
    sorted_arr = insertion_sort(arr)
    print(*sorted_arr)