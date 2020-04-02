def max_heapify(arr, i):
    # left child of node at index i
    left = 2 * i
    # right child of node at index i
    right = 2 * i + 1
    # if left child index is within the array
    # and left child is larger than parent, then
    # update largest variable to left child index
    # else let it be the parent index
    if left < len(arr) and arr[left] > arr[i]:
        largest = left
    else:
        largest = i

    # if right child index is within the array
    # and right child is larger than largest element, 
    # then update largest variable to right child index
    # else let it be the previously set value
    if right < len(arr) and arr[right] > arr[largest]:
        largest = right

    # if parent is not the largest value, then
    # swap the largest element with the parent
    # to satisfy the max heap property
    if not largest == i:
        arr[largest], arr[i] = arr[i], arr[largest]
        # recursively call max_heapify on the swapped
        # element. Since it was modified (swapped),
        # there is a chance that it may have violated
        # the max heap property w.r.t. other nodes
        arr = max_heapify(arr, largest)
    
    return arr

def build_max_heap(arr):
    # in a heap, the elements from n // 2 to the end
    # are leaf nodes. So, apply max_heapify on the 
    # non-leaf nodes i.e. from 0 to n // 2.
    for i in range(len(arr) // 2, -1, -1):
        arr = max_heapify(arr, i)
    return arr

if __name__ == '__main__':
    # arr = [4, 7, 6, 3, 2, 8, 5]
    arr = [1, 4, 3, 7, 8, 9, 10]
    print(build_max_heap(arr))