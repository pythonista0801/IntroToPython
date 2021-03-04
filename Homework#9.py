""""""

"""
1. Считать данные из файла names.txt и поместить в список только фамилии из файла.
Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
Фамилия находится всегда на одной и той же позиции в строке.
"""
import os
import json
import random
import string

path = "C:\\Users\\CNata\\PycharmProjects\\IntroToPython\\names.txt"

# files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
# print(files)
#
# for file in sorted(files):
#     file_path = os.path.join(path, file)


def read_last_names(path):
    with open(path, "r") as file_txt:
        lines = file_txt.readlines()
        result = []
        for line in lines:
            result.append(line.split('\t')[1])
    return result


last_names = read_last_names(path)
print(last_names)

""" 
2. Создать функцию для записи в файл json.
Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
(можно с повторениями символов).
Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
такая же, как и вероятность того, что будет типа float или типа bool.
"""
filename = "my_dict_write.json"


def write_json_file(filename, my_dict):
    with open(filename, "w") as js_file:
        json.dump(my_dict, js_file, indent=2)


def random_key():
    selection = [random.choice(string.ascii_lowercase) for n in range(5)]
    return ''.join(selection)


def random_value():
    value = random.choice(["int", "float", "bool"])
    if value == "int":
        value = random.randint(-100, 100)
    elif value == "float":
        value = random.random()
    elif value == "bool":
        value = random.choice([True, False])
    return value


def create_my_dict():
    return {random_key(): random_value() for k in range(random.randint(5, 20))}


my_dict = create_my_dict()
print(my_dict)


"""
3. Написать функцию generate_and_write_json которая принимает один параметр - полный путь к файлу.
Cгенерировать данные для записи с помощью функции из пункта 2 и записать в данный файл.
"""

filepath = "C:\\Users\\CNata\\PycharmProjects\\IntroToPython\\my_dict_function.json"


def generate_and_write_json(filepath):
    with open(filepath, "w") as new_file:
        json.dump(create_my_dict(), new_file, indent=2)

generate_and_write_json(filepath)

