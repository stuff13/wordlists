import time

def count_words(file):
    total_words = 0
    words_with_e = 0

    try:
        with open(file, 'r') as file:
            start = time.time()
            for line in file:
                words = line.split()
                total_words += len(words)
                for word in words:
                    if word.endswith("e"):
                        words_with_e += 1
                end = timer()
                time = end - start
            
    except FileNotFoundError:
        print("File not found.")
        return

    print(f"Total number of words: {total_words}")
    print(f"Number of words ending with 'e': {words_with_e}")
    print(f"It took {time} seconds to find this out!")

count_words('Wordlist.txt')
