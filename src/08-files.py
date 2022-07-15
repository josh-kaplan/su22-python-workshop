"""

Get a list of 5-letter words from the common words list.

"""

import os

# Get the current file
print(__file__)

# Get the directory name of the file location
dirname = os.path.dirname(__file__)
print(dirname)

# Get the full path
data_path = os.path.join(dirname, "..", "data")
print(data_path)

# Absolute path
abs_path = os.path.abspath(data_path)
print(abs_path)

# File path
file_path = os.path.join(abs_path, "common_words.txt")
print(file_path)

# Open and read the file
with open(file_path) as f:
    text = f.read()                 # Read the text
    lines = text.splitlines()       # Split lines into list of strings
    n_words = len(lines)            # Get the length of the list
    print(n_words)

