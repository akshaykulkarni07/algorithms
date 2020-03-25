class HashTable(object):
    def __init__(self):
        self.table = [None]*255

    def store(self, num):
        '''
        Store the number input in hash table
        '''
        key = self.calculate_hash_value(num)
        if self.table[key]:
            self.table[key].append(num)
        else:
            self.table[key] = [num]

    def lookup(self, num):
        '''Return the hash value if the
        number is already in the table.
        Return -1 otherwise.'''
        key = self.calculate_hash_value(num)
        if self.table[key]:
            return key
        else:
            return -1
    
    def calculate_hash_value(self, num):
        '''Helper function to calulate a
        hash value from a number.'''
        return num % 255

def check_subarray(arr1, arr2):
    table = HashTable()
    for i in range(len(arr1)):
        table.store(arr1[i])

    for j in range(len(arr2)):
        if table.lookup(arr2[j]) == -1:
            return False
    
    return True

if __name__ == '__main__':
    arr1 = input()
    arr2 = input()
    arr1 = arr1.split(' ')
    arr2 = arr2.split(' ')
    arr1 = [int(i) for i in arr1]
    arr2 = [int(i) for i in arr2]
    print(check_subarray(arr1, arr2))