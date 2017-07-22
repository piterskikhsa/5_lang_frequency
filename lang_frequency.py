import os
import re
import string
from collections import Counter

import sys


MOST_FREQUENT_WORDS_LIMIT = 10

def load_data(filepath):
    words_list = []
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        for line in file_handler:
            words_list += get_word_from_line(line)

    return words_list


def get_word_from_line(text_line):
    words = text_line.lower()
    words = re.findall(r'\w+', words)
    words = [w.rstrip(string.punctuation) for w in words]
    return words


def get_most_frequent_words(words_list):
    return Counter(words_list).most_common(MOST_FREQUENT_WORDS_LIMIT)


def pprint_words_list(words_list):
    for word in words_list:
        print('слово "{}" встретилось - {} - раз;'.format(item[0], item[-1]))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input('ВВедите путь к файлу: ')
    words = load_data(file_path)
    if words:
        most_frequent_words = get_most_frequent_words(words)
        pprint_words_list(most_frequent_words)
