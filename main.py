Students_Name = ["Name"]
Students_ID = ["ID"]
Students_Password = ["password"]
Students_Grade = ["Grade"]
Students_Attendance = ["Attendance"]
questions = {
    "Which programming language is the best?\na. Python\nb. Java\nc. C": "a",
    "Which programming language is older?\na. Python\nb. Java\nc. C": "c",
    "which PL is the best for web?\na. JavaScript\nb. PHP\nTypeScript": "a"
}


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


def attendance(grade):
    for i in questions:
        print(i)
        answer = input()
        if answer == questions[i]:
            grade += 1
    return grade


def sign_in():
    while True:
        ID = int(input("Enter your ID... "))
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
    Students_Grade[index] = attendance(Students_Grade[index])
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
    while True:
        login = int(input("""
        ##########################
        ##  Choose the option:  ##
        ##      1. Sign up      ##
        ##      2. Sign in      ##
        ##       3. Admin       ##
        ##########################

        Enter the option... """))
        if login == 1:
            sign_up()
        elif login == 2:
            sign_in()
        elif login == 3:
            admin()


if __name__ == '__main__':
    main()
