'''
Exception handling in python is done using the try and except blocks.
The code after an exception occurs continues to execute normally.
We can have a stack of custom exception followed by generic exception.
'''
def sampleFunc():
    try:
        y='5'+5
        #The following code is not execute as exception occurred in the previous
        #line
        print("is this printed")
    except TypeError as t:
        print("type error triggered")
        print(str(t))
    except Exception as e:
        print('generic exception triggered')

    print('out side try and except')
sampleFunc()
