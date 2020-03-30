def max_heapify(arr, i):
    left = 2 * i
    right = 2 * i + 1
    if left < len(arr) and arr[left] > arr[i]:
        largest = left
    else:
        largest = i

    if right < len(arr) and arr[right] > arr[largest]:
        largest = right

    if not largest == i:
        arr[largest], arr[i] = arr[i], arr[largest]
        arr = max_heapify(arr, largest)
    
    return arr

def build_max_heap(arr):
    for i in range(len(arr) // 2, -1, -1):
        arr = max_heapify(arr, i)
    return arr

if __name__ == '__main__':
    # arr = [4, 7, 6, 3, 2, 8, 5]
    arr = [1, 4, 3, 7, 8, 9, 10]
    print(build_max_heap(arr))