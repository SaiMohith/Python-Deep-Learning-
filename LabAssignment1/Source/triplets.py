# This program is to find the triplets in the given sequence


def triplets(numbers):  # define a function which takes the number sequences as input
    print("\n Given Sequence: ", numbers)  # prints the given input
    l = len(numbers)  # get the length of the list
    t_list = []  # creates a tuple to store the triplets
    for x in range(0, l-2):  # runs for loop until index is l-2
        for y in range(x+1, l-1):  # runs for loop until index is l-1
            for z in range(y+1, l):  # runs for loop until index is l
                if numbers[x] + numbers[y] + numbers[z] == 0:  # if sum is zero append the values to the t_list
                    t_list.append([numbers[x], numbers[y], numbers[z]])
                else:  # breaks if sum is not zero
                    break
    print("\nTriplets from the given sequence: ", t_list)  # print the triplets list


sequence = [4, 1, -5, 6, 4, -10, 9, 8, 7]  # sequence of numbers to find the triplets
triplets(sequence)  # calls the function triplets for the input sequence
