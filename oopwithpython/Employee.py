class Employee:
    def __init__(self,*args,**kwargs):
        self.firstName = args[0]
        self.lastName = args[1]
        self.age = args[2]
                
def main():
    emp = Employee('John','hoppkins','22');
    print('*'*5,"Welcome to the employee database",'*'*5)
    print("first Name:",emp.firstName)
    print("last Name:",emp.lastName)
    print("Age:",emp.age)
main()
    
