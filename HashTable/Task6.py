from Task4 import QuadraticProbeTable

class QuaProForReadFile(QuadraticProbeTable):

    def __setitem__(self, key, data):
        """
        To set value to an item and its key into the hash table instance and can handle collisions
        :precondition: The instance of List exists and has spare space to store items
        :postcondition: The target position is assigned the input data
        :param key: Hash the key to determine which position data should be stored
        :param data: The value that need to be stored.
        :complexity: O(1) in best case, O(N) in worst case
        """
        position = self.hash(key)
        for _ in range(self.table_size):
            if self.array[position] is None:
                self.array[position] = (key, 1)     # If this is the first occurrence of this word, set count to 1
                self.count += 1
                return
            elif self.array[position][0] == key:
                # if this word is already exist in the table, increment the count by 1
                self.array[position] = (key, self.array[position][1]+1)
                return
            else:
                self.collision += 1
                position = (position + (_ + 1) ** 2) % self.table_size
        # raises an IndexError if the table is already full
        raise IndexError("The hash table is full!")

def occurrence_table():
    '''
    Function to construct a table which can be used to look up whether a given word is
    common, uncommon or rare within written English.
    :return: a table which can be used to look up whether a given word is
    common, uncommon or rare within written English
    '''

    inputfile = open('Hamlet.txt','r')
    inputstr = inputfile.read().lower()
    inputfile.close()
    for char in inputstr:
        if char in '!`~@#$%^&*()_+-={}[]|:"<>?.,/;\'':
            inputstr = inputstr.replace(char, ' ')

    inputlist = inputstr.split()

    HashTable = QuaProForReadFile(50000)

    for word in inputlist:

        HashTable[word] = word

    highest_occurrence = 0

    for item in HashTable.array:
        if item is not None:
            if item[1] > highest_occurrence:
                highest_occurrence = item[1]

    lst_common = []
    lst_uncommon = []
    lst_rare = []

    for item in HashTable.array:
        if item is not None:
            if item[1] > highest_occurrence/100 :
                lst_common.append(item[0])
            elif item[1] > highest_occurrence/1000:
                lst_uncommon.append(item[0])
            else:
                lst_rare.append(item[0])

    occur_table = []
    occur_table.append(lst_common)
    occur_table.append(lst_uncommon)
    occur_table.append(lst_rare)
    return occur_table