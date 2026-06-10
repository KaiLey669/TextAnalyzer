import string


def clear_punctuation(text: str) -> list:
    words = []
    current_word = ""
    for ch in user_text:
        if ch not in string.punctuation and ch != " ":
            current_word += ch
        else:
            if current_word:
                words.append(current_word)
                current_word = ""

    if current_word:
        words.append(current_word)

    return words

def check_repeated_words(lower_word: str, repeated_words: dict):
    if lower_word not in repeated_words:
        repeated_words[lower_word] = 1
    else:
        repeated_words[lower_word] += 1

def check_max_word(word: str, max_word_count: int, max_len_word: str) -> tuple:
    current_word_len = len(word)
    if current_word_len > max_word_count:
        max_word_count = current_word_len
        max_len_word = word

    return max_len_word, max_word_count

def add_vowels(word: str, vowels: str, vowels_count: int) -> int:
    for char in word.lower():
        if char in vowels:
            vowels_count += 1

    return vowels_count

def print_results(words: list, max_len_word: str, vowels_count: int, repeated_words: dict):
    print(f"Количество слов в тексте - {len(words)}")
    if max_len_word == "":
        print("Самое длинное слово - отсутсвует")
    else:
        print(f"Самое длинное слово - {max_len_word}")

    print(f"Количество гласных в тексте - {vowels_count}")

    print("Количество повторений слов в тексте:")
    if repeated_words:
        for word in repeated_words:
            print(f"{word} -> {repeated_words[word]}")
    else:
        print("Слова в тексте отсутсвуют.")

def analyze_text(user_text: str):
    vowels_ru = "аеёиоуыэюя"
    vowels_count = 0
    max_word_count = 0
    max_len_word = ""
    repeated_words = {}
    clear_words = clear_punctuation(user_text)

    for word in clear_words:
        lower_word = word.lower()
        check_repeated_words(lower_word, repeated_words)

        max_word_info = check_max_word(word, max_word_count, max_len_word)
        max_len_word = max_word_info[0]
        max_word_count = max_word_info[1]

        vowels_count =+ add_vowels(lower_word, vowels_ru, vowels_count)

    print_results(clear_words, max_len_word, vowels_count, repeated_words)


user_text = input("Введите текст (RU): ")
analyze_text(user_text)
