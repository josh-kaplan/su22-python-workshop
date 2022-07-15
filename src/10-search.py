"""

Determine if a word is in the list.

"""

import os

# Get the file path of the words
data_path = os.path.join(os.path.dirname(__file__), "..", "data")
abs_path = os.path.abspath(data_path)
file_path = os.path.join(abs_path, "common_words.txt")

# Open and read the file
with open(file_path) as f:
    words = f.read().splitlines()


# Prompt user for a word
search_word = input("Enter a word: ")

# Search for the word
is_found = False
for word in words:
    # If the word is 5 letters long, append it to the list
    if word == search_word:
        print(f"Yes! The word '{search_word}' is in the list.")
        is_found = True
        break
if not is_found:
    print(f"No. The word '{search_word}' was not found.")
