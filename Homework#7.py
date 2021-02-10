""
"""
1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
Задание можно выполнить и через обычный цикл и через генератор списков.
"""

from random import randint

new_list = [randint(1,100) for i in range(0,20)]
print(new_list)

my_list = []
for index in range(0,20):
    my_list.append(randint(1,100))
print(my_list)

print("----------------------------------------------------------end-of-1")
"""
2) Создать словарь triangle в который записать точки A B C (ключи),
и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси.
"""
def create_random_point():
    point = (randint(-10, 10),
             randint(-10, 10),
             randint(-10, 10))
    return point

triangle = {"A": create_random_point(),
            "B": create_random_point(),
            "C": create_random_point()}
print(triangle)

print("----------------------------------------------------------end-of-2")
"""
3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
с тремя символами * вначале и в конце строки.
Пример:
my_str = 'I'm the string'
Печатает ***I'm the string***
"""
my_str = "I'm the string"
def print_string(string):
    print(f"***{string}***")

print_string(my_str)

print("----------------------------------------------------------end-of-3")
"""
4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
в) Посчитать среднее количество лет всех людей из списка.
"""

persons = [{"name": "John", "age": 25},
           {"name": "Anna", "age": 65},
            {"name": "Bill", "age": 33},
            {"name": "Jack", "age": 45},
           {"name": "Christine", "age": 15},
           {"name": "Kateline", "age": 15}]

"""а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена."""

all_age_list = []
for person in persons:
    all_age_list.append(person["age"])
print(all_age_list)

min_age = min(all_age_list)
print(min_age)

for item in persons:
    if item["age"] > min_age:
        pass
    elif item["age"] == min_age:
        print(f"Имя самого молодого человека - {item['name']}")

print("----------------------------------------------------------end-of-4a")

"""б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена."""

all_names = []
for person in persons:
    all_names.append(person["name"])
print(all_names)

length = []

for name in all_names:
    length.append(len(name))
print(length)

max_length = max(length)

for name in all_names:
    if len(name) < max_length:
        pass
    elif len(name) == max_length:
        print(f"Самое длинное имя - {name}")

print("----------------------------------------------------------end-of-4b")

"в) Посчитать среднее количество лет всех людей из списка."

all_age_list = []
for person in persons:
    all_age_list.append(person["age"])
print(all_age_list)

number = len(all_age_list)
print(number)

average_age = sum(all_age_list)/number
print(f"Среднее количество лет -  {average_age}")

print("----------------------------------------------------------end-of-4v")
"""
5) Даны два словаря my_dict_1 и my_dict_2.
а) Создать список из ключей, которые есть в обоих словарях.
б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
г) Объединить эти два словаря в новый словарь по правилу:
если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
"""
my_dict_1 = {"name": "John",
             "last_name": "Black",
             "email": "test@gmail.com",
             "age": 35,
             "address": "Cleveroad, 12",
             "Company": "Soft Solutions"}

my_dict_2 = {"name": "David",
             "email": "david@gmail.com",
             "age": 45,
             "address": "Bendroad, 18",
             "Occupation": "Developer",
             "Hobby": "Sky Diving"}

"а) Создать список из ключей, которые есть в обоих словарях."

my_dict_1_keys = set(my_dict_1.keys())
my_dict_2_keys = set(my_dict_2.keys())

list_of_keys = list(my_dict_1_keys.intersection(my_dict_2_keys))
print(list_of_keys)

print("---------------------------------------------------end-of-5a")
"б) Создать список из ключей, которые есть в первом, но нет во втором словаре."

list_of_unique_keys = []
for key in my_dict_1_keys:
    if key not in my_dict_2_keys:
        list_of_unique_keys.append(key)
print(list_of_unique_keys)

print("---------------------------------------------------end-of-5b")
"в) Создать новый словарь из пар {ключ:значение}, для ключей,"
"которые есть в первом, но нет во втором словаре."

new_dict = dict((key, my_dict_1[key]) for key in my_dict_1 if key not in my_dict_2)
print(new_dict)

new_dictionary = {}
for key in my_dict_1:
    if key not in my_dict_2:
        new_dictionary.setdefault(key, my_dict_1[key])
print(new_dictionary)

print("---------------------------------------------------end-of-5v")
"""г) Объединить эти два словаря в новый словарь по правилу:
если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
если ключ есть в двух словарях - поместить пару {ключ: 
[значение_из_первого_словаря, значение_из_второго_словаря]},"""

joined_dict = {}
for key in my_dict_1.keys():
    if key not in my_dict_2:
        joined_dict.setdefault(key, my_dict_1[key])
    if key in my_dict_2:
        joined_dict.setdefault(key,[my_dict_1[key], my_dict_2[key]])
print(joined_dict)

for key in my_dict_2.keys():
    if key not in my_dict_1:
        joined_dict.setdefault(key, my_dict_2[key])
print(joined_dict)

print("---------------------------------------------------end-of-5g")

