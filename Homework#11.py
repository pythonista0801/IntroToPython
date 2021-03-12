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
    value = sort_dict["name"].split(" ")[-1]
    return value

result = sorted(data, key = sort_key_by_name)
print(result)

#3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.

# def find_numbers(sort_dict: dict):
#     values = sort_dict["years"]
#     all_values = re.findall(r"[0-9]+", values)
#     return int(all_values)
#
# result = sorted(data, key = find_numbers)
# print(result)


def sort_key_by_year(sort_dict: str) -> int:
    year = re.match(".+\s(\d+)\D*$", sort_dict).group(1)
    year = -int(year) if ("bc" in sort_dict.lower()) else int(year)
    return year


res = sorted(data, key=lambda x: sort_key_by_year(x["years"]))
print(res)


#4. Написать функцию сортировки по количеству слов в поле "text"
def sort_key_by_len_text(sort_dict):
    text_string = sort_dict["text"]
    result = len(re.findall(r'\w+', text_string))
    return result

result = sorted(data, key=sort_key_by_len_text, reverse = True)
print(result)