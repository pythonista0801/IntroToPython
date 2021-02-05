""
"""1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран: 2"""
#
# my_str = "blablacar"
# my_symbol="bla"
#
# number = my_str.count(my_symbol)
# print(number)

"""
2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать столько раз my_symbol, сколько он встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
bla
bla
"""

# my_str = "blablacar"
# my_symbol= "bla"
#
# # for i in range(my_str.count(my_symbol)):
# #     print(my_symbol)
#
# result = (my_symbol + '\n') * my_str.count(my_symbol)
# result = result.strip()
# print(result)

"""
3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько 
РАЗНЫХ символов встречается в my_str. 
Большая и маленькая буква считается как один символ. 
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car". 
Вывод на экран: 6"""

#not the right solution, need not count big and small letters as different symbols.
# Besides, the correct way is to work with the strings, not the list!
# my_str="bla BLA car"
# my_list = list(my_str)
# print(my_list)
# result = []
#
# for value in my_list:
#     if value not in result:
#         result.append(value)
# length = len(result)
# print(length)
"----------------------------------------"
#
# my_str="bla BLA car"
# my_str_upper = my_str.upper()
# print(my_str_upper)
# unique_symbols = ""
#
# for value in my_str_upper:
#     if value not in unique_symbols:
#         unique_symbols += value
# print(unique_symbols)
# result = len(unique_symbols)
# print(result)

"-----------------------------------------------"

"""
4)
Дана строка my_str и пустой список my_list.
Заполнить my_list символами из my_str, 
которые стоят на четных местах в строке (считаем с 0)
"""
# my_str = "bla bla bla car"
# my_list = []

#First way to solve the problem, but! you can work with a string too:
# new_list = list(my_str)

# for index, value in enumerate(new_list):
#     if not index % 2:
#         my_list.append(value)
# print(my_list)
"-----------------------------------------------------"
#Without creating the list

# for index, symbol in enumerate(my_str):
#     if not index % 2:
#         my_list.append(symbol)
# print(my_list)
"------------------------------------------------------"
#2е решение, используя четные позиции в срезе:
# for symbol in my_str[::2]:
#     my_list.append(symbol)
# print(my_list)

"""
5)
Дана строка my_str, список str_index целых чисел в диапазоне от 
0 до длинны строки минус 1, пустой список my_list.
Заполнить my_list символами из my_str, которые стоят на местах с 
индекса
"""
# my_str = "test string"
# str_index = [2, 4, 10, 5, 1, 1, 3, 5, 6, 7]
# my_list = []
#
# for index in str_index:
#     value = my_str[index]
#     my_list.append(value)
# print(my_list)

"""
6) Super hard to solve...! Studying the code only!.. wasn't so hard after all...
Даны списки my_list_1 и my_list_2.
Создать список my_result в который поместить элементы из my_list_1 и 
my_list_2 через один, начиная с my_list_1.
a) кол-во эл-тов одинаковое
б) кол-во эл-тов разное. Оставшиеся дописать в конец.
"""
# my_list_1 = [1,2,3,4,5]
# my_list_2 = [10,20,30,40,50]
# my_result = []
#
# for index in range(len(my_list_1)):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
# print(my_result)
# "----------------------------------------------------"
# my_list_1 = [1,2,3]
# my_list_2 = [10,20,30,40,50]
# my_result = []
#
# length_1 = len(my_list_1)
# length_2 = len(my_list_2)
#
# if length_1 > length_2:
#     my_list_1, my_list_2 = my_list_2, my_list_1
#
# for index in range(length_1):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
# my_result.extend(my_list_2[length_1:])
# print(my_result)


"""
Training session complete:
Need to remember three ways to work with for cycles, with value, index, and a pair of them.
The majority of the problems is solved only one of these ways!!
With index we are looking at the range of length!
With value - taking it from a string!
With a pair of them - looking at enumerate.
"""

"""Дан список чисел, необходимо удалить все вхождения числа 20 из него."""
# my_list1 = [20, 30, 20, 50, 20, 70]
# my_list2 = []
#
# for index in range(len(my_list1)):
#     if my_list1[index] != 20:
#         my_list1.pop(index)
#         print(my_list1)