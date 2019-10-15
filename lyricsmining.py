"""
This file contains all the functions related to the analysis of the dataset
"""

import string

def bring_words(filename):
    """
    Reads the file with all the words from all the lyrics and puts them into a list so they can be analyzed
    """
    all_words = []
    wds = open(filename)
    for line in wds:
        cleanline = line.strip(string.whitespace)
        all_words.append(cleanline)
    return all_words

# print(bring_words("all_words.txt"))

def frequency(word_list):
    """
    Takes a list of words and displays the top n in order of frequency of appearances, removing any words with non-english characters
        Non-english characters include numbers, latin script letters with accents, non-latin script characters(such as Korean), and emojis(the fire emoji had a really high frequency so this deals with that)

    ######## IS THIS FUNCTION EVEN NECESSARY?? freq_cleaned() DOES THE SAME THING BUT JUST MORE USEFUL... THIS IS ONLY RELEVANT IF freq_cleaned() CAN CALL THIS... OTHERWISE JUST USE freq_cleaned() ONLY FOR WORD FREQUENCY
    ####################### SHOULD I DISPLAY THE COUNTS OF THE WORDS WITH THE WORDS?? IF SO HOW DO I DO THAT??
    """
    ## Create dictionary of word counts
    word_counts = dict()
    for word in word_list:
        for letter in str(word):    #THIS DOESNT WORK, CAN U DO NESTED FOR LOOPS FOR WORD IN LIST AND LETTER IN THAT WORD??
            if ord(letter) >= 97 and ord(letter) <= 122 or ord(letter) == 39 or ord(letter) == 45:    # Remove words w/ non-english characters (apostrophes and dashes are allowed)
                word_counts[word] = word_counts.get(word,0) + 1
    ## Sort the words by frequency
    ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)
    return ordered_by_frequency

# print(frequency(bring_words("all_words.txt"),400))
print(frequency(bring_words("all_words.txt")))

def freq_cleaned(word_list,n):
    """
    Displays the ordered frequency list but with coordinating conjunctions, meaningless words/articles, and non-english characters/words removed
    Will be used for frequency analysis of just words (not phrases)
    """
    cc = ['for','and','nor','but','or','yet','so']
    meaningless = ['the','a','an']
    ## Create dictionary of word counts
    word_counts = dict()
    for word in word_list:  ############### HOW DO I MAKE THE CLEANED LIST BY CALLING frequency() AND NOT DOING THE WHOLE OPERATION AGAIN?? - I'm not entirely sure how the list sorting works with the dict->list in frequency() which is why i cant do it
        if word not in cc and word not in meaningless:   # Remove coordinating conjunctions and meaningless words/articles
            for letter in word:
                if ord(letter) >= 97 and ord(letter) <= 122 or ord(letter) == 39 or ord(letter) == 45:    # Remove words w/ non-english characters (apostrophes and dashes allowed)
                    word_counts[word] = word_counts.get(word,0) + 1
    ## Sort the words by frequency
    ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)
    return ordered_by_frequency[:n]

    # freq = []
    # cc = ['for','and','nor','but','or','yet','so']
    # meaningless = ['the','a','an']
    # for word in frequency(word_list):
    #     if word not in cc and word not in meaningless:   # Remove coordinating conjunctions and meaningless words/articles
    #         for letter in word:
    #             if ord(letter) >= 97 and ord(letter) <= 122 or ord(letter) == 39:    # Remove non-english characters
    #                 freq.append(word)  ###THIS DOESNT WORK
    # return freq
# print(freq_cleaned(bring_words("all_words.txt"),50))





####################****ngrams -- groups of words that follow each other -- can do for higher level analysis -- can grab words that follow e/o from list of words -- FOR PHRASES
