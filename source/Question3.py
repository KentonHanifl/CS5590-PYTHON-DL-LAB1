pythonStudents = set()
webappStudents = set()

cont = True
while cont:
    choice = input("1)Add students to python\n2)Add students to web application\n3)See common students\n4)See not common students\n5)Quit\n")
    if choice[0]=="1":
        students = input("Enter student names for python with spaces between the names\n").split(" ")
        pythonStudents.update(students)
    elif choice[0]=="2":
        students = input("Enter student names for web application with spaces between the names\n").split(" ")
        webappStudents.update(students)
    elif choice[0]=="3":
        if len(pythonStudents)==0 and len(webappStudents)==0:
            print("both lists empty!")
        elif len(pythonStudents)==0:
            print("python students list empty!")
        elif len(webappStudents)==0:
            print("webapp students list empty!")
        else:
            print(pythonStudents & webappStudents) #the set union between are the students in common
    elif choice[0]=="4":
        if len(pythonStudents)==0 and len(webappStudents)==0:
            print("both lists empty!")
        elif len(pythonStudents)==0:
            print("python students list empty!")
        elif len(webappStudents)==0:
            print("webapp students list empty!")
        else:
            print(pythonStudents ^ webappStudents) #the set difference is the students not in common
    else:
        cont = False
