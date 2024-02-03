import re
from collections import Counter


def find_most_common_shortest_word(file):
    with open(file, 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)

        words = [word.lower() for word in words]

        word_counter = Counter(words)

        most_common_shortest_word = min(
            (word for word, count in word_counter.items() if count == max(word_counter.values(), default=0)),
            key=len
        )

    return most_common_shortest_word


file_path = 'Input_1.txt'
result = find_most_common_shortest_word(file_path)
print(result)
