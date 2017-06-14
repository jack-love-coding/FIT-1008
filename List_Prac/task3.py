from task2 import List

def import_file(filename):
    """
    Function to read a file into a list
    :param filename: the name of the file
    :precondition: a file ready to read
    :postcondition: the file is read into the list
    :return: a list whose content is elements of the file
    """
    #target_file = input("Please enter the file name: ")
    target_list = List()

    open_file = open(filename,'r')

    for line in open_file:
        target_list.append(line.rstrip())

    open_file.close()

    return target_list
