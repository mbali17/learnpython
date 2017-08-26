adminUsers = {"admin":"admin","user1":"password" }

def isAdministrator():
    userName = input("Enter UserName: ")
    try:
        storedPassword=adminUsers[userName]
        password = input("Enter Password: ")
        if storedPassword == password:
            return True
        else:
            return False
    except KeyError as k:
        print("User name does not exist")
        print(str(k))
        return False
    except Exception as e:
        print("Some exception occurred")
        print(str(e))
        return False
