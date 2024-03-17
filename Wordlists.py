import time

FILENAME = "/usr/share/dict/words"
LETTER = "s"


def count_words(filename, letter):
    total_words = 0
    words_with_letter = 0

    try:
        with open(filename, 'r') as f:
            words = f.read().splitlines()
    except FileNotFoundError:
        print("File not found.")
        return

    start = time.time()
    total_words = len(words)
    for word in words:
        if word.endswith(letter):
            words_with_letter += 1
    end = time.time()
    duration = end - start

    print(f"Total number of words: {total_words}")
    print(f"Number of words ending with '{letter}': {words_with_letter}")
    print(f"It took {duration} seconds to find this out!")

count_words(FILENAME, LETTER)
