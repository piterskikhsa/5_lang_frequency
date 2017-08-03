import os
import re
import string
from collections import Counter

import sys


MOST_FREQUENT_WORDS_LIMIT = 10

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return file_handler.read()


def get_word_from_file(text_file):
    words = text_file.lower()
    words = re.findall(r'\w+', words)
    words = [word.rstrip(string.punctuation) for word in words]
    return words


def get_most_frequent_words(words_list):
    return Counter(words_list).most_common(MOST_FREQUENT_WORDS_LIMIT)


def pprint_words_list(words_list):
    for word in words_list:
        print('слово "{}" встретилось - {} - раз;'.format(word[0], word[-1]))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input('ВВедите путь к файлу: ')
    text_file = load_data(file_path)
    words = get_word_from_file(text_file)
    if words:
        most_frequent_words = get_most_frequent_words(words)
        pprint_words_list(most_frequent_words)
