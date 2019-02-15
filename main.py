
maincont = True
while maincont:
    mainchoice = input("\n\nRun which program?\n1)Bank account\n2)Tuples\n3)Students in common\n4)Longest non-repeating substring\n5)Airline Booking Reservation\n6)Website table finder\n7)Quit\n")
    if mainchoice[0] == "1":
        exec(open("Question 1 - Bank Account.py").read())

    elif mainchoice[0] == "2":
        exec(open("Question2 - Tuples.py").read())

    elif mainchoice[0] == "3":
        exec(open("Question3.py").read())

    elif mainchoice[0] == "4":
        exec(open("Question4.py").read())

    elif mainchoice[0] == "5":
        exec(open("Question5.py").read())

    elif mainchoice[0] == "6":
        exec(open("Question6.py").read())


    else:
        maincont = False


                   
