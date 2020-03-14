def bubble_sort(arr) :
    # making at most len(arr) number of passes
    # of comparisons
    for i in range(len(arr)) :
        swapped = False
        # iterating over the array upto the 'i'th element
        # from the end, because the last 'i' elements
        # will be sorted (because of the algorithm)
        for j in range(len(arr) - i - 1) :
            # swapping 2 consecutive elements if next one is 
            # smaller than previous one
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # if no swaps occurred in current iteration, then 
        # array is already sorted, so return sorted array
        if not swapped :
            return arr

    return arr

if __name__ == '__main__' :
    arr = input()
    arr = arr.split(' ')
    arr = [int(i) for i in arr]
    sorted_arr = bubble_sort(arr)
    print(*sorted_arr)