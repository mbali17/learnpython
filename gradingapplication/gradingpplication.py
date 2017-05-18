import login
from statistics import mean as m
studentGrades = {}
#shows the application menu
def showApplicationMenu():
   ''' print("Welcome to Grade central")
    print("[1] to Enter Grades")
    print("[2] to Remove Student")
    print("[3] to Student Average grades")
    print("[4] to exit")'''
    #instead of having multiple print statements we can have one single
    #multiline print
   print('''
        Welcome to Grade central
        print("[1] to Enter Grades")
        print("[2] to Remove Student")
        print("[3] to Student Average grades")
        print("[4] to exit
    ''')
   userInput = input("what would you like to do today? (Enter a number) ")
   return int(userInput)
#allows to enter grades for an student
def enterGrades():
    print("entering grades")
    studentName = input("Enter student name: ")
    studentGrade= input("Enter student grade: ")
    gradeList = []
    if studentName in studentGrades:
        studentGrades[studentName].append(int(studentGrade))
    else:
        gradeList.append(int(studentGrade))
        studentGrades[studentName]=gradeList
    print("After Insertion",studentGrades)

#remove grades for a given student                                          
def removeGrades():
    print("removing student")
    studentName = input("Enter student name: ")
    if studentName in studentGrades:
        del studentGrades[studentName]
    else:
        print("Student with name",studentName,"Not found")
    print("After removal",studentGrades)
                                          
#finds average for all  student
def findStudentAverage():
    print("finding student average")
    for eachStudent in studentGrades:
        gradeList = studentGrades[eachStudent]
        average = m(gradeList)
        print(eachStudent,"average is",average)
                                          
#wrap the main logic into main function
def main():
    userInput = showApplicationMenu()
    print("The input entered by the user",userInput) 
    if userInput == 1:    
        enterGrades()
    elif userInput == 2:
        #remove student
        removeGrades()
    elif userInput == 3:
        #average student grade
        findStudentAverage()
    else:
        print("Enter a number between 1-4")
        print("Thanks for using the application")
        print("current state of the database",studentGrades)
        exit()

isAdministrator = login.isAdministrator()
if isAdministrator:
    while True:
        main()
else:
    print("Contact administrator only admin users can enter the details")
