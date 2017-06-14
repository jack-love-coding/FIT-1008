from task5 import Editor


def test_read():
    """
    To test command_read method
    :return: Test result
    """
    # test case 1: read a file into editor
    print("Testing read......")
    test_case_1 = Editor()
    test_case_1.command_read('text.txt')

    assert test_case_1 is not None, "Read method does not work as expect!"
    print("Test 1 succeed!")

def test_read_fail():

    # test case 2 : read a file that does not exist
    test_case_2 = Editor()
    test_case_2.command_read('N/A.text')


def test_insert():
    """
    To test command_insert method
    :return: Test result
    """
    print("Testing insert......")
    test_case = Editor()

    # test case 1: insert a text into the list
    test_case.command_read('text.txt')
    test_case.command_insert(1)
    assert test_case.list[1] == 'hello', "Insert method does not work as expect!"
    test_case.command_print('')

def test_insert_fail():
    # test cast 2 : index out of range
    test_case = Editor()
    test_case.command_insert(100)

def test_print():
    """
    To test command_print method
    :return: Test result
    """
    print("Testing print......")
    test_case = Editor()

    # test case 1: print a line of text in the editor
    test_case.command_read('text.txt')
    try:
        test_case.command_print(0)
    except:
        print("method does not work as expect!")

def test_print_fail():
    # test case 2: index out of range
    test_case = Editor()
    test_case.command_print(100)

def test_delete():
    """
    To test command_delete method
    :return: Test result
    """
    print("Testing delete......")
    test_case = Editor()

    # case 1 : delete a line of text in the editor
    test_case.command_read('text.txt')
    origin_text = test_case.list[0]
    test_case.command_delete('0')
    final_text = test_case.list[0]

    assert origin_text != final_text, "Delete method does not work!"

def test_delete_fail():
    # case 2 : index out of range]
    test_case = Editor()
    test_case.command_delete(100)


def test_search():
    """
    To test command_search method
    :return: Test result
    """
    print("Testing search......")
    test_case = Editor()

    # case 1: search a word that is in the file
    test_case.command_read('text.txt')
    test_case.command_search('love')

    # case 2 : search a word that is not in the file
    test_case.command_read('text.txt')
    test_case.command_search('hahahaha')


def test_count():
    """
    To test command_count method
    :return: Test result
    """
    print("Testing count......")
    test_case = Editor()

    # case 1: count an empty list
    test_case.command_count()

    # case 2: count a file
    test_case.command_read('text.txt')
    test_case.command_count()


def test_menu():
    """
    To test menu method
    :return: Test result
    """
    test_case = Editor()
    try:
        test_case.menu()
        pass
    except:
        print("Menu method does not work as expect!")

if __name__ == '__main__':
    try:
        test_read()
    except AssertionError:
        pass
    try:
        test_read_fail()
    except FileNotFoundError:
        pass
    try:
        test_insert()
    except AssertionError:
        pass
    try:
        test_insert_fail()
    except AssertionError:
        pass
    try:
        test_print()
    except AssertionError:
        pass
    try:
        test_print_fail()
    except AssertionError:
        pass
    try:
        test_delete()
    except AssertionError:
        pass
    try:
        test_delete_fail()
    except AssertionError:
        pass
    try:
        test_search()
    except AssertionError:
        pass
    try:
        test_count()
    except AssertionError:
        pass
    try:
        test_menu()
    except:
        pass