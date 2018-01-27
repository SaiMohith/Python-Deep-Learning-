testfile = open("C:/Users\SaiMohith\PycharmProjects\ICP2\Test.txt", 'r')  # open the Test.txt file in read mode
line = testfile.readline()  # reads each line in the file
while line != "":  # run the loop if the line is not empty
    word = line.split()  # split the line into words
    print(line, len(word))  # print the results
    line = testfile.readline()  # go for the next line in the file until there is a empty line
