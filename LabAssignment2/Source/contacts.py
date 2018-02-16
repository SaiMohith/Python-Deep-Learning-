def name(inp):
    c = True
    for contact in contact_list:
        if inp in contact["name"]:
            print("Name: ", contact["name"], "Phone:", contact["phone"], "Email:", contact["email"])
            c = True
            break
        else:
            c = False
    if c is False:
        print("There is no contact with the given name. Please check and try again.")


def number(inp):
    c = True
    for contact in contact_list:
        if int(contact["phone"]) == inp:
            print("Name: ", contact["name"], "Phone:", contact["phone"], "Email:", contact["email"])
            c = True
            break
        else:
            c = False
    if c is False:
        print("There is no contact with given number. Please check and try again.")


def edit(inp):
    c = True
    for contact in contact_list:
        if inp in contact["name"]:
            print("Name: ", contact["name"], "Phone:", contact["phone"], "Email:", contact["email"])
            print("1) Edit Name\n""2)Edit Number\n""3)Edit Email\n""4)Exit\n")
            while True:
                new = int(input("Choose what to edit: "))
                if new == 1:
                    new_name = str(input("New Name: "))
                    contact["name"] = new_name
                    print("Name: ", contact["name"], "Phone:", contact["phone"], "Email:", contact["email"])
                elif new == 2:
                    new_number = int(input("New Number: "))
                    contact["phone"] = new_number
                    print("Name: ", contact["name"], "Phone:", contact["phone"], "Email:", contact["email"])
                elif new == 3:
                    new_email = str(input("New Email: "))
                    contact["email"] = new_email
                    print("Name: ", contact["name"], "Phone:", contact["phone"], "Email:", contact["email"])
                elif new == 4:
                    break
                else:
                    print("Invalid Response")
            c = True
            break
        else:
            c = False
    if c is False:
        print("There is no contact with the given name. Please check and try again.")


def start():
    while True:
        print("\na)Display contact by name \n"
              "b)Display contact by number \n"
              "c)Edit contact by name \n"
              "d)Exit \n")
        ch = str(input("Choose one: "))
        if ch == 'a':
            n = str(input("Please enter the name: "))
            name(n)
        elif ch == 'b':
            n = int(input("please enter the number:"))
            number(n)
        elif ch == 'c':
            n = str(input("Please enter the name to edit the contact:"))
            edit(n)
        elif ch == 'd':
            exit()
        else:
            print("please choose from the given options")


contact_list = [{"name": "Uma", "phone": "910529", "email": "dad@gmail.com"},
                {"name": "Srinivasa", "phone": "910210", "email": "mom@gmail.com"},
                {"name": "Sumanth", "phone": "910928", "email": "bro@gmail.com"},
                {"name": "Mohith", "phone": "111214", "email": "mohith@gmail.com"}]


start()
