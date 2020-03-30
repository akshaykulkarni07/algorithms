import sys
sys.path.insert(1, '../data_structures/')
import heap

def heap_sort(arr):
    arr = heap.build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        arr[ : i] = heap.build_max_heap(arr[ : i])        
    return arr

if __name__ == '__main__':
    arr = [4, 7, 9, 3, 2, 8, 5, 1, 6]
    print(heap_sort(arr))