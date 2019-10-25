"""
@author: Afraz Padamsee

This file contains all the functions related to the analysis of the dataset
"""

import string
from nltk.util import ngrams
import collections

def bring_words(filename):
    """
    Reads the file with all the words from all the lyrics and puts them into a list so they can be analyzed
    """
    all_words = []
    wds = open(filename)
    for line in wds:
        cleanline = line.strip(string.whitespace)
        all_words.append(cleanline)
    # print(len(all_words))
    return all_words
# print(bring_words("all_words.txt"))
# bring_words("all_words.txt")

def valid_letters(word):
    """
    Returns True if a word has all valid letters,
    words w/ valid letters are words that don't include numbers, latin script letters with accents, non-latin script characters(such as Korean), and emojis(the fire emoji had a really high frequency so this deals with that)
    Apostrophes and dashes are allowed

    >>> valid_letters('\ufeffi')
    False
    >>> valid_letters('må')
    False
    >>> valid_letters('x2')
    False
    >>> valid_letters('øjne')
    False
    >>> valid_letters('introduction')
    True
    >>> valid_letters("don't")
    True
    >>> valid_letters('oh-oh-oh')
    True
    """
    flag = True
    for letter in word:
        if letter != "'" and letter != '-':
            if ord(letter) < 97 or ord(letter) > 122:
                flag = False
    return flag


###### I did not use this function in my final code, but I just figured I'd keep it here if I wanted to reference it later
# def histogram_unclean(word_list):
#     """
#     Takes a list of words and displays the top n in order of frequency of appearances, removing any words with non-english characters
#
#     ######## IS THIS FUNCTION EVEN NECESSARY?? freq_cleaned() DOES THE SAME THING BUT JUST MORE USEFUL... THIS IS ONLY RELEVANT IF freq_cleaned() CAN CALL THIS... OTHERWISE JUST USE freq_cleaned() ONLY FOR WORD FREQUENCY
#     ####################### SHOULD I DISPLAY THE COUNTS OF THE WORDS WITH THE WORDS?? IF SO HOW DO I DO THAT??
#     """
#     ## Create dictionary of word counts
#     word_counts = dict()
#     for word in word_list:
#         if valid_letters(word):
#             word_counts[word] = word_counts.get(word,0) + 1
#         # for letter in str(word):    #THIS DOESNT WORK, CAN U DO NESTED FOR LOOPS FOR WORD IN LIST AND LETTER IN THAT WORD??
#         #     if ord(letter) >= 97 and ord(letter) <= 122 or ord(letter) == 39 or ord(letter) == 45:    # Remove words w/ non-english characters (apostrophes and dashes are allowed)
#         #         word_counts[word] = word_counts.get(word,0) + 1
#     ## Sort the words by frequency
#     ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)  #PUT THIS IN SEPARATE FUNCTION TO OPERATE ON HISTOGRAM -- have several functions that operate on histogram... diff methods of analysis
#     #### DO LIST(DICT.items())
#     return ordered_by_frequency  #have this return (directly above line)
# # print(frequency(bring_words("all_words.txt"),400))
# # print(frequency(bring_words("all_words.txt")))

def histogram_cleaned(word_list):
    """
    Returns a histogram(dictionary) of words and their associated frequencies as keys and values, respectively
    This histogram cleans the original set of words by excluding coordinating conjunctions, meaningless words/articles, and non-english characters/words
    Will be used for frequency analysis of just words (not phrases)
    """
    cc = ['for','and','nor','but','or','yet','so']  ## Could have used filtering here
    meaningless = ['the','a','an']
    pronouns = ['i', 'you', 'he', 'she', 'it', 'they', 'me', 'him', 'her', 'my', 'mine', 'your', 'yours', 'his', 'her', 'hers', 'its']
    word_counts = dict()
    # COUNTER = 0
    for word in word_list:
        if word not in cc and word not in meaningless and word not in pronouns and word != '':   # Remove coordinating conjunctions and meaningless words/articles (and empty strings)
            if valid_letters(word):
                # COUNTER += 1
                word_counts[word] = word_counts.get(word,0) + 1
    # print(COUNTER)
    return word_counts
# histogram_cleaned(bring_words("all_words.txt"))

def ordered(histogram):
    """
    Returns a list of words in order of frequency of appearances
    This function is the frequency analysis of words
    """
    ordered_by_frequency = sorted(histogram, key=histogram.get, reverse=True)
    return ordered_by_frequency

def take_second(pair):
    """
    Returns the 2nd element in a list or a tuple
    Helper function for ordered_w_frequency() to sort histogram based on frequency while also including the corresponding frequency number
    """
    return pair[1]

def ordered_w_frequency(histogram,n):
    """
    Sorts the histogram of words and returns a list of tuples of the top n words and their respective frequencies(counts), ordered by frequency
    This function is the frequency analysis of words
    """
    hist_items = list(histogram.items())
    ordered_by_frequency = sorted(hist_items, key=take_second, reverse=True) # The key is calling the helper function that is right before this function
    return ordered_by_frequency[:n]
print(ordered_w_frequency(histogram_cleaned(bring_words("all_words.txt")),20))


def find_ngrams(word_list, n, amt):
    """
    Returns a list of the top [amt] of [n]-grams in a given [word_list]
    This function is the frequency analysis of phrases
    """
    n_grams = list(ngrams(word_list,n))
    freqs = collections.Counter(n_grams)  # I only found this package/function while I was researching to do n-grams, which is why it's not used anywhere else in this prioject
                                          # Honestly I'm happy I didn't use it because it was a better learning experience for me to work with ordering dictionaries and this just feels a little bit like a shortcut to use it on all frequency analysis of the project
    return freqs.most_common(amt)
print(find_ngrams(bring_words("all_words.txt"),2,30))


if __name__ == "__main__":
    import doctest
    doctest.run_docstring_examples(valid_letters, globals(), verbose=False)
    # doctest.testmod()
