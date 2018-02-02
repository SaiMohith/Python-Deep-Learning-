# This program is to get the middle word, longest word in the sentence and print the sentence with words reversed


def mid_word(inp):  # define a function mid_word to find the middle word in the sentence
    words = inp.split()  # split the sentence into words and store in the list words
    num = int((len(words)))  # get the length of the list
    if len(words) % 2 == 0:  # if length is even number
        print("Middle words: ", words[(int((num / 2)-1)):(int((num / 2)+1))])  # print the middle words
    else:  # if the length is odd
        print("Middle Word: ", words[int(num/2)])  # print the median


def longest_word(inp):  # define a function longest_word to print the longest word in the sentence
    words = inp.split()  # split the sentence into words in a list
    lengths = []  # create a lengths list
    for word in words:
        lengths.append(len(word))  # for every word in the words list append the list of each word in the lengths list
    i = lengths.index(max(lengths))  # get the index which has the max length in the length list
    print("Longest word: ", words[i])  # return the longest word


def reversed_words(inp):  # define a function to print the sentence with the reversed words
    words = inp.split() # split the words in the sentence
    r_words = []  # create a empty list to store the reversed words
    for word in words:
        r_words.append(word[::-1])  # for each word in words get the reversed word and append it in the r_words list
    print("Sentence with reversed words: ", ' '.join(r_words))  # print the joined version of the r_words list


# ask the user to enter the sentence
sent = input("\n Please enter the sentence to get the middle word, longest word and sentence with reversed words:")
mid_word(sent)  # call the mid_word function for the user input
longest_word(sent)  # call the longest_word function
reversed_words(sent)  # call the reversed_words function
