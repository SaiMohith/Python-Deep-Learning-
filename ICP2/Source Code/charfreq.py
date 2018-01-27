file = open("C:/Users\SaiMohith\PycharmProjects\ICP2\Wordlist.txt", 'r')  # open the Wordlist.txt file in read mode
result = open("C:/Users\SaiMohith\PycharmProjects\ICP2/results.txt", 'w')  # open the results.txt file in write mode
line = file.readline().lower()  # read the line in the file and convert the words into lowercase
while line != "":  # run the loop if the line is not empty
    i = (len(line)-1)
    print(line, i)
    result.write('{:0d}\n'.format(i))  # writes the result in the results.txt file
    line = file.readline().lower()  # reads the other lines in the file until there is a empty line
