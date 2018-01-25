import re

def strnum(string):
'''Function to extract int and float from strings'''
    lst=re.findall('[0-9]+[0-9.]*',string)
    total=0.0
    if len(lst)>0:
        for num in lst:
            total+=float(num)
    return total    

def add(*args):
'''The add all function'''
    total=0
    for item in args:
        if item is None:
            continue
        elif type(item) is str:
            total+=strnum(item)
        elif type(item) is list:
            total+=add(*item)         # *list to unpack list items
        elif type(item) is dict:
            for key in item.keys():
                total+=add(item[key])
        else:
            total+=item;
    return total

def main():                           # Test Code
    print(add({'a':8,'b':[2,4,'Roll No. 21']}))

if __name__ == '__main__':            # To use this as a module
    main()
