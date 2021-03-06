class LinearProbeTable:
    """
    A class that implement a complete version of a hash table using Linear Probing to resolve collisions
    """

    def __init__(self, size = 10000):
        """
        Construction function that initialize an instance of class LinearProbeTable
        """
        self.count = 0      # how many items have been stored
        self.array = [None] * size  # the array to store items
        self.table_size = size  # size of the underlying array, a prime

    def __len__(self):
        """
        Returns the length of the hash table. Called by len(self)
        :precondition: The instance of LinearProbeTable exists.
        :postcondition: The length of the instance is calculated.
        :return: The length of the list.
        :complexity: O(1)
        """
        return self.count

    def hash(self, key):
        """
        Return the hash value of a key using universal hash algorithm.
        :precondition: The key is able to be hashed and the value of hashing will not over the size of the hash table
        :postcondition: The key inputed is hashed and a hash value is returned.
        :return: The hash value of a key.
        :complexity: O(key)
        """
        value = 0
        a = 31415
        b = 1
        for i in range(len(key)):
            value = (ord(key[i]) + a * value) % self.table_size
            a = a * b % (self.table_size - 1)
        return value

    def __getitem__(self, key):
        """
        To get item in the LinearProbeTable instance according to the given key.
        :precondition: The instance of Table exists.
        :postcondition: The target item is returned if it is in the list.
        :param key: An index to mark the position of an item.
        :return: Returns the item with matching key in the table
        :complexity: O(1) for best cases, O(key) for worst cases
        """
        position = self.hash(key)
        for i in range(self.table_size):
            if self.array[position] is None:
                raise KeyError(key)
            elif self.array[position][0] == key:
                return self.array[position][1]
            else:
                position =  (position + 1) % self.table_size
        # raises an KeyError if item relate to the key is not in the table
        raise KeyError(key)

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
                self.array[position] = (key, data)
                self.count += 1
                return
            elif self.array[position][0] == key:
                self.array[position] = (key, data)
                return
            else:
                position = (position + 1) % self.table_size
        # raises an IndexError if the table is already full
        raise IndexError("The hash table is full!")

    def __contains__(self, item):
        """
        To determine whether the item is in the table
        :param item: The item that need to be determined that if it is in the table
        :return: True if item is in the table; else False
        :complexity: O(1) in best case, O(N) in worst case
        """
        for i in range(self.table_size):
            if self.array[i] is not None:
                if self.array[i][1] == item:
                    return True
        return False
