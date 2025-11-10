str=(input("введите строку: ")) # запрашиваем строку
words = str.split()              # разбиваем строку на слова
reversed_words = [w[::-1] for w in words]  # разворачиваем каждое слово
result = " ".join(reversed_words) # собираем обратно в строку
print(result)#выводи перевёрнутую строку на экран

