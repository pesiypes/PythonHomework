# Напишите программу, которая получает от пользователя имя файла,
# открывает этот файл в текущем каталоге, читает его и выводит два слова:
# наиболее часто встречающееся из тех, что имеют размер более трех символов,
# и наиболее длинное слово на английском языке.
#
# В файле ожидается смешанный текст на двух языках — русском и английском.
u_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ru_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
en_lower = 'abcdefghijklmnopqrstuvwxyz'
en_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
words = []
with open('name.txt', encoding="utf8") as myFile:
    for word in myFile:
        words.append(word.replace('\n', '').split(' '))

# for i in words:
#     print(i)


def count(f):
    diction = {}
    for l in f:
        for w in l:
            if w not in diction:
                diction[w] = 1
            else:
                diction[w] += 1
    return diction
print(count(words))
a = count(words)
print(max(a.values()))
z = []
for i in a.keys():
    if a.get(i) == max(a.values()):
        z.append(i)
print(z)
print(a.keys())
print(a.values())
print(max(a.values()))