# Write an efficient program to find smallest and second smallest element in an array.

# an obvious solution would be to sort the array and take the first 2 elements
# but that would be O(n logn) time complexity

# O(n) time complexity solution (single traversal of array)
# and O(1) space complexity (no auxiliary space requirements)
def find(arr):
    smallest = float('inf')
    second_smallest = float('inf')
    for element in arr:
        if element < second_smallest:
            if element < smallest:
                second_smallest = smallest
                smallest = element
            else:
                second_smallest = element
    return smallest, second_smallest

if __name__ == '__main__' :
    arr = input()
    arr = arr.split(' ')
    arr = [int(i) for i in arr]
    print(find(arr))
