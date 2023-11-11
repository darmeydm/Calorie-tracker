
# Online Python - IDE, Editor, Compiler, Interpreter

username = "Tyler"
password = "warhawks13$"

print("Sign in to your account")
print("-----------------------\n")

# get username and password
username_login = input("Enter username: ")
password_login = input("Enter password: ")

# check username/passowrd is correct; ask again if wrong
while username_login != username or password_login != password:

    print("\nERROR! Username or password invalid.")

    username_login = input("\nEnter username: ")
    password_login = input("Enter password: ")


###################### ACCOUNT ######################


print("\n----------------------------------------")
print("|            Welcome  Back!            |")
print("----------------------------------------")

choice = 0    # initialize loop variable

while choice != 4:

    # display menu options
    print("\n MENU OPTIONS")
    print(" ============")
    print(" 1. Change email address")
    print(" 2. Change username")
    print(" 3. Change password")
    print(" 4. Logout\n")

    choice = int(input(" Enter choice (1 - 4): "))

    # input validation: don't accept anything but 1 - 4
    while choice < 1 or choice > 4:
        choice = int(input(" Error! Enter choice (1 - 4): "))

    print("\n----------------------------------------\n")
    
    if choice == 1:
        print(" CHANGE EMAIL ADDRESS")
        print(" ====================\n")

        email = input(" Enter new email: ")     # get email

        # input validation: don't accept email without @
        while "@" not in email:

            email = input(" Error! Email must contain @: ")
        
    elif choice == 2:
        print(" CHANGE USERNAME")
        print(" ===============\n")

        username = input(" Enter new username: ") # get username
        
    elif choice == 3:
        print(" CHANGE PASSWORD")
        print(" ===============\n")

        # display password criteria
        print(" Password Must Contain At Least:")
        print(" ===============================")
        print("  - 8 characters")
        print("  - one letter")
        print("  - one number")
        print("  - one of @ # $ % ^ & *\n")
        
        password = input(" Enter new password: ") # get password

        # input validation - don't accept if doesn't meet above criteria
        isError = True     # True = there is an error
        
        while isError:
            index = 0

            letters = False    # False = no letters
            numbers = False    # False = no numbers
            special = False    # False = no @#$%^&*

            validChar = True   # True = char is letter, digit, or special char

            while index < len(password):    # go thru each char of password

                # get 1 char from password
                char = password[index]  

                if char.isalpha():      # check if letter
                    letters = True

                elif char.isdigit():    # check if digit
                    numbers = True

                elif char in "@#$%^&*": # check if an allowed special char
                    special = True

                else:                   # didn't meet any of the criteria
                    validChar = False

                index += 1

            # display if password is valid or invalid.
            if len(password) >= 8 and validChar and letters and numbers and special:
                isError = False
                
            else:
                print("\n----------------------------------------")

                # display password was invalid
                print("\n{0:^40s}".format(password + " is INVALID."))

                # display what the problem was
                #if validChar:
                if not letters or not numbers or not special or len(password) < 8:
                    print("\n    ================================")
                    print("    |         Must Contain         |")
                    print("    ================================")
                            
                    if len(password) < 8:
                        print("    | - At least 8 characters      |")

                    if not letters:
                        print("    | - At least one LETTER        |")

                    if not numbers:
                        print("    | - At least one NUMBER        |")

                    if not special:
                        print("    | - At least one @ # $ % ^ & * |")

                    print("    ================================")

                if not validChar:                    
                    print("\n    ================================")
                    print("    |       Must ONLY Contain      |")
                    print("    ================================")
                    print("    | - Letters                    |")
                    print("    | - Numbers                    |")
                    print("    | - @ # $ % ^ & *              |")
                    print("    ================================")
                        

                password = input("\n Enter new password: ") # get another password

    else:   # choice 4
        print("           YOU ARE LOGGED OUT           ")
    

    print("\n----------------------------------------")
