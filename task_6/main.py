# Открываем исходный файл для чтения
with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()
# Разбиваем текст на слова
words = text.split()
# Преобразуем список слов в множество (оставляет только уникальные)
unwords = set(words)
# Записываем уникальные слова в новый файл
with open("output.txt", "w", encoding="utf-8") as f:
    for word in unwords:
        f.write(word + "\n")

print("Уникальные слова успешно записаны в output.txt")

