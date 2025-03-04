#!/usr/bin/env python3
import sys
from collections import defaultdict
import nltk
nltk.download('averaged_perceptron_tagger')

# Initialize a dictionary to store word counts
word_counts = defaultdict(int)

for line in sys.stdin:
    word, count = line.strip().split("\t")
    word_counts[word] += int(count)

# Perform POS tagging on the words
tagged_words = nltk.pos_tag(list(word_counts.keys()))

# Aggregate words by their POS tags
pos_dict = defaultdict(list)
for word, tag in tagged_words:
    pos_dict[tag].append(word)

# Emit the POS tags and their corresponding words
for tag, words in pos_dict.items():
    print(f"{tag}\t{','.join(words)}")


#https://github.com/singhj/big-data-repo/blob/main/text-proc/poe-stories/A_DESCENT_INTO_THE_MAELSTROM