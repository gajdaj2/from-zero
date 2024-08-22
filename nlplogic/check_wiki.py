#!/usr/bin/env python

import wikipedia
import nltk

nltk.download("punkt_tab")
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


def get_phrases(name):
    text = summerize_wikipedia(name)
    blob = get_text_blob(text)
    return blob.noun_phrases


if __name__ == "__main__":
    name = "Jan Brzechwa"
    print(f"Search for name: {name}")
    print(search_wikipedia(name))
    print(f"Summarize name: {name}")
    print(summerize_wikipedia(name))
    print(f"Get phrases for name: {name}")
    print(get_phrases(name))
