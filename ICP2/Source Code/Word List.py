def longest(words):  # define a function to find the longest word
    lengths = []  # create an empty list to store the length of each word
    for word in words:
        lengths.append((len(word), word))  # append each word and it's length
    return max(lengths)  # return the word with maximum length


print(longest(["Python", "Saimohith", "University", "PHP"]))  # print the longest word
