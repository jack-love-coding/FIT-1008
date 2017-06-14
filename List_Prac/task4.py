from task2 import List
import task3


class Editor:

    """
    A class that implement an UX editor
    """

    def __init__(self):
        """
        Construction function that initialize an instance for class Editor
        """
        self.list = List()

    def command_insert(self, num):
        """
        Insert a line of text into certain position.
        :precondition: A list ready to be inserted.
        :postcondition: New text is inserted into the list.
        :return: The list with new text.
        """

        # raises an exception if no num is given

        try:
            index = int(num)
        except:
            print("?")
            print("Please enter valid position!")
        insert_str = input("Please enter the text you want to insert: ")
        self.list.insert(index,insert_str)

    def command_read(self,filename):
        """
        Read a file to the editor.
        :precondition: There is an existed file to read.
        :postcondition: The file is read into the editor.
        :return: The list of editor whose items are retrieved from the file.
        """
        self.list = task3.import_file(filename)


    def command_write(self, filename):
        """
        Write the content of editor to a file.
        :precondition: No precondition.
        :postcondition: The content of the editor is added to a file.
        :return: The file extended with lines of text which are from the editor.
        """
        # Get the file ready to write
        write_file = open(filename,'w+')
        # Add lines of text in the editor into the file
        write_str = self.list.__str__()
        write_file.write(write_str)

        write_file.close()

    def command_print(self, num):
        """
        Print the texts in the editor.
        :precondition: There is an instance of Editor.
        :postcondition: Texts in the editor are printed out.
        :return: Printing lines of text in the editor.
        """
        # if no num is given prints all the lines
        if num == '':
            print_str = self.list.__str__()
            print(print_str)
        else:
            # if input is not a integer, raise an error
            try:
                index = int(num)
            except:
                print('?')
                print('Please enter a valid position!')
            print_str = self.list[index]
            print(print_str)

    def command_delete(self,num):
        """
        Delete a line of text in a certain position.
        :precondition: The list is not empty.
        :postcondition: The target line of text is deleted.
        :return: The list with a line of text removed.
        """
        #  deletes all the lines if no num is given.
        if num == '':
            self.list = List()
        # if input is not a integer, raise an error
        else:
            try:
                index = int(num)
            except:
                print('?')
                print('Please enter a valid position!')
            self.list.delete(index)

    def command_quit(self):
        """
        Quit the program
        :precondition: Program is still running.
        :postcondition: Program end.
        :return: Program end.
        """
        exit()

    def menu(self):
        """
        Print the menu of commands.
        :return: The menu of commands.
        """
        print('\nMenu: ')
        print('1. insert (num)')
        print('2. read (filename)')
        print('3. write (filename)')
        print('4. print (num)')
        print('5. delete (num)')
        print('6. quit')

        command_str = input("Please enter your command: ")
        command_set = command_str.split(' ', 1) + ['']
        command = command_set[0]
        command_para = command_set[1]
        if command == 'insert':
            self.command_insert(command_para)
        elif command == 'read':
            self.command_read(command_para)
        elif command == 'write':
            self.command_write(command_para)
        elif command == 'print':
            self.command_print(command_para)
        elif command == 'delete':
            self.command_delete(command_para)
        elif command == 'quit':
            self.command_quit()


