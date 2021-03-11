""
"""1. Дано целое число (int). Определить сколько нулей в этом числе."""

number = 1200000001
my_digit = '0'
result = str(number).count(my_digit)
print(result)

"""2. Дано целое число (int). Определить сколько нулей в конце этого числа."""

number = 1200100000
reverse_string = str(number)[::-1]

result = 0
length = len(reverse_string)

for index in range(length):
    if reverse_string[index] != '0':
        break
    else:
        result += 1
print(result)

"""3a. Даны списки my_list_1 и my_list_2.
Создать список my_result в который вначале поместить
элементы на четных местах из my_list_1, 
а потом все элементы на нечетных местах из my_list_2."""

my_list_1 = [1, 2, 3, 4, 5, 6, 7]
my_list_2 = [2, 4, 6, 8, 10, 12, 14]
my_result = []

for index, symbol in enumerate(my_list_1):
    if not index % 2:
        my_result.append(symbol)
print(my_result)

for index, symbol in enumerate(my_list_2):
    if index % 2:
        my_result.append(symbol)
print(my_result)


"""3b. Даны списки my_list_1 и my_list_2. Создать список my_result в который
вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 
и потом нечетные элементы из my_list_2.
my_list_1 = [1,3,2,4,5], my_list_2 = [10, 20, 15, 25, 22] 
-> my_result [2, 4, 15, 25]"""

my_list_1 = [1, 2, 4, 5, 6, 7, 8]
my_list_2 = [2, 5, 7, 8, 9, 11, 12]
my_result = []

for value in my_list_1:
    if not value % 2:
        my_result.append(value)
print(my_result)

for value in my_list_2:
    if value % 2:
        my_result.append(value)
print(my_result)


"""4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент 
из my_list стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]"""

my_list = [11, 2, 3, 5, 6, 8]

first_symbol = [my_list[0]]
new_list = my_list[1:] + first_symbol
print(new_list)

"""5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
[1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)"""

my_list = [11, 2, 3, 5, 6, 8]

first_symbol = my_list.pop(0)
my_list.append(first_symbol)

print(my_list)

"""6. Дана строка в которой есть числа (разделяются пробелами).
Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
Для данного примера ответ - 133."""

my_string = "56 is greater than 23 but less than 78"
my_list = my_string.split()
print(my_list)
numbers = []

for value in my_list:
    if value.isdigit():
        value = int(value)
        numbers.append(value)
print(numbers)

result = sum(numbers)
print(result)


"""7. Дана строка my_str. Разделите эту строку на пары 
из двух символов и поместите эти пары в список.
Если строка содержит нечетное количество символов, пропущенный 
второй символ последней пары должен быть заменен подчеркиванием ('_'). 
Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']"""

my_str = "aaldfjlaflfdkgj lakjflksjalfk alskfjlkajl"
length = len(my_str)
print(length)

if length % 2:
    my_str = my_str + "_"
print(my_str)

my_list = []

for index in range(0, length, 2):
    my_list.append(my_str[index: index*2+2])
print(my_list)

# for index in range(length):
#     my_list.append(my_str[index*2: index*2+2])
# print(my_list)
"""8. Дана строка my_str в которой символы не повторяются 
и два символа l_limit, r_limit, которые точно находятся в этой строке. 
Причем l_limit левее чем r_limit. В переменную sub_str поместить 
часть строки между этими символами. my_str = "My_long str", 
l_limit = "o", r_limit = "t" -> sub_str = "ng s" """

my_string = 'Asdfgh.jkl_ertyui-xcnb'
l_limit = 'f'
r_limit = 'x'
l_limit_place = my_string.find(l_limit)
r_limit_place = my_string.find(r_limit)
sub_string = my_string[l_limit_place:r_limit_place]
print(f"Переменная sub_string с {l_limit_place} по {r_limit_place} места: {sub_string}")


"""9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin"."""

my_string = "It's a very fascinating but difficult homework, indeed!"
l_limit = 'a'
r_limit = 'w'
l_limit_place = my_string.find(l_limit) # возвращает номер первого вхождения
r_limit_place = my_string.rfind(r_limit) # возвращает номер последнего вхождения

print(l_limit_place)
print(r_limit_place)

sub_string = my_string[l_limit_place:r_limit_place]
print(f"Переменная sub_string с {l_limit_place} по {r_limit_place} места: {sub_string}")


"""10. Дан список чисел. Определите, сколько в этом списке элементов,
которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ 
КОЛИЧЕСТВО таких элементов. Крайние элементы списка никогда не учитываются, 
поскольку у них недостаточно соседей.
Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0."""

my_list = [2, 3, 9, 2, 5, 8, 1, 6, 8, 1, 2]
length = len(my_list)
print(length)

result = []

for index in range(length-2):
    if my_list[index + 1] > my_list[index] + my_list[index + 2]:
        result.append(my_list[index+1])
print(result)

number_of_elements = len(result)
print(number_of_elements)
