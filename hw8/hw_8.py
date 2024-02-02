def process_text(text):
    text = text.lower()

    vowels = 'aeiouаеёиоуыэюя'
    consonants = 'bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ'

    num_vowels = sum(1 for char in text if char in vowels)
    num_consonants = sum(1 for char in text if char in consonants)

    if num_vowels > num_consonants:

        popular_vowels = sorted(set([char for char in text if char in vowels]), key=text.count, reverse=True)[:3]
        result = f"Голосних літер більше. Три найпопулярніші голосні літери: {', '.join(popular_vowels)}"
    else:

        popular_consonant = max(set([char for char in text if char in consonants]), key=text.count)
        result = f"Приголосних літер більше. Найпопулярніша приголосна літера: {popular_consonant}"

    return result


def find_most_common_short_word(text):
    words = text.split()
    word_counts = {}

    for word in words:

        clean_word = ''.join(char for char in word if char.isalnum())

        if clean_word:
            word_counts[clean_word] = word_counts.get(clean_word, 0) + 1

    most_common_short_word = min(word_counts, key=lambda x: (len(x), -word_counts[x]))

    return most_common_short_word


def replace_most_common_short_word(text, most_common_short_word):
    most_common_short_word_upper = most_common_short_word.upper()

    result_text = text.replace(most_common_short_word, most_common_short_word_upper)

    return result_text


def main():
    with open('input_8.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    result = process_text(text)

    most_common_short_word = find_most_common_short_word(text)

    result_text = replace_most_common_short_word(text, most_common_short_word)

    with open('output.txt', 'w', encoding='utf-8') as out_file:
        out_file.write(result)
        out_file.write('\n\nСаме коротке слово, яке встречається найчастіше: {}\n'.format(most_common_short_word))
        out_file.write(result_text)


main()
