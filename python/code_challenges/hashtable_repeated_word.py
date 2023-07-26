from data_structures.hashtable import Hashtable
import re


def first_repeated_word(_str):
    # Clean the input string and remove punctuation
    stripped_str = re.sub(r'[^\w\s]', '', _str.lower())

    # Tokenize the cleaned string into words
    words = re.findall(r'\b\w+\b', stripped_str)

    # Use a dictionary to keep track of seen words
    word_dict = {}

    for word in words:
        if word in word_dict:
            return word
        else:
            word_dict[word] = True

    return None

