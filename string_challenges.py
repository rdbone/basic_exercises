# Вывести последнюю букву в слове
word = 'Архангельск'
print(f'Последняя буква в слове: {word[-1]}')


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(f'Количество букв "а": {word.lower().count("а")}')


# Вывести количество гласных букв в слове
word = 'Архангельск'

vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'ю', 'я']
count = 0
for letter in word.lower():
    if letter in vowels:
        count += 1
print(f'Количество гласных букв: {count}')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f'Количество слов в предложении: {len(sentence.strip().split(" "))}')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.strip().split(' '):
    print(word[0])



# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
total_length = 0
for word in sentence.strip().split(' '):
    total_length += len(word)
print(f'Усредненная длина слов в предложении: {round(total_length/len(sentence.strip().split(" ")))}')