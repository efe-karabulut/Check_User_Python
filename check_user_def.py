user_1 = {"id": 123124, "name": "ali", "role": "user"}
user_2 = {"id": 123123123124, "name": "cansu", "role": "user"}
user_3 = {"id": 123321124, "name": "ceren", "role": "admin"}
user_4 = {"id": 1231214, "name": "ceren", "role": "user"}
user_5 = {"id": 123125514, "name": "ceren", "role": "user"}
user_6 = {"id": 12311232312, "name": "efe", "role": "admin"}

db = [user_1, user_2, user_3, user_4, user_5, user_6]


def checkFlag(string=""):
    strArray = string.split()
    if string.__contains__("-r"):
        targetUser = strArray[0]
        targetRole = strArray[2]
        return {"name": targetUser, "role": targetRole}
    else:
        return False


def getInput():
    userInput = input("Please enter ID or NAME: ")
    isFlag = checkFlag(userInput)
    if isFlag == False:
        return checkUser({"name": userInput})
    if isFlag != False:
        return checkUser(isFlag)


def checkUser(args):
    foundUser = []
    userRole = args.get("role")
    for user in db:
        isName = user["name"]
        isRole = user["role"]
        if args["name"].isdigit():
            isName = str(user["id"])

        if userRole != None:
            if args["name"] == isName and args["role"] == isRole:
                foundUser.append(user)
        if userRole == None:
            if args["name"] == isName:
                foundUser.append(user)

    else:
        text = "Found User"
        if len(foundUser) > 1:
            text = "Found Users"
        if len(foundUser) < 1:
            print("No such user found. Please check again!")
        else:
            print(text, foundUser)


# Invoke Function
getInput()
