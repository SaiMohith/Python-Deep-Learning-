print('Enter two numbers to compute Quotient and Remainder')
First = input("Enter First Number:") #Takes the first number from the user
Second = input("Enter Second Number:") #Takes tne second number from the user
Quotient = int(First) / int(Second) #Quotient is calculated
Remainder = int(First) % int(Second) #Remainder is calculated using modulus
print("Quotient is %f and remainder is %f" % (Quotient, Remainder)) #Prints the output
