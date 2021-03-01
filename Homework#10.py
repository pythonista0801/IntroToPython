""""""
import csv
import json
"""
1. Написать функцию read_file которая принимает один параметр - полный путь к файлу.
В зависимости от расширения файла (txt, csv, json) считывает и возвращает данные из файла.
Для csv использовать reader.
Если расширение не соответствует заданным, то вывести текст "Unsupported file format"
"""


def read_file(file_path):
    extension = file_path.rsplit('.',1)[-1]
    if extension == "txt":
        with open(file_path, 'r') as txt_file:
             data = []
             for line in txt_file.readlines():
                 data.append(line)
        return data
    elif extension == "csv":
        with open(file_path, 'r') as csv_file:
            data = []
            reader = csv.reader(csv_file, delimiter = ';')
            for row in reader:
                data.append(row)
        return data
    elif extension == "json":
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    else:
        print("Unsupported file format")


file_path = "names.txt"
data = read_file(file_path)
print(data)

file_path = "my_dict_function.json"
data = read_file(file_path)
print(data)

file_path = "hw10.csv"
data = read_file(file_path)
print(data)

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

def write_file(filename, data):
    extension = filename.rsplit(".", 1)[-1]
    if extension == "txt":
        with open(filename, "w") as txt_file:
            txt_file.writelines(data)
    elif extension == "json":
        with open(filename, "w") as json_file:
            json.dump(data, json_file, indent = 2)
    elif extension == "csv":
        with open(filename,"w", encoding="utf-8") as csv_file:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(data)
    else:
        print("Unsupported file format")


data = "aajgkajhakfj aljhlgkjhaskjf ;adlkfkajhfkajdh"
filename = "newhw10.txt"
write_file(filename, data)
print(read_file("newhw10.txt"))

write_file(filename, "I hope that works out well")
print(read_file("newhw10.txt"))

dictionary = {"name": "John",
              "age": 35,
              "city": "Dnipro",
              "country": "Ukraine",
              "job": "Developer"}
filename = "newhw10.json"
write_file(filename, data = dictionary)
print(read_file("newhw10.json"))

dictionary = [{'Year': 1981, 'Length': 120, 'Title': 'Who knows', 'Subject': 'Horror', 'Actor': 'Famous', 'Actress': 'Charlize Theron', 'Director': 'Al Pacino', 'Popularity': 75, 'Awards': 'No', 'Image': 'none.jpg'}]
filename = "newhw10.csv"
write_file(filename, data=dictionary)
print(read_file(filename))
