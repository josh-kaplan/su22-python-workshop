"""

Fast lookups with dictionaries.

"""

import os

# Get the file path of the words
data_path = os.path.join(os.path.dirname(__file__), "..", "data")
abs_path = os.path.abspath(data_path)
file_path = os.path.join(abs_path, "common_words.txt")

# Open and read the file
with open(file_path) as f:
    words = f.read().splitlines()


# Create a dictionary of words
words_dictionary = {}
for word in words:
    words_dictionary[word] = True

print(words_dictionary.get("degree", False))
print(words_dictionary.get("aerospace", False))

