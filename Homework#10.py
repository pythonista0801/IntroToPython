""""""
"""
1. Написать функцию read_file которая принимает один параметр - полный путь к файлу.
В зависимости от расширения файла (txt, csv, json) считывает и возвращает данные из файла.
Для csv использовать reader.
Если расширение не соответствует заданным, то вывести текст "Unsupported file format"
"""
import csv
import json

def read_file(filepath):
    extension = filepath.rsplit('.',1)[-1]
    if extension == "txt":
        with open(filepath, 'r') as txt_file:
             data = []
             for line in txt_file.readlines():
                 data.append(line)
        return data
    elif extension == "csv":
        with open(filepath, 'r') as csv_file:
            data = []
            reader = csv.reader(csv_file, delimeter = ',')
            for row in reader:
                data.append(row)
        return data
    elif extension == "json":
        with open(filepath, 'r') as json_file:
            data = json.load(json_file)
        return data
    else:
        print("Unsupported file format")




# def write_file(filename, data):
#     extension = filename.rsplit(".", 1)[-1]
#     if extension == "txt":
#         write_txt(filename, data)

"""
2. Написать функцию write_file которая принимает два параметра - полный путь к файлу и данные.
В зависимости от расширения файла (txt, csv, json) записывает данные в данный файл.
Для csv использовать DictWriter.
Если расширение не соответствует заданным, то вывести текст "Unsupported file format"

Данные для записи и файлы создать самим. Файлы с результатами добавить в гит.
"""