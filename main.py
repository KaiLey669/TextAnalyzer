import string


punctuation = string.punctuation
vowels_ru = "аеёиоуыэюя"
vowels_count = 0
max_word_count = 0
max_len_word = ""
repeated_words = {}

user_text = input("Введите текст (RU): ")
words = []
current_word = ""
for ch in user_text:
    if ch not in punctuation and ch != " ":
        current_word += ch
    else:
        if current_word:
            words.append(current_word)
            current_word = ""

if current_word:
    words.append(current_word)

for word in words:
    lower_word = word.lower()
    if lower_word not in repeated_words:
        repeated_words[lower_word] = 1
    else:
        repeated_words[lower_word] += 1

    current_word_len = len(word)
    if current_word_len > max_word_count:
        max_word_count = current_word_len
        max_len_word = word

    for char in word.lower():
        if char in vowels_ru:
            vowels_count += 1

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
