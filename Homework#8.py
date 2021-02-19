""
"""Друзья, теперь ваше ДЗ это одно задание, у которого есть подзадания.
Т.е. если вы создали какую то функцию для задания 1, то вы можете ее или ее результат использовать в другом задании.
Не повторяйте себя ))

ДЗ
1. Даны списки names и domains (создать самостоятельно).
Написать функцию для генерирования e-mail в формате:
фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
фамилию и домен брать случайным образом из заданных списков 
переданных в функцию в виде параметров.
Строку и число генерировать случайным образом.
Буквы в строке МОГУТ повторяться (перемешивание алфавита не подойдет, 
так как буквы не смогут повторяться)
Пример:
names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
print(e_mail)

>>>miller.249@sgdyyur.com"""

names = ["king", "miller", "kean", "jones", "smith", "black"]
domains = ["net", "com", "ua"]

import random as rnd
import string

#def random_string():
    #letters = string.ascii_lowercase
    #selection = [rnd.choice(letters) for i in range(rnd.randint(5,7))]
    #str = ''.join(selection)
    #return str

#print(random_string())

def create_email(names, domains):
     name = rnd.choice(names)
     number = rnd.randint(100, 999)
     domain = rnd.choice(domains)
     selection = [rnd.choice(string.ascii_lowercase) for i in range(rnd.randint(5, 7))]
     box_name = ''.join(selection)
     return f"{name}.{number}@{box_name}.{domain}"

mail = create_email(names, domains)
print(mail)

print("----------------------------------------------------enf-of-1")

""" 
2. Написать функцию, которая генерирует и возвращает строку 
случайной длинны.
Минимальную и максимальную длину строки ограничить с 
помощью параметров min_limit, max_limit, передаваемых в функцию.
"""

def random_string(min_limit: int, max_limit: int):
    alphabet = string.ascii_lowercase
    count = rnd.randint(min_limit, max_limit)
    str = alphabet*count
    return str

print(random_string(2,5))

print("------------------------------------------------------end-of-2")

"""
3. Написать функцию (или последовательность нескольких функций), 
которые преобразуют случайную строку, полученную в п 2 по следующим правилам:
- В строке должны присутствовать большие и маленькие буквы английского алфавита, 
цифры, пробелы, знаки препинания, символ перехода на новую строку (\n).
- Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
Под словом будем понимать набор случайных букв от одной до 10.
- Большие буквы только в начале слов. 
- Цифры не должны быть частями слов, а стоять отдельно.
- Знаки препинания всегда идут в конце слова.
"""

def create_random_str(rand_flag=False):
    alphabet = string.ascii_lowercase
    count = rnd.randint(1, 10) if rand_flag else 2
    return alphabet * count

def create_spaces(rand_str):
    index = 0
    random_string_to_list = list(rand_str)
    condition = True
    while condition:
        step = rnd.randint(1, 10)
        index += step
        if index < len(rand_str):
            random_string_to_list[index] = " "
        else:
            condition = False
    rand_str = "".join(random_string_to_list)
    return rand_str

def modify_word(word, capitalize_percentage=0.3):
    if rnd.random() < capitalize_percentage:
        word = word.capitalize()
    return word

def modify_str(rand_str):
    rand_str_split = rand_str.split()
    result = []
    for word in rand_str_split:
        word = modify_word(word)
        result.append(word)
    return " ".join(result)

def create_list():
    my_list = []
    for i in range(10):
        my_list.append(rnd.randint(100, 999))
    return my_list
my_list = create_list()
print(my_list)

def change_to_list(rand_str):
    rand_str_split = rand_str.split(' ')
    return rand_str_split

rand_str = create_random_str(True)
rand_str = create_spaces(rand_str)
rand_str = modify_str(rand_str)
rand_str = change_to_list(rand_str)

def merge_lists(rand_str):
    outcome = rand_str + create_list()
    rnd.shuffle(outcome)
    outcome = ' '.join(str(elem) for elem in outcome)
    return outcome

rand_str = merge_lists(rand_str)
print(rand_str)

punctuation = ['.',',',':',';','-','/n']

def add_punctuation(rand_str):
    random_string_to_list = rand_str.split(' ')
    i = 0
    condition = True
    while condition:
        step = rnd.randint(2, 4)
        i += step
        if i < len(random_string_to_list):
            random_string_to_list[i] = random_string_to_list[i] + rnd.choice(punctuation)
        else:
            condition = False
    rand_str = " ".join(random_string_to_list)
    return rand_str

rand_str = add_punctuation(rand_str)
print(rand_str)