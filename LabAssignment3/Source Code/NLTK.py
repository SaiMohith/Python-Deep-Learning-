import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk import ngrams
from operator import itemgetter

file = open('input', 'r')  # Read the input file  to lemmatize and get bigrams
lines_in_file = file.readlines()
mrg = ""
for line in lines_in_file:  # Merge all the lines into one single line
    mrg=mrg+line

words_mrg = word_tokenize(mrg)  # Word Tokenize the sentence

# lemmatization

lemmatizer = WordNetLemmatizer()  # Lemmatize the words
list_lemm_words = []
for word in words_mrg:
    lemm_word = lemmatizer.lemmatize(word)
    list_lemm_words.append(lemm_word)
print("\n Lemmetization: \n")
print(list_lemm_words)  # print the Lemmatized words

# Bi-grams

grams_mrg = []
bigrams = ngrams(list_lemm_words, n=2)  # Bi-grams in the list of lemmatized words
for grams in bigrams:
    grams_mrg.append(grams)
print("\n BI-GRAMS in the Input: \n")
print(grams_mrg)  # Print the Bigrams

# Word Freq
pos_mrg = pos_tag(list_lemm_words)  # parts of Speech for all the words
string = " ".join(str(x) for x,y in pos_mrg)
string_word = word_tokenize(string)
mrg_freq = nltk.FreqDist(grams_mrg)  # Calculate the frequencies of words
common = mrg_freq.most_common()
BWF = sorted(common,key=itemgetter(0))
print("\n BI-GRAMS Word Frequencies: \n")
print(BWF)  # print the Bi-grams with word frequencies

print("\n Top Five BI-GRAMS According to Word Count: \n")
top_five_bigrams = mrg_freq.most_common(5)  # gets the  5 most common occurred bi-grams in the top_five_bigrams
print(top_five_bigrams)

# Sentences
sentence_mrg = sent_tokenize(mrg)  # Gets the sentences from the merged input file
sent_list = []

for sent in sentence_mrg:
    for word, words in grams_mrg:
        for ((o, p), l) in top_five_bigrams:
            if (word, words) == (o, p):
                sent_list.append(sent)  # Appending the sentences with the most common words.
print ("\n Sentences with top five Bigrams: \n")
print(max(sent_list, key=len))
