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

path = "C:\\Users\\CNata\\PycharmProjects\\IntroToPython\\"

# files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
# print(files)
#
# for file in sorted(files):
#     file_path = os.path.join(path, file)

with open(os.path.join(path, "names.txt"), "r") as file_txt:
    lines = file_txt.readlines()
    result = []
    for line in lines:
        result.append(line.split('\t')[1])
    print(result)

""" 
2. Создать функцию для записи в файл json.
Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
(можно с повторениями символов).
Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
такая же, как и вероятность того, что будет типа float или типа bool.
"""

def create_my_dict():
    keys = []
    values = []
    for i in range(random.randint(5, 20)):
        list = [random.randint(-100, 100), random.random(), random.choice([True, False])]
        selection = [random.choice(string.ascii_lowercase) for n in range(5)]
        keys.append(''.join(selection))
        values.append(random.choice(list))
    my_dict = dict(zip(keys, values))
    return my_dict

my_dict = create_my_dict()
print(my_dict)

def write_json(filename, my_dict):
    filename = "my_dict_write.json"
    with open(filename, "w") as js_file:
        json.dump(my_dict, js_file, indent=2)


# print(type(json.dumps(data)))


"""
3. Написать функцию generate_and_write_json которая принимает один параметр - полный путь к файлу.
Cгенерировать данные для записи с помощью функции из пункта 2 и записать в данный файл.
"""
