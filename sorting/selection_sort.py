def selection_sort(arr) :
    # iterate over all elements of array
    for i in range(len(arr)) :
        min_idx = i
        # iterate over elements after current element and check
        # if that element is smaller than current element
        # and update the minimum index if yes
        for j in range(i + 1, len(arr)) :
            if arr[j] < arr[min_idx] :
                min_idx = j

        # swap the current element and minimum index element
        # so that lowest possible number comes to the 
        # current element. After all iterations, array will be sorted.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == '__main__' :
    arr = input()
    arr = arr.split(' ')
    arr = [int(i) for i in arr]
    sorted_arr = selection_sort(arr)
    print(*sorted_arr)