# Python program to show that the variables with a value 
# assigned in class declaration, are class variables
#Reference article : http://www.geeksforgeeks.org/g-fact-34-class-or-static-variables-in-python/
# Class for Computer Science Student
class CSStudent:
    #Class variable is shared among all the instance of the class.
    stream = 'cse'#Class  variable.
    '''
        A class variable declared must be assigned value.Otherwise NameError is thrown.
        NameError: name 'someValue' is not defined
    '''
    #someValue
    def __init__(self,name,roll):
        #instance variable: Each instance of the object have their own copy of the instance variable.
        self.name = name
        self.roll = roll
    def someMethod(self):
        #This adds the variable x to the current instance.
        self.x=10;
# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)
a.someMethod()
print(a.x)
#print(CSStudent.someValue)
#Class variable value can also be updated for an instance.
a.stream = 'ECE'
print(a.stream) # prints "cse"
print(b.stream) # prints "cse"
print(a.name) # prints "Geek"
print(b.name) # prints "Nerd"
print(a.roll) # prints "1"
print(b.roll) # prints "2"
#print(b.x)
# Class variables can also be  accessed using class name as well.
print(CSStudent.stream) # prints "cse"
