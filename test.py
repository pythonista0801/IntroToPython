import json
import random
import string

"""
3. Написать функцию generate_and_write_json которая принимает один параметр - полный путь к файлу.
Cгенерировать данные для записи с помощью функции из пункта 2 и записать в данный файл.
"""
# def write_txt(file_path, data):
#     with open(file_path, "w") as txt_file:
#         txt_file.writelines(data)

path = "C:\\Users\\CNata\\PycharmProjects\\IntroToPython\\"

filepath = "C:\\Users\\CNata\\PycharmProjects\\IntroToPython\\my_dict.json"

def generate_and_write_json(filepath):
    keys = []
    values = []

    with open(filepath, "w") as my_json:
        json.dump(my_dict, my_json)
    # return filepath

generate_and_write_json(filepath)

filename = "my_dict_write.json"
with open(filename, "w") as js_file:
    json.dump(my_dict, js_file, indent = 2)

file_path='/tmp/student_data.json'
    with open(file_path, 'w') as outfile:
        print("writing file to: ",file_path)
        # HERE IS WHERE THE MAGIC HAPPENS
        json.dump(student_data, outfile)


