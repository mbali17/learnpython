writeMe = "Some sample text"
'''
to open a file in python we use the open function which accepts the filename
and the mode in which the file is to be opened.If the file exists then the
existing file is openened otherwise a new file is created in the mode passed.
The mode can be either write(w) or append(a). where write overwrites the file contents
and append, appends to the existing content.
'''
fileToWrite = open("examplefilewrite.txt","a")
fileToWrite.write(writeMe)
#This is an important step which signifies that the operation with the file is
#complete.
fileToWrite.close()
