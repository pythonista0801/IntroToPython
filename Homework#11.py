""""""
"""
data.json - файл с данными о некоторых математиках прошлого.
1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
Если фамилии нет, то использовать имя, например Euclid.
3. Написать функцию сортировки по дате смерти из поля "years".
Обратите внимание на сокращение BC. - это означает до н.э.
4. Написать функцию сортировки по количеству слов в поле "text"
"""

import json
import re

#1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
def read_json(filename):
    with open(filename, "r") as js_file:
        data = json.load(js_file)
    return data

data = read_json('data.json')

#2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
#Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
#Если фамилии нет, то использовать имя, например Euclid.

def sort_key_by_name(sort_dict):
    # if sort_dict["name"] == 1:
    #     value = sort_dict["name"]
    # else:
    value = sort_dict["name"][-1]
    return value

result = sorted(data, key = sort_key_by_name)

print(result)

def turn_to_negative(my_dict):
    if 'BC' in my_dict['years']:


# def sort_by_bday(sort_dict):
#     age = sort_dict["age"]
#     years = re.findall(r'[0-9]+', age)
#     return int(years[0])