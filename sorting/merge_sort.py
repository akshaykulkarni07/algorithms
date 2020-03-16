def merge_sort(arr) :
    # do following operations only for 
    # arrays with 2 or more elements
    if len(arr) > 1 :
        # finding middle position
        mid = len(arr) // 2
        # splitting into left and right half arrays
        l_arr = arr[ : mid]
        r_arr = arr[mid : ]
        # recursively call merge_sort on left 
        # and right arrays
        merge_sort(l_arr)
        merge_sort(r_arr)
        # merge the sorted half arrays
        merge(arr, l_arr, r_arr)
    
    return arr

def merge(arr, l_arr, r_arr) :
    # initialize counters for merged array and the 
    # two half arrays
    i = j = k = 0
    # iterate over the 2 half arrays at the same time
    while i < len(l_arr) and j < len(r_arr) :
        # if left array has smaller element, put it 
        # into the future merged array and increment
        # the left counter
        if l_arr[i] < r_arr[j] :
            arr[k] = l_arr[i]
            i += 1
        # otherwise put the right array element in the 
        # future merged array and increment it's counter
        else :
            arr[k] = r_arr[j]
            j += 1
        # increment the merged array counter
        k += 1
    
    # in case right array finishes first in the last
    # loop, then left array elements left are put into 
    # the merged array
    while i < len(l_arr) :
        arr[k] = l_arr[i]
        i += 1
        k += 1
    
    # similarly, if left array finishes first, then 
    # right array elements are put into the merged array
    while j < len(r_arr) :
        arr[k] = r_arr[j]
        j += 1
        k += 1

if __name__ == '__main__' :
    arr = input()
    arr = arr.split(' ')
    arr = [int(i) for i in arr]
    sorted_arr = merge_sort(arr)
    print(*sorted_arr)