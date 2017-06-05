class program():
    #This is the method invoked when the object is created and
    #This can contain initial setiting or the default value of the object
    #self is the accessor to the object.
    def __init__(self,*args,**kwargs):
        #defining certain properties using the object if the properties are
        #not to be referenced then we don't need to use the self pointer.
        self.lang = input("what is the language: ")
        #converting the user input to float value.
        self.version = float(input("What is the version of the language: "))
        self.skillLevel = input("What is the skill level: ")
    #if self is not passed then a typeError is thrown refer the following for
    #more info
    #https://stackoverflow.com/questions/18884782/typeerror-worker-takes-0-positional-arguments-but-1-was-given
    def upgrade(self):
        #this  variable is not part of the object
        new_version = input("What is the version to be updated: ")
        print("version updated for:",self.lang);
        self.version = new_version;
#creating an object.
p1 = program()
print("Language : ",p1.lang)
print("version : ",p1.version)
print("skill level :",p1.skillLevel)
#invoking custom method.
p1.upgrade()
