from Task1 import LinearProbeTable
import timeit



if __name__ == '__main__':

    # "The main function to test time consumed for each combination of the values for table size and b"


    lst_file = ['english_small.txt', 'english_large.txt', 'french.txt']
    lst_b = [1, 27183, 250726]
    lst_table_size = [250727, 402221, 1000081]

    for file in lst_file:
        for b in lst_b:
            for size in lst_table_size:
                if (b+1) != size:
                    class LinearProbeTable_with_b(LinearProbeTable):
                        def __init__(self,size):
                            super(LinearProbeTable_with_b, self).__init__(size)
                            self.b = b
                    # test time consumed for each combination of the values for table size and b
                    inputfile = open(file,'r')
                    hash_table = LinearProbeTable_with_b(size)
                    start = timeit.default_timer()
                    for item in inputfile:
                        hash_table[item] = item
                    end = (timeit.default_timer()-start)
                    inputfile.close()
                    print("The time consumed for " + str(file) + " of b = "+str(b)+" and size = "+ str(size) + " is " + str(end))

