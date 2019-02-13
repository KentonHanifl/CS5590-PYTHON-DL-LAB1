
# This program was done by Syed M Rahman.
# This program computes the net amount of a bank account based a transaction log from console input.


# the variable below is the net bank balance amount. It is initialized to zero when the program is first executed.
bank_balance=float(0.00)

# Implementing a while loop that will execute the expressions & statements within the while body until
# the break statement terminates this indefinite loop
while True:

    # The user is asked to enter a transaction type(deposit or withdrawl) and an amount
    # The values are then stored in a string
    usr_input = input("Enter transaction type and amount: ")



    # The split method is used to split the string into list items i.e. the sring "Deposi 300" is separated into 2 items: Deposit and 300
    transaction = usr_input.split()

    #The If condition executes if the first letter of list item of the string user entered is either D or d
    if (usr_input[0] == 'D' or usr_input[0] == 'd'):
        # the second list item from the string is type casted into a float number and is assigned to a variable called credit
        credit = float(transaction[1])

        #Here the float value of the variable credit is added to the value of the variable bank_balance at which point it updates the new value
        #of the variable bank_balance
        bank_balance += credit

    #the Else If statement executes if the first letter of list item of the string user entered is either W or w
    elif (usr_input[0] == 'W' or usr_input[0] == 'w'):
        # the second list item from the string is type casted into a float number and is assigned to a variable called debit
        debit = float(transaction[1])

        # Here the float value of the variable debit is subtracted from the value of the variable bank_balance at which point it updates the new
        # value of the variable bank_balance
        bank_balance -= debit

        # This while loop goes into effect when the bank balance goes under zero and keeps asking the user to enter
        # an amount that will bring the bank balance above zero
        while (bank_balance < 0.00):
            print("Your bank balance is below zero. Please make a deposit immediately to avoid overdraft charges!")
            #shows the current negative bank balance
            print("The current balance is:", bank_balance)

            #User is asked an to enter an amount to bring the bank amount above 0.
            #The string value user enters is type casted into a float value
            pos_balance = float(input("Enter a deposit amount that will bring you bank balance above zero: "))

            #float value variable is added bank_balance variable and updates the new value of variable bank_balance
            bank_balance += pos_balance

            #once the bank balance is zero or above it executes the if the statement and prints the statement
            if (bank_balance >= 0.00):
                print("You now have a positive balance!")

    #The user is asked if they wish to make another transaction
    usr_input2 = input("Would you like to make another deposit or withdrawl? (Press Y or y for yes or Press any key for no): ")

    # The not operator will return True if the expression is false. So, when the user enters anything other than Y or y
    # the expression becomes false and thus breaks the loop. But if the user enters Y or y then the expression becomes true and the
    # while loop continues as the if not statement does not return True
    if not (usr_input2[0] == 'Y' or usr_input2[0] == 'y'):

        break


# Prints the updated bank balance
print("Your current Bank Balance is:", bank_balance)

