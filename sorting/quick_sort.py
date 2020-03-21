def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        
        arr = quicksort(arr, low, pivot - 1)
        arr = quicksort(arr, pivot + 1, high)
    
    return arr

def partition(arr, low, high):
    # index of smaller element
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

if __name__ == '__main__' :
    arr = input()
    arr = arr.split(' ')
    arr = [int(i) for i in arr]
    sorted_arr = quicksort(arr, 0, len(arr) - 1)
    print(*sorted_arr)