def board(height, width):  # define a function with arguments as height and width
    print("---" * height)  # print horizontal border
    for i in range(height):  # print the game board
        print("|  " * (width+1))
        print("---" * width)


height_inp = int(input("Enter the Height of the Game Board:"))  # asks user fot the height
width_inp = int(input("Enter the Width of the Game Board:"))  # asks user for the width
print(board(height_inp, width_inp))  # calls the function to print the game board
