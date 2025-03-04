#!/usr/bin/env python3
import sys
import re
import string
import requests

# Load stopwords

stopwords_list = requests.get("https://gist.githubusercontent.com/rg089/35e00abf8941d72d419224cfd5b5925d/raw/12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt").content
stopwords = list(set(stopwords_list.decode().splitlines()))


def clean_text(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)  # Remove text within brackets
    text = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', text)  # Remove punctuation
    text = re.sub(r'[\d]+', ' ', text)  # Remove numbers
    text = ' '.join([word for word in text.split() if word not in stopwords])  # Remove stopwords
    return text

for line in sys.stdin:
    cleaned_text = clean_text(line.strip())
    words = cleaned_text.split()
    for word in words:
        print(f"{word}\t1")