class Employee:
    def __init__(self,*args,**kwargs):
        self.firstName = args[0]
        self.lastName = args[1]
        self.age = args[2]
    #defining class methods.If you observe the first param is self defining it is class method.
    def getAge(self):
        return self.age
    def incrementAge(self,ageToIncrement):
        return self.age+ageToIncrement    
    # def someFunc():
    #     print("Some value on the terminal")      
def main():
    emp = Employee('John','hoppkins',22)
    print('*'*5,"Welcome to the employee database",'*'*5)
    print("first Name:",emp.firstName)
    print("last Name:",emp.lastName)
    print("Age:",emp.age)
    print("getAge:",emp.getAge())
    #If you observe the self parameter is not passed by the user.It is automatically 
    # contains the reference to the current object.
    print("incrementAge:",emp.incrementAge(5))
    # emp.someFunc()
main()
    
