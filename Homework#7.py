""
"""
1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
Задание можно выполнить и через обычный цикл и через генератор списков.
"""

from random import randint

my_list = []
for index in range(0,20):
    my_list.append(randint(1,100))
print(my_list)

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

all_age = []
for person in persons:
    all_age.append(person["age"])
print(all_age)

min_age = min(all_age)
print(min_age)

for item in persons:
    if item["age"] > min_age:
        pass
    elif item["age"] == min_age:
        print(f"Имя самого молодого человека - {item["name"]}")

print("------------------------------------------------------------------")

"""б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена."""

all_names = []
for person in persons:
    all_names.append(person["name"])
    print(all_names)

for i in all_names:


"""Если циклом пройтись по persons и прочитать person["age"] 
в отдельный список и потом найти min для него. 
Это будет минимальный возраст.
А потом еще раз в цикле пройти и сравнить с этим значением."""

#for d in LofD:
  #   for k, v in d.items():
  #     r[k][v] += 1
  # return dict((k, dict(v)) for k, v in r.items())

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

"б) Создать список из ключей, которые есть в первом, но нет во втором словаре."

list_of_unique_keys = []
for key in my_dict_1_keys:
    if key not in my_dict_2_keys:
        list_of_unique_keys.append(key)
print(list_of_unique_keys)

"в) Создать новый словарь из пар {ключ:значение}, для ключей,"
"которые есть в первом, но нет во втором словаре."

new_dict = {}
