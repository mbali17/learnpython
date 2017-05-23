#open the file in read mode. and read the contents.
dataRead = open("examplefilewrite.txt","r").read()
print(dataRead)
'''
The data read can be split using the split function or if the file is to be
read line by line then we could use the readlines()
'''
splitData=dataRead.split("\n");
print(splitData)

readline = open("examplefilewrite.txt","r").readlines()
print(readline)
