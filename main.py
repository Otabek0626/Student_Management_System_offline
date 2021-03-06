import json
Students_Name = []
Students_ID = []
Students_Password = []
Students_Grade = []
Students_Attendance = []

                
questions = {}

def open_data():
    with open('Student_Name', 'r') as filehandle:
        for line in filehandle:
            currentPlace = line[:-1]
            Students_Name.append(currentPlace)
    with open('Student_ID', 'r') as filehandle:
        for line in filehandle:
            currentPlace = line[:-1]
            Students_ID.append(currentPlace)
    with open('Student_Password', 'r') as filehandle:
        for line in filehandle:
            currentPlace = line[:-1]
            Students_Password.append(currentPlace)

    with open('Student_Attandance', 'r') as filehandle:
        for line in filehandle:
            currentPlace = line[:-1]
            Students_Attendance.append(currentPlace)

    with open('Student_Grade', 'r') as filehandle:
        for line in filehandle:
            currentPlace = line[:-1]
            Students_Grade.append(currentPlace)


def store_data():
    with open('Student_Name', 'w') as filehandle:
        for listitem in Students_Name:
            filehandle.write('%s\n' % listitem)

    with open('Student_ID', 'w') as filehandle:
        for listitem in Students_ID:
            filehandle.write('%s\n' % listitem)

    with open('Student_Grade', 'w') as filehandle:
        for listitem in Students_Grade:
            filehandle.write('%s\n' % listitem)

    with open('Student_Password', 'w') as filehandle:
        for listitem in Students_Password:
            filehandle.write('%s\n' % listitem)

    with open('Student_Attandance', 'w') as filehandle:
        for listitem in Students_Attendance:
            filehandle.write('%s\n' % listitem)
    
    with open('questions.json', 'w') as fp:
        json.dump(questions, fp, sort_keys=True, indent=4)


def add_question():
    pass    


def sign_up():
    ID = int(input("Enter your Student ID... "))
    password = input("Enter your new password... ")
    while True:
        con_pass = input("Confirm your new password... ")
        if password == con_pass:
            break
        else:
            print("Your password is not confirmed")
            continue
    name = input("Enter your name... ")
    Students_ID.append(ID)
    Students_Password.append(password)
    Students_Name.append(name)
    Students_Grade.append(0)
    Students_Attendance.append("-")





def sign_in():
    while True:
        ID = input("Enter your ID... ")
        password = input("Enter your password... ")
        if ID in Students_ID:
            index = Students_ID.index(ID)
            check = Students_Password[index]
            if check == password:
                print(Students_ID[index], Students_Password[index], Students_Name[index])
                break
            else:
                print("Wrong Password")
                continue
        else:
            print("There is no Data")
            continue
    print(questions)
    grade = 0
    for i in questions:
        print(i)
        answer = input()
        if answer == questions[i]:
            grade += 1
    Students_Grade[index] = grade
    Students_Attendance[index] = "+"


def admin():
    while True:
        id = input("Enter admin ID... ")
        password = input("Enter admin password... ")
        if id == "admin" and password == "adminid":
            for i in range(len(Students_ID)):
                print(i, Students_ID[i], Students_Password[i], Students_Name[i], Students_Grade[i],
                      Students_Attendance[i])
            break
        else:
            print("wrong Password or ID")
            continue


def main():
    open_data()    

    while True:
        login = int(input("""
        ##########################
        ##  Choose the option:  ##
        ##      1. Sign up      ##
        ##      2. Sign in      ##
        ##       3. Admin       ##
        ##        4. Quit       ##
        ##########################

        Enter the option... """))
        if login == 1:
            sign_up()
        elif login == 2:
            
            sign_in()
        elif login == 3:
            admin()
        elif login == 4:
            store_data()
            exit()

if __name__ == '__main__':
    question = json.load(open("questions.json","r"))
    questions = dict(question)
    main()
    
