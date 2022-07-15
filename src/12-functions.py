"""

Fast lookups with dictionaries.

"""

import os
import time


def main():
    # Get the file path of the words
    data_path = os.path.join(os.path.dirname(__file__), "..", "data")
    abs_path = os.path.abspath(data_path)
    file_path = os.path.join(abs_path, "common_words.txt")

    # Open and read the file
    with open(file_path) as f:
        words_list = f.read().splitlines()

    # Create a dictionary of words
    words_dictionary = {}
    for word in words_list:
        words_dictionary[word] = True

    # Prompt user for a word
    search_word = input("Enter a word: ")

    # Search for the word
    start_1 = time.time()
    lookup_word_from_list(search_word, words_list)
    elapsed_1  = time.time() - start_1

    start_2 = time.time()
    lookup_word_from_dictionary(search_word, words_dictionary)
    elapsed_2 = time.time() - start_2

    print(f"Lookup from list took {elapsed_1} s.")
    print(f"Lookup from dict took {elapsed_2} s.")


def lookup_word_from_list(search_word, words_list):
    is_found = False
    for word in words_list:
        # If the word is 5 letters long, append it to the list
        if word == search_word:
            print(f"Yes! The word '{search_word}' is in the list.")
            is_found = True
            break
    if not is_found:
        print(f"No. The word '{search_word}' was not found.")


def lookup_word_from_dictionary(search_word, words_dictionary):
    is_in_dict = words_dictionary.get(search_word, False)
    if is_in_dict:
        print(f"Yes! The word '{search_word}' is in the dictionary.")
    else:
        print(f"No. The word '{search_word}' was not found.")


if __name__ == "__main__":
    main()
