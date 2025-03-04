import string
import requests
import re

text_url = "https://raw.githubusercontent.com/singhj/big-data-repo/main/text-proc/poe-stories/A_DESCENT_INTO_THE_MAELSTROM"
text_response = requests.get(text_url)
text = text_response.content.decode('utf-8')

# Fetch the stopwords list
stopwords_url = "https://gist.githubusercontent.com/rg089/35e00abf8941d72d419224cfd5b5925d/raw/12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt"
stopwords_response = requests.get(stopwords_url)
stopwords_list = stopwords_response.content.decode('utf-8')
stopwords = set(stopwords_list.splitlines())


def clean_text(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)  # Remove text within brackets
    text = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', text)  # Remove punctuation
    text = re.sub(r'[\d]+', ' ', text)  # Remove numbers
    text = ' '.join([word for word in text.split() if word not in stopwords])  # Remove stopwords
    return text

text = clean_text(text).split()

print(len(text))

# Answer: 2481 words in total for A_DESCENT_INTO_THE_MAELSTROM