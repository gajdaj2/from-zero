#!/usr/bin/env python

import wikipedia 
from textblob import TextBlob


def search_wikipedia(name):
    print(f"Search for name: ${name}")
    return wikipedia.search("Jan Brzechwa")

def summerize_wikipedia(name):
    print(f"Summarize name: {name}")
    return wikipedia.summary(name)    
    

def get_text_blob(text):
    blob = TextBlob(text)
    return blob


def get_phrases(text):
    blob = TextBlob(text)
    return blob.noun_phrases


