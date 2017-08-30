'''
Exception handling in python is done using the try and except blocks.
The code after an exception occurs continues to execute normally.
We can have a stack of custom exception followed by generic exception.
'''
def sampleFunc():
    try:
        y='5'+5
        #The following code does not execute as exception occurred in the previous line.
        print("is this printed")
    #we can stack all the type of exception starting from  a specific exception moving down to 
    #generic exception.
    except TypeError as t:
        print("type error triggered")
        print(str(t))
    #THis is a  generic exception to accept all kinds of exception.
    except Exception as e:
        print('generic exception triggered')
    #this would be executed as this is outside the try block.If the above code is
    #not wrapped in try except block then this would not be executed.
    print('out side try and except')
sampleFunc()
