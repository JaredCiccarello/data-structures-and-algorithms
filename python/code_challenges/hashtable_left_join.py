from data_structures.hashtable import Hashtable


def left_join(synonyms, antonyms):
    result = {}

    for word, synonym in synonyms.items():
        result[word] = [synonym, antonyms.get(word)]

    return result

