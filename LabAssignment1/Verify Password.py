import re


def valid_password(pwd):

        if len(pwd) < 6 or len(pwd) > 16:
            print("Your Password length should be between 6-16 characters")
        elif re.search('[0-9]', pwd) is None:
            print("Make Sure your Password contains at least one digit")
        elif re.search('[$@!*]', pwd) is None:
            print("Make sure your Password contains at least one of the special characters ($@!*)")
        elif re.search('[A-Z]', pwd) is None:
            print("Make sure your Password has at least one uppercase letter")
        elif re.search("[a-z]", pwd) is None:
            print("Make sure your Password has at least one lowercase letter")
        else:
            print("Strong Password")


p = input("Please Enter your Password: ")
valid_password(p)
