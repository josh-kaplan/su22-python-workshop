"""

Get a list of 5-letter words from the common words list.

"""

import os

# Get the file path of the words
data_path = os.path.join(os.path.dirname(__file__), "..", "data")
abs_path = os.path.abspath(data_path)
file_path = os.path.join(abs_path, "common_words.txt")

# Open and read the file
with open(file_path) as f:
    words = f.read().splitlines()

# Start with an empty list
five_letter_words = []
for word in words:
    # If the word is 5 letters long, append it to the list
    if len(word) == 5:
        five_letter_words.append(word)

# Print the final list
count = 1
for word in sorted(five_letter_words):
    print(f"{count}. {word}")
    count += 1

