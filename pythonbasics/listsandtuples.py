'''
Tuples are immutable and generally used for sequence unpacking i,e if there are
certain values returned from a function and the values are not to be changed
including the order then we would use the tuple.

Lists are mutable and can be used with any datatype and following operations
can be performed.
    1)append -- appends the value to the end of list
    2)insert-- inserts a value at a given position
    3)sort -- this sorts the given list using either ascending order for numbers
    and alphabetical order for the words
    4)Reverse -- reverses a given list.
    5)remove - removes the given element if there are multiple occurrences of
    the element then the first occurrence is removed.
    6)Count- count the occurrence of a given element
'''
def exampleFunc():
    return 15,12,3
#This is called sequence unpacking.Tuples can be created in 2 ways
#1)Comma separated values 1,32,42
#2)Using the circular braces(1,23.44)
a,b,c = exampleFunc()
print(a)
print(b)
print(c)
#Lists in python are created using square braces.
exList=[22,3,5,66,6,7,7,7,8,4,1]
print(exList)
exList.append(9)
print(exList)
#The following line means insert 44 at the position 5
exList.insert(5,44)
print(exList)
exList.remove(44)
print(exList)
exList.sort()
print(exList)
exList.reverse()
print(exList)
