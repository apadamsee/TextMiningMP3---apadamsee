"""
MP3 Lyric Scraping from Genius

@author: Afraz Padamsee

This file contains the code for connecting to the Genius API and scraping lyrics from Genius
"""

import requests
import urllib.request as urllib
import json
from bs4 import BeautifulSoup
import re

def search_for_song(search_term):
    """
    Searches for search_term on Genius thru its API and returns a JSON object of the top search result('hit')

    UNIT TESTED: by comparing searches on the Genius website to the results of the same searches on this function and seeing if they matched
        e.g. print(search_for_song('highest in the room')) -- (correctly searched for and grabbed the Travis Scott song)
    """
    # Format a request URI for the Genius API  (to search for songs)
    _URL_API = "https://api.genius.com/"
    _URL_SEARCH = "search?q="
    querystring = _URL_API + _URL_SEARCH + urllib.quote(search_term)
    request = urllib.Request(querystring)
    request.add_header("Authorization", "Bearer " + "QootmN8aXaeUEtMguYVsDpQyr1VO6s1O8FUB0cTccMeyB4GRTHMvlDfUUb7YjEF1") #utilizing user access token
    request.add_header("User-Agent", "")
    # Actually search for the song
    response = urllib.urlopen(request, timeout=3).read().decode('UTF-8')
    json_obj = json.loads(response)
    if 'New Music Friday' in json_obj['response']['hits'][0]['result']['full_title']: # Avoiding issue where Genius returns the top search term as its weekly "New Music Friday" series that the song is a part of, rather than the song itself
        return json_obj['response']['hits'][1]['result']
    else:
        return json_obj['response']['hits'][0]['result']


def pull_spec_data(search_term, data_term):
    """
    Since search_for_song returns a JSON object that functions as a dict, this function returns the the specified
        category/data_term out for the specified song in the search term

    Options for data_term:
        'annotation_count', 'api_path', 'full_title', 'header_image_thumbnail_url', 'header_image_url', 'id', 'lyrics_owner_id',
        'lyrics_state', 'path', 'pyongs_count', 'song_art_image_thumbnail_url', 'song_art_image_url', 'stats', 'title',
        'title_with_featured', 'url', 'primary_artist'

    UNIT TESTED: by putting in each item in data_term list(above) and seeing if it returned the same info (but just for that specfific data term) as was in the general call of the search_for_song
        **Problem w/ 'primary_artist' that it has a sublist attached to it, so caling it in this manner returns another list for the primary_artist rather than 1 thing... ignoring it because for this project's purpose, primary_artist won't need to be called
        e.g. print(pull_spec_data('highest in the room','full_title'))
    """
    json_obj = search_for_song(search_term)
    return json_obj[data_term]
# print(json_obj['response']['hits'][0]['result'].keys())

def get_lyrics(search_term):
    """
    Scrapes the lyrics for the song specified in the search_term

    UNIT TESTED: by putting in multiple search terms and seeing if it pulled the lyrics
        e.g. print(get_lyrics('highest in the room'))
    """
    URL = pull_spec_data(search_term, 'url')
    # URL = json_obj['response']['hits'][0]['result']['url']
    page = requests.get(URL)
    html = BeautifulSoup(page.text, "html.parser") # Extract the page's HTML as a string
    # Scrape the song lyrics from the HTML
    lyrics = html.find("div", class_="lyrics").get_text()
    return lyrics

#### For scraping if you have the song ID
# song_id = 82926
# querystring = "https://api.genius.com/songs/" + str(song_id)  # Songs endpoint
# request = urllib.Request(querystring)
# request.add_header("Authorization", "Bearer " + "QootmN8aXaeUEtMguYVsDpQyr1VO6s1O8FUB0cTccMeyB4GRTHMvlDfUUb7YjEF1")
# request.add_header("User-Agent", "")
# response = urllib.urlopen(request, timeout=3)
# raw = response.read()
# json_obj = json.loads(raw)['response']['song']
