""
""" 
1. Дан список строк my_list. Создать новый список в который поместить
элементы из my_list по следующему правилу:
Если строка стоит на нечетном месте в my_list, то ее заменить на
перевернутую строку. "qwe" на "ewq".
Если на четном - оставить без изменения.
Задание сделать с использованием enumerate.
"""
my_list = ['dog', 'maroon', 'cat', 'moon', 'life', 'gold']
new_list = []

for index, value in enumerate(my_list):
    if index % 2:  #нечетные позиции
        new_list.append(value[::-1])
    if not index % 2: #четные позиции
        new_list.append(value)
print(new_list)

print("-------------------------------------------------end-of-1")

"""
2. Дан список строк my_list. Создать новый список в который поместить
элементы из my_list у которых первый символ - буква "a".
"""

my_list = ['Adagio', 'apron', 'cat', 'Amen', 'life', 'gold']
letter = 'A'

new_list = [value for value in my_list if value[0].lower() == letter.lower()]

print(new_list)

print("-------------------------------------------------end-of-2")

""" 
3. Дан список строк my_list. Создать новый список в который поместить
элементы из my_list в которых есть символ - буква "a" на любом месте.
"""
my_list = ['Adagio', 'apron', 'cat', 'Amen', 'life', 'glad']
letter = 'A'

new_list = [value for value in my_list if letter.lower() in value.lower()]
print(new_list)

print("-------------------------------------------------end-of-3")

""" 
4. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
Создать новый список в который поместить только строки из my_list.
"""
my_list = ['Adagio', 123, 'apron', 56, 78, 'Amen', 9, 'life']
str_list = [value for value in my_list if type(value) == str]

print(str_list)

print("-------------------------------------------------end-of-4")

""" 
5. Дана строка my_str. Создать список в который поместить те символы из my_str,
которые встречаются в строке только один раз.
"""

my_str = "akjfhg fdkglhas dlkfjjdfg koireutp"

# for symbol in set(my_str):
#     # print(f"Symbol: {symbol} --> {my_str.count(symbol)}")
#     if my_str.count(symbol) == 1:
#         my_list.append(symbol)

my_list = [symbol for symbol in set(my_str) if my_str.count(symbol) == 1]
print(my_list)

print("-------------------------------------------------end-of-5")
"""
6. Даны две строки. Создать список в который поместить те символы,
которые есть в обеих строках хотя бы раз.
"""
my_str_1 = "wfgasdvkzhvkjhfjdgajsdfgkcn<kjskuqq"
my_str_2 = "qqqqqqqqqqqqqqaysfdjagsc<ncl<a"

my_set_1 = set(my_str_1)
my_set_2  = set(my_str_2)

result_set = my_set_1.intersection(my_set_2)
result_list = list(result_set)
print(result_list)

print("-------------------------------------------------end-of-6")

"""
7. Даны две строки. Создать список в который поместить те символы, 
которые есть в обеих строках, но в каждой только по одному разу.
быть в обеих строках - интерсекшн
проверить по счету
"""

my_str_1 = "wfertcb,mncxmnyuiopq dghdjhjk"
my_str_2 = "qccvbnbmnbm,"

my_set_1 = set(my_str_1)
my_set_2  = set(my_str_2)

both_sets = my_set_1.intersection(my_set_2)

new_list = list(both_sets)
print(new_list)

discard_list = []

for symbol in new_list:
    if my_str_1.count(symbol) > 1 or my_str_2.count(symbol) > 1:
        discard_list.append(symbol)
print(discard_list)

result = [symbol for symbol in new_list if symbol not in discard_list]
print(result)

print("-------------------------------------------------end-of-7")

"""
8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
Фамилия
Имя
Возраст
Проживание
    Страна
    Город
    Улица
Работа
    Наличие
    Должность
"""
my_dict = {"Last_name": "Roberts",
           "First_name": "Julia",
           "Age": 53,
           "Residence": {"Country": "USA",
                         "City": "San-Francisco",
                         "Street": "Main Street"},
           "Employment": {"Employed": "Yes",
                          "Occupation": "Actress/Producer"}}
print(my_dict)

print("-------------------------------------------------end-of-8")

"""
9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
придумать и указать граммы для продуктов):
Составляющие
    Коржи
        Мука
        Молоко
        Масло
        Яйцо
    Крем
        Сахар
        Масло
        Ваниль
        Сметана
    Глазурь
        Какао
        Сахар
        Масло
"""

new_dict = {"Коржи": {"Мука": "400 гр",
                      "Молоко": "200 мл",
                      "Масло": "200 гр",
                      "Яйцо": "5 штук"},
            "Крем": {"Сахар": "150 гр",
                     "Масло": "100 гр",
                     "Ваниль": "20 гр",
                     "Сметана":"200 гр"},
            "Глазурь": {"Какао": "200 гр",
                        "Сахар": "200 гр",
                        "Масло": "100 гр"}}
print(new_dict)

print("-------------------------------------------------end-of-9")