"""
@author: Afraz Padamsee

This file contains all the functions related to compiling and cleaning the dataset for analysis
"""

from textmining import search_for_song, pull_spec_data, get_lyrics
import string

def searches(filename):
    """
    There is a text file with all the songs whose lyrics I'm analyzing, one search term (song) per line ("geniussearches.txt", which is in the repo)
    This function calls that file and puts all the songs in a list so their lyrics can be scraped
    """
    all_searches = []
    gs = open(filename)
    for line in gs:
        cleanline = line.strip(string.whitespace)
        all_searches.append(cleanline)
    return all_searches

def pull_all_lyrics(search_terms):
    """
    Uses get_lyrics to pull the lyrics from a list of searches (pulls all the lyrics of all the songs into one very long list)
    """
    lyrics_from_search = []
    for term in search_terms:
        lyric = get_lyrics(term)
        lyrics_from_search.append(lyric)
    return lyrics_from_search

def process_lyrics(search_terms):
    """
    Takes list of searches, calls pull_all_lyrics, and then processes them, splitting all the lyrics from all the given searches into individual words and caching them in a text file
    ONLY MEANT TO BE RUN ONCE - THE TEXT FILE WILL HOLD ALL THE WORDS LOCALLY AFTER ONE RUN (*PERSON GRADING THIS: The file is already in the repo, so no need to run this)
    """
    all_words = open("all_words.txt","w")
    pulled_lyrics = pull_all_lyrics(search_terms)
    processedwords = []
    for song in pulled_lyrics:
        song = song.lower()     # making all characters lowercase
        lines = song.split('\n') # splitting by line break to process song line by line
        for line in lines:
            if '[' not in line and line != '':    # Ignoring lines that are just the stage of the song (verse/chorus/etc.) or the name of the artist singing the verse (all in brackets), AND double line
                words = line.split(' ')  # Splitting each line into words to process farther
                for word in words:
                    word = word.strip(string.punctuation)
                    all_words.write(word+'\n')   # Caching giant list of all words from all lyrics
                    processedwords.append(word)
    all_words.close()
    # return processedwords    # un-comment if for some reason you want to return the giant word list without storing it

# process_lyrics(searches("geniussearches.txt"))   # Un-comment this to generate the text file with all the lyric words
