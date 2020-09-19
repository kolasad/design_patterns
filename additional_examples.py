
# replace Sam in sentence with John
sentence = 'Sam did it!'
# CLEAN CODE
sentence = sentence.replace('Sam', 'John')

# NO CLEAN CODE
# sentence = list(sentence)
# print(sentence)
# sentence = sentence[3:]
# print(sentence)
# sentence = ['J', 'o', 'h', 'n'] + sentence
# print(''.join(sentence))


numbers = [2, 3, 15, 1, 150, 12]
print(f'Liczby przed sortowaniem: {numbers}')
print(f'Wynik sorted: {sorted(numbers)}')
print(f'Liczby po sortowaniu sorted bez przypisania: {numbers}')
print(f'Wynik .sort(): {numbers.sort()}')
print(f'Liczby po sortowaniu .sort(): {numbers}')