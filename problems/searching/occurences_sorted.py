# Given a sorted array arr[] and a number x, 
# write a function that counts the occurrences 
# of x in arr[]. Expected time complexity is O(Logn).

def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > x:
            r = mid - 1
        elif arr[mid] < x:
            l = mid + 1
        else:
            return mid
    return -1

def occurences(arr, x):
    ind = binary_search(arr, x)
    # if element not found, 0 occurences
    if ind == -1:
        return 0
    
    # since one occurence is already found during
    # binary search, we start count with 1
    count = 1
    
    # counting left side occurences
    j = ind - 1
    while j >= 0 and arr[j] == x:
        count += 1
        j -= 1
    
    # counting right side occurences
    j = ind + 1
    while j < len(arr) and arr[j] == x:
        count += 1
        j += 1
    
    return count

if __name__ == '__main__' :
    arr = input()
    x = input()
    arr = arr.split(' ')
    arr = [int(i) for i in arr]
    print(occurences(arr, int(x)))