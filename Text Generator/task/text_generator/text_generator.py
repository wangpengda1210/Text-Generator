# Write your code here
from nltk.tokenize import regexp_tokenize
from collections import Counter
import random


def get_tri_grams(corpus):
    words = regexp_tokenize(corpus, "[\\S]+")
    tri_grams = [[f'{words[i]} {words[i + 1]}', words[i + 2]] for
                 i in range(len(words) - 2)]
    return tri_grams


def get_markov_chain(tri_grams):
    markov_chain = {}

    for head, tail in tri_grams:
        markov_chain.setdefault(head, []).append(tail)

    return markov_chain


def get_first_word(markov_chain):
    next_word_first, next_word_second = random.choice(list(markov_chain.keys())).split()
    while not next_word_first[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or \
            next_word_first.endswith(".") or next_word_first.endswith("?") or \
            next_word_first.endswith("!"):
        next_word_first, next_word_second = random.choice(list(markov_chain.keys())).split()

    return next_word_first + " " + next_word_second


if __name__ == "__main__":
    with open(input(), "r", encoding="utf-8") as f:
        corpus = f.read()

    tri_grams = get_tri_grams(corpus)
    markov_chain = get_markov_chain(tri_grams)

    for _ in range(10):
        sentence = get_first_word(markov_chain) + " "
        while True:
            words = sentence.split()

            counter = Counter(markov_chain[words[-2] + " " + words[-1]]).most_common()

            next_word = random.choices([pair[0] for pair in counter],
                                       weights=[pair[1] for pair in counter])[0]

            if (next_word.endswith(".") or next_word.endswith("?") or
                    next_word.endswith("!")) and len(sentence.split()) >= 4:
                sentence += next_word
                break

            sentence += next_word + " "

        print(sentence)
