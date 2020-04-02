import sys
sys.path.insert(1, '../data_structures/')
import heap

def heap_sort(arr):
    # build max heap from given array
    arr = heap.build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        # swap the root element (which will be the largest),
        # with the last element of a shortened array (array
        # shortens at every step of this loop). Consequently,
        # the largest elements go to the end in each step
        arr[0], arr[i] = arr[i], arr[0]
        # since we swapped elements, max heap property may
        # have been violated, so build max heap again with
        # shortened array
        arr[ : i] = heap.build_max_heap(arr[ : i])        
    return arr

if __name__ == '__main__':
    arr = [4, 7, 9, 3, 2, 8, 5, 1, 6]
    print(heap_sort(arr))