#!/usr/bin/env python3
import sys
from collections import defaultdict
import nltk
nltk.download('averaged_perceptron_tagger')

# Collect all unique words
unique_words = set()

for line in sys.stdin:
    word, _ = line.strip().split("\t")
    unique_words.add(word)

# Perform POS tagging on unique words
tagged_words = nltk.pos_tag(list(unique_words))

# Count POS tags
pos_counts = defaultdict(int)
for word, tag in tagged_words:
    if tag.startswith('NN'):  # Nouns
        pos_counts['NN'] += 1
    elif tag.startswith('VB'):  # Verbs
        pos_counts['VB'] += 1
    elif tag.startswith('JJ'):  # Adjectives
        pos_counts['JJ'] += 1
    elif tag.startswith('RB'):  # Adverbs
        pos_counts['RB'] += 1

# Emit POS counts
for pos, count in pos_counts.items():
    print(f"{pos}\t{count}")