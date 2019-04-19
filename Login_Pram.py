def csv2dict(fileName, keyIndex=0, valueIndex=1):
    import os
    if os.path.exists(fileName) == False:
        import csv
        with open(fileName, "w", newline="") as f:
            tmp = csv.writer(f, delimiter=",")
#            tmp.writerow([])
    dataDict = {}
    import csv
    with open(fileName, "r") as csvFile:
        tmp = csv.reader(csvFile, delimiter=",")
        for row in tmp:
            dataDict[row[keyIndex]] = row[valueIndex]
    return dataDict

#        dataLine = csvFile.readline().strip("\n")
#        while dataLine != "":
#            tmpList = dataLine.split(",")
#            print(tmpList)
#            dataDict[tmpList[keyIndex]] = tmpList[valueIndex]
#            print(dataDict)
#            dataLine = csvFile.readline().strip("\n")
#    return dataDict


def dict2csv(file, dict):
    import csv
    with open(file, "w", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        for k, v in dict.items():
            csvWriter.writerow([k, v])

def regist_account():
     question = input("Do you want to regist an account? Please answer \"yes\" or \"no\":")
     answer = question.lower()
     if answer == "yes":
        user = input("Please input username:")
        temp = csv2dict("user_passwd.csv")
        if user not in temp:
            passwd = input("Please input the password:")
            temp[user] = passwd
            dict2csv("user_passwd.csv", temp)
            print("Regist sucessfull !")
        else:
            print("The account is exist! Please tye another")
     elif answer == "no":
        print("Bye Bye! Have a joy day!")
     else:
        print("The answer must be \"yes\" or \"no\",please try again.")

def check_user_passwd():
    user_passwd = csv2dict("user_passwd.csv")
    user = input("Please input username:")
    if user in user_passwd:
        passwd = input("Please input the password:")
        if passwd == user_passwd[user]:
            print("欢迎来到公牛集群OA办公平台！")
        else:
            print("The password is wrong! please try again.")
    else:
        print("The username not exist! please try again.")

def login_oa():
    question = input("Do you have an account? Please answer \"yes\" or \"no\":")
    answer = question.lower()
    if answer == "yes":
        check_user_passwd()
    elif answer == "no":
        regist_account()
    else:
        print("The answer must be \"yes\" or \"no\",please try again.")
login_oa()
