# This program is check if the password meet certain requirements


import re  # import re library


def valid_password(pwd):  # define a function valid_password

        if len(pwd) < 6 or len(pwd) > 16:  # prints if the input has length less than 6 or high than 16
            print("Your Password length should be between 6-16 characters")
        elif re.search('[0-9]', pwd) is None:  # prints if pwd doesn't have any of digit between 0-9
            print("Make Sure your Password contains at least one digit")
        elif re.search('[$@!*]', pwd) is None:  # prints if pwd doesn't have any of special characters
            print("Make sure your Password contains at least one of the special characters ($@!*)")
        elif re.search('[A-Z]', pwd) is None:  # prints if pwd doesn't have any of letters between A-Z
            print("Make sure your Password has at least one uppercase letter")
        elif re.search("[a-z]", pwd) is None:  # prints if pwd doesn't have any of letters between a-z
            print("Make sure your Password has at least one lowercase letter")
        else:
            print("Strong Password")  # prints if pwd is find


p = input("\n Please Enter your Password: ")  # asks the user to enter the password
valid_password(p)  # calls the function valid_password with user input
