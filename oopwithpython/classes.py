'''
    Classes are used to structure the program and __init__ is the first
    method that is invoked when the object of the class is created.
    A class consists of three enities 
        Class data attributes
        object data attributes 
        Methods

'''
class program():
    #Class variables are declared with a class scope and can be acessed with
    #the class name directly: Following is the class data attributes 
    isProductionReady = True;
    #This is the method invoked when the object is created and
    #This can contain initial setiting or the default value of the object
    #self is the accessor to the object.
    #args are formal arguments to the constructor and kwargs are the keyword
    #arguments for example age='12' or height=5.1.
    def __init__(self,*args,**kwargs):
        #defining certain properties using the object if the properties are
        #not to be referenced then we don't need to use the self pointer.
        self.lang = input("what is the language: ")
        #converting the user input to float value.
        self.version = float(input("What is the version of the language: "))
        self.skillLevel = input("What is the skill level: ")
    #defining a method in python is same as defining a function but the deffirence
    # is that the class method/ instance method take a special param called the self as the 
    # first parmeter.The name could be anything but it is a standard to use self.
    #https://stackoverflow.com/questions/21694901/difference-between-python-self-and-java-this
    def currentStatus(self):
        prefix= 'The program is written in \t'
        return prefix +"lang:"+ self.lang + "\t version: "+str(self.version);
#creating an object.
p1 = program();
print("Language : ",p1.lang)
print("version : ",p1.version)
print("skill level :",p1.skillLevel)
#method invocation.
print('currentStatus: ',p1.currentStatus())
#Accessing class variables
print("isProductionReady",program.isProductionReady)
