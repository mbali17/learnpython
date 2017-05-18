import login
from statistics import mean as m
isAdministrator = login.isAdministrator()
def showApplicationMenu():
    print("Welcome to Grade central")
    print("[1] to Enter Grades")
    print("[2] to Remove Student")
    print("[3] to Student Average grades")
    print("[4] to exit")
    userInput = input("what would you like to do today? (Enter a number) ")
    return int(userInput)
    
if isAdministrator:
    userInput = showApplicationMenu()
    print("The input entered by the user",userInput)
    studentGrades = {}
    while userInput != 4:
        studentName = input("Enter student name: ")
        if userInput == 1:
            studentGrade= input("Enter student grade: ")
            gradeList = []
            if studentName in studentGrades:
                gradeList = studentGrades[studentName]
                gradeList.append(int(studentGrade))
            else:
                gradeList.append(int(studentGrade))
                studentGrades[studentName]=gradeList
            userInput = showApplicationMenu()
        elif userInput == 2:
            #remove student
            print("removing student")
            if studentName in studentGrades:
                del studentGrades[studentName]
            else:
                print("Student with name",studentName,"Not found")
            userInput = showApplicationMenu()
        elif userInput == 3:
            #average student grade
            print("finding student average")
            if studentName in studentGrades:
                gradeList = studentGrades[studentName]
                print(m(gradeList))
            else:
                print("Student with name",studentName,"Not found")
            userInput = showApplicationMenu()
    print("Thanks for using the application")
    print("current state of the database",studentGrades)
else:
    print("Contact administrator only admin users can enter the details")
