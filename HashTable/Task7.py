import Task6
from Task6 import QuaProForReadFile

def Analyse():
    '''
    Function to analyse and print the percentage of common, uncommon, rare and misspelled words for the given text.
    :return: the percentage of common, uncommon, rare and misspelled words for the given text.
    '''
    reference_table = Task6.occurrence_table()

    inputfile = open('Macbeth.txt','r')
    inputstr = inputfile.read().lower()
    inputfile.close()
    for char in inputstr:
        if char in '!`~@#$%^&*()_+-={}[]|:"<>?.,/;\'':
            inputstr = inputstr.replace(char, ' ')

    inputlist = inputstr.split()

    HashTable = QuaProForReadFile(50000)

    for word in inputlist:

        HashTable[word] = word

    common_count = 0
    uncommon_count = 0
    rare_count = 0
    misspelled_count = 0

    for item in HashTable.array:
        if item is not None:
            if item[0] in reference_table[0]:
                common_count += 1
            elif item[0] in reference_table[1]:
                uncommon_count += 1
            elif item[0] in reference_table[2]:
                rare_count += 1
            else:
                misspelled_count += 1

    common_percent = common_count*100/(common_count + uncommon_count + rare_count + misspelled_count)
    uncommon_percent = uncommon_count *100/(common_count + uncommon_count + rare_count + misspelled_count)
    rare_percent = rare_count *100/(common_count + uncommon_count + rare_count + misspelled_count)
    misspelled_percent = misspelled_count*100/(common_count + uncommon_count + rare_count + misspelled_count)

    print("The percentage of common words is: " + "{0:.0f}%".format(common_percent))
    print("The percentage of uncommon words is: " + "{0:.0f}%".format(uncommon_percent))
    print("The percentage of rare words is: " + "{0:.0f}%".format(rare_percent))
    print("The percentage of misspelled words is: " + "{0:.0f}%".format(misspelled_percent))

if __name__ == '__main__':

    Analyse()