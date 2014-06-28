import csv

def csvSingle(inputString,index):
    """parse csv string. return string of specified index position.
       check string length for out of list bounds error tolerance.
       if index is at least on less than the length of input string.
       
       usage: >>> csvSingle('one,two,three,"four,five",six, seven', 0)
       will return: "one" which is the 0th element of the string
    """
    try:
        checkString = len(inputString) -1
        if index < checkString:
            csv_reader = csv.reader( [inputString] )
            fields = None
            for row in csv_reader:
                fields = row
            print( fields[index] )
    except IndexError:
        print("You have specified index: <", index, "> :which exceeds the range of the string: IndexError") 
