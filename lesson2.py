name = "John"
age = 23
value = age / 2
# name = 123
print(name, age)

number = 1
another_number = 3
some_number = 5
name_form_server = "Jane"

print(name, type(name))
print(age, type(age))
print(value, type(value))


value = input("Введи целое число: ")
value = int(value)

value = input("Введи число с точкой: ")
value = float(value)
print(value * 2, type(value))

val_1 = 11
val_2 = -11
val_3 = 11.5
val_4 = -11.999

print(float(val_1), float(val_2), int(val_3), int(val_4))

# тип bool

bool_value = (421 != 42)  # ==    >    <    >=  <=   !=
bool_value = "qwy" in "qwerty"
print(bool_value, type(bool_value))

value = -100
print(bool(value))  # для int True все, кроме 0

value = 0.00000000000000000001
print(bool(value))  # для float True все, кроме 0.0

value = "False"
print(bool(value))  # для str True все, кроме ""


# if условие_1:
#     блок кода с отступом, (если уловие_1 верно)
#     ...
#     блок кода с отступом, (если уловие_1 верно)
# elif условие_2:
#     блок кода с отступом, (если уловие_2 верно)
#     ...
#     блок кода с отступом, (если уловие_2 верно)
# ...............................................
# elif условие_n:
#     блок кода с отступом, (если уловие_n верно)
#     ...
#     блок кода с отступом, (если уловие_n верно)
# else:
#     блок кода с отступом, (если уловие ложно)
#     ...
#     блок кода с отступом, (если уловие ложно)


value = 2001

if value > 100:
    print("Это число больше 100")
elif value < 100:
    print("Это число меньше 100")
else:
    print("Это число равно 100")

if value % 2 == 0:
    print("Четное число")
else:
    print("Нечетное число")

if value % 2 == 0 and value % 3 == 0:
    print("Число делится на 6")
else:
    print("Число не делится на 6")

# and   T   F
#  T    T   F
#  F    F   F

# or   T   F
#  T   T   T
#  F   T   F

# not
#  T  -> F
#  F -> T

value = input("Введи строку")
if not value or value == "qwerty":
    print('Wow!!!')