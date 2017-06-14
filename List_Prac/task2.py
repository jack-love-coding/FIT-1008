class List:

    """
    A class that implement an array-based list
    """

    def __init__(self):
        """
        Construction function that initialize an instance for class List
        """
        self.base_size = 50
        self.size = self.base_size
        self.the_array = self.size * [0]    # base size = 50 and it can never be less than 50
        self.count = 0      # count: The number of items in the List instance.

    def __str__(self):
        """
        Returns a string representation of the list. Print one item on one line.
        :precondition: A list ready to be printed.
        :postcondition: Items in the list are printed line by lien.
        :return: A string representation of the list.
        """
        index = 0
        return_str = ''
        while index < self.count:
            return_str += str(self.the_array[index])
            return_str += '\n'
            index += 1
        return return_str

    def __len__(self):
        """
        Returns the length of the list. Called by len(self)
        :precondition: The instance of List exists.
        :postcondition: The length of the instance is calculated.
        :return: The length of the list.
        """
        return self.count

    def __contains__(self, item):
        """
        To determine whether an item is in the List instance. Called by 'item in self'.
        :precondition: The instance of List exists and the item is not none.
        :postcondition: Draw the conclusion that if the item is in the list.
        :param item: The target to detect.
        :return: Returns True if item is in the list, False otherwise.
        """
        index = 0
        is_in_list = False
        # Match the item using linear search
        while index < self.count:
            if self.the_array[index] == item:
                is_in_list = True
            index += 1
        return is_in_list

    def __getitem__(self, index):
        """
        To get item in the List instance according to the given index.
        :precondition: The instance of List exists and the index is not out of range.
        :postcondition: The target item is returned if it is in the list.
        :param index: An integer to mark the position of an item.
        :return: Returns the item at index in the list, if index is non-negative. If it is negative, it will return the
        last item if index is −1, the second-to last if index is −2, and so on up to
        minus the length of the list, which returns the first item.
        """
        # Raises an IndexError if index is out of the range from -len(self) to len(self).
        assert -self.count <= index < self.count, "Not a valid index!"
        return self.the_array[index]


    def __setitem__(self, index, item):
        """
        To set value to an item in the List instance according to the given index.
        :precondition: The instance of List exists and the index is not out of range.
        :postcondition: The target item is assigned a value.
        :param index: An integer to mark the position of an item.
        :param item: The value that need to be assigned.
        """
        # Raises an IndexError if index is out of the range from -len(self) to len(self).
        assert -self.count <= index < self.count, "Not a valid index!"
        self.the_array[index] = item

    def __eq__(self, other):
        """
        To determine if this instance is equal to other lists.  Called by self == other.
        :precondition: The instance of List and the 'other' object exist.
        :postcondition: Draw a conclusion that if these two objects are equivalent.
        :param other: Objects that used to compare.
        :return: Returns True if this list is equivalent to other.
        """
        return self.the_array == other

    def append(self, item):
        """
        To add a new item at the end of the List instance.
        :precondition: The instance of List exists and the item to add is not none.
        :postcondition: A item is added to the end of the list.
        :param item: Item to add.
        :return: A list that just add a new item
        """
        # If the list becomes full, it is resized to be 2 times larger than the current size.
        if self.count >= self.size:
            self.size *= 2
            new_array = [None] * self.size
            for i in range(self.count):
                new_array[i] = self.the_array[i]
            self.the_array = new_array
        self.the_array[self.count] = item
        self.count += 1

    def prepend(self, item):
        """
        To add a new item at the start of the List instance.
        :precondition: The instance of List exists and the item to add is not none.
        :postcondition: A item is added to the start of the list.
        :param item: Item to add.
        :return: A list that just add a new item
        """
        # If the list becomes full, it is resized to be 2 times larger than the current size.
        if self.count >= self.size:
            self.size *= 2
            new_array = [None] * self.size
            for i in range(self.count):
                new_array[i] = self.the_array[i]
            self.the_array = new_array
        self.count += 1
        for i in range(self.count-1, 0, -1):
            self.the_array[i] = self.the_array[i-1]
        self.the_array[0] = item

    def insert(self, index, item):
        """
        To insert a item in the position 'index'.
        :precondition: The instance of List exists and the item to add is not none.
        :postcondition: A item is added to the list.
        :param index: An integer to mark the position.
        :param item: Item to insert.
        :return: A list that just add a new item
        """
        # Raises an IndexError if index is out of the range from -len(self) to len(self).
        assert -self.count <= index < self.count, "Not a valid index!"
        # If the list becomes full, it is resized to be 2 times larger than the current size.
        if self.count >= self.size:
            self.size *= 2
            new_array = [None] * self.size
            for i in range(self.count):
                new_array[i] = self.the_array[i]
            self.the_array = new_array
        self.count += 1
        for i in range(self.count-1, index, -1):
            self.the_array[i] = self.the_array[i-1]
        self.the_array[index] = item

    def remove(self, item):
        """
        To delete the first instance of item from the list
        :precondition: The instance of List exists and the item to delete is in the list.
        :postcondition: Target item is removed.
        :param item: Item to delete
        :return: A list just had an item removed from it.
        """

        index = 0
        while index < self.count:
            if self.the_array[index] == item:
                break
            index += 1
        # Raises a ValueError if item does not exist in self
        assert item in self, "Item does not exist!"
        for i in range(index, self.count-1):
            self.the_array[i] = self.the_array[i+1]
        self.count -= 1
        # The underlying size should decrease by half if the underlying array is larger than the base size but the
        # content occupies less than 1/4 of the available space.
        if self.count <= ((1/4)*self.size) and self.size >= (2*self.base_size):
            self.size //= 2
            new_array = [None] * self.size
            for i in range(self.count):
                new_array[i] = self.the_array[i]
            self.the_array = new_array

    def delete(self, index):
        """
        To delete the item at index from the list, moving all items after it towards the start
        of the list.
        :precondition: The instance of List exists and the item to delete is in the list.
        :postcondition: Target item is removed.
        :param index: An integer to mark the position.
        :return: A list just had an item removed from it.
        """
        # Raises an IndexError if index is out of the range from -len(self) to len(self).
        assert -self.count <= index < self.count, "Not a valid index!"

        for i in range(index, self.count-1):
            self.the_array[i] = self.the_array[i+1]
        self.count -= 1
        # The underlying size should decrease by half if the underlying array is larger than the base size but the
        # content occupies less than 1/4 of the available space.
        if self.count <= ((1/4)*self.size) and self.size >= (2*self.base_size):
            self.size //= 2
            new_array = [None] * self.size
            for i in range(self.count):
                new_array[i] = self.the_array[i]
            self.the_array = new_array


if __name__ == '__main__':
    help(List)