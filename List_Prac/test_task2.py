from task2 import List

def test_str():
    """
    Test the str method
    :return: Test result
    """
    print("Testing str......")
    test_list = List()

    # case 1 : apply the method to an empty list
    return_str = List()
    assert return_str == '', "There is something wrong with __str__ method!"

    # case 2 : apply the method to a list with items in it
    test_list.append("hello")
    test_list.append("I'm Jack")
    return_str = test_list.str()

    input_str = "hello" + "\n" + "I'm Jack"
    assert return_str == input_str, "There is something wrong with __str__ method!"

def test_len():
    """
    Test the len method
    :return: Test result
    """
    print("Testing len......")
    test_list = List()

    # case 1: apply the method to an empty list
    assert len(test_list) == 0, "There is something wrong with __len__ method!"

    # case 2 : apply the method to a list with items in it
    test_list.append(1)
    test_list.append(2)

    assert len(test_list) == 2, "There is something wrong with __len__ method!"

def test_contains():
    """
    Test the contains method
    :return: Test result
    """
    print("Testing contains......")
    test_list = List()

    test_list.append(1)
    test_list.append(2)

    # case 1 : item in the list
    assert 1 in test_list, "1 is not in the list!"
    # case 2 : item not in the list
    assert 3 not in test_list, "3 is not in the list!"

def test_getitem():
    """
    Test the getitem method
    :return: Test result
    """
    print("Testing getitem......")
    test_list = List()

    test_list.append(1)
    test_list.append(2)

    # test case 1: does the method return a correct result
    case_1 = test_list[0]
    assert case_1 == 1, "Getitem method does not work as expect!"

def test_getitem_fail():
    # test case 2: input an index that is out of range
    test_list = List()
    case_2 = test_list[3]



def test_setitem():
    """
    Test the setitem method
    :return: Test result
    """
    print("Testing setitem......")
    test_list = List()

    test_list.append(1)
    test_list.append(2)

    # test case 1: Target item is set to the target position
    test_list[0] = 10
    assert test_list[0] == 10, "Setitem method does not work as expect!"

def test_setitem_fail():
    # test case 2: input an index that is out of range
    test_list = List()
    test_list[3] = 1
    pass


def test_eq():
    """
    Test the eq method
    :return: Test result
    """
    print("Testing eq......")
    test_list_1 = List()
    test_list_1.append(1)

    # test case 1 : compare two equivalent lists

    test_list_2 = List()
    test_list_2.append(1)

    assert test_list_1 == test_list_2, "Eq method does not work as expect!"

    # test case 2: compare two not equivalent lists
    test_list_3 = List()
    test_list_3.append(11)

    assert test_list_1 == test_list_3, "Yes! These two lists are not equivalent!"

def test_append():
    """
    Test the append method
    :return: Test result
    """
    print("Testing append......")
    test_list = List()

    # test case 1: append an item to the list
    test_list.append(1)
    assert test_list[0] == 1, "Append method does not work as expect!"
    assert test_list.count == 1, "Append method does not work as expect!"

    # test case 2: append an item to a full list
    test_list_2 = List()
    for i in range(100):
        test_list_2.append(1)
    test_list_2.append(1)
    print(test_list_2.size)


def test_prepend():
    """
    Test the prepend method
    :return: Test result
    """
    test_list = List()

    # test case 1: prepend an item to the list
    test_list.append(12)
    test_list.prepend(1)
    assert test_list[0] == 1, "Prepend method does not work as expect!"
    assert test_list.count == 2, "Prepend method does not work as expect!"

    # test case 2: prepend an item to a full list
    test_list_2 = List()
    for i in range(50):
        test_list_2.append(1)

    test_list_2.prepend(1)
    print(test_list_2.size)

def test_insert():
    """
    Test the insert method
    :return: Test result
    """
    print("Testing insert......")
    test_list = List()

    # test case 1: insert an item to the list
    test_list.append(12)
    test_list.append(2)
    test_list.insert(1,100)
    assert test_list[1] == 100, "Insert method does not work as expect!"
    assert test_list.count == 3, "Insert method does not work as expect!"

    # test case 2: Insert an item to a full list
    test_list_2 = List()
    for i in range(100):
        test_list_2.append(1)

    test_list_2.insert(1,100)
    print(test_list_2.size)

def test_remove():
    """
    Test the remove method
    :return: Test result
    """
    print("Testing remove......")
    test_list = List()

    # case 1: remove an item from the list
    test_list.append(1)
    test_list.append(2)
    test_list.append(3)

    test_list.remove(2)
    assert 2 not in test_list, "Remove method does not work well"
    assert test_list.count == 2, "Remove method does not work well"

def test_remove_fail():
    # case 2: remove an item that is not in the list
    test_list = List()

    test_list.append(1)
    test_list.append(2)
    test_list.append(3)
    test_list.remove(100)

def test_delete():
    """
    Test the delete method
    :return: Test result
    """
    print("Testing delete......")
    test_list = List()

    # case 1: delete an item from the list
    test_list.append(1)
    test_list.append(2)
    test_list.append(3)

    test_list.delete(2)
    assert 3 not in test_list, "Delete method does not work well"
    assert test_list.count == 2, "Delete method does not work well"

def test_delete_fail():
    # case 2: Index out of range
    test_list = List()

    test_list.append(1)
    test_list.append(2)
    test_list.append(3)
    test_list.delete(100)





if __name__ == "__main__":

    try:
        test_str()
    except AssertionError:
        pass
    try:
        test_len()
    except AssertionError:
        pass
    try:
        test_contains()
    except AssertionError:
        pass
    try:
        test_getitem()
    except:
        pass
    try:
        test_getitem_fail()
    except AssertionError:
        pass
    try:
        test_setitem()
    except:
        pass
    try:
        test_setitem_fail()
    except AssertionError:
        pass
    try:
        test_eq()
    except AssertionError:
        pass
    try:
        test_append()
    except:
        pass
    try:
        test_prepend()
    except:
        pass
    try:
        test_insert()
    except:
        pass
    try:
        test_remove()
    except:
        pass
    try:
        test_remove_fail()
    except AssertionError:
        pass
    try:
        test_delete()
    except:
        pass
    try:
        test_delete_fail()
    except AssertionError:
        pass