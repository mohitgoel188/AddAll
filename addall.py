import re
def strnum(string):
    lst=re.findall('[0-9]+[0-9.]*',string)
    total=0.0
    if len(lst)>0:
        for num in lst:
            total+=float(num)
    return total    
def add(*args):
    total=0
    for item in args:
        if item is None:
            continue
        elif type(item) is str:
            total+=strnum(item)
        elif type(item) is list:
            total+=add(*item)          # *list to unpack list items
        else:
            total+=item;
    return total
def main():                         
    print(add(1,2,"got 40 and30 al50.1so",4.0,5.9,[1,2,"make",[10,20,"jhone"]]))

if __name__ == '__main__':          # To use this as a module
    main()
