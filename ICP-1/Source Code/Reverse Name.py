print("Please Enter the First Name and Last Name of the user:")
FirstName = input("Enter the First Name: ") #Reads the firtname entered by user
LastName = input("Enter the Last Name: ") #Reads the lastname entered by user
RFN = ''.join(list(reversed(FirstName))) #Reverse the firstname
RLN = ''.join(list(reversed(LastName))) #Reverse the lastname
print(RLN + RFN) #prints the firstname and lastname combined
