class BinarySearchTreeNode:
    '''
    Class to implement a node in BST
    '''

    def __init__(self, key, value=None, left=None, right=None):
        """
        Construction function that initialize an instance of class BinarySearchTreeNode
        """
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        '''
        Return a string that is consist of the key and value of this node
        :return: a string that is consist of the key and value of this node
        '''
        return "{" + str(self.key) + ", " + str(self.value) + "}"


class BinarySearchTree:

    '''
    A class to implement Binary Search Tree
    '''

    def __init__(self):
        """
        Construction function that initialize an instance of class BinarySearchTree
        """
        self.root = None

    def is_empty(self):
        '''
        To test if the tree is empty
        :return: True if the tree is empty
        '''
        return self.root is None

    def insert(self, key, value):
        '''
        Function to insert a node
        :param key: key of the node
        :param value: value of the node
        :return: The BST with new node inserted
        '''
        self.root = self.__addaux(self.root, key, value)

    def __addaux(self, current, newkey, value):
        '''
        auxiliary function to help inserting a node
        :param current: current node in BST
        :param newkey: key of the new node
        :param value: value of the new node
        '''
        if current is None:
            current = BinarySearchTreeNode(newkey, value)
        else:
            if newkey < current.key:
                current.left = self.__addaux(current.left, newkey, value)
            elif newkey > current.key:
                current.right = self.__addaux(current.right, newkey, value)
            else:
                raise ValueError("Duplicate key, can't do yo!")
        return current

    def print_preorder(self):
        '''
        Function to print the free in preoder
        :return:
        '''
        self._print_preorder_aux(self.root)

    def _print_preorder_aux(self, current):
        '''
        auxiliary function to help printing the BST
        :param current: the current node
        :return: print the current node
        '''
        if current is not None:
            print(current, end=" ")
            self._print_preorder_aux(current.left)
            self._print_preorder_aux(current.right)

    def __getitem__(self, key):
        '''
        To search a item in BST
        :param key: key of the target node
        :return:
        '''
        return self._search(key, self.root)

    def _search(self, key, current):
        '''
        auxiliary function to help searching the node
        :param key: key of the target node
        :param current: the current node
        :return:
        '''
        if current is None:
            raise KeyError("Key does not exist")
        elif current.key == key:
            return current.value
        elif key < current.key:
            return self._search(key, current.left)
        else:
            return self._search(key, current.right)

    def __contains__(self, item):
        """
        To determine whether the item is in the BST
        :param item: The item that need to be determined that if it is in the table
        :return: True if item is in the table; else False
        :complexity: O(1) in best case, O(N) in worst case
        """
        try:
            self._search(item, self.root)
        except KeyError:
            return False
        return True







