values = (1,2,3,4,5)
values = list(values)
print(type(values))

values = [1,2,3,4,5]
values = tuple(values)
print(type(values))

values = [1,2,3,4,5]
result = []
for value in values:
    result.append(value)
print(result)

values = [1,2,3,4,5]
result = []
for value in values[::-1]:
    result.append(value)
print(result)

values = [1,2,3,4,5]
print(len(values))

values = [1,2,3,4,5]
new_value = values + values[::-1]
print(new_value)
# [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

values = [1,2,3,4,5]
new_value = values
new_value.append(6)
print(values)
# [1, 2, 3, 4, 5, 6]

values = [1,2,3,4,5]
new_value = values.copy()
new_value.append(6)
print(values)
# [1, 2, 3, 4, 5]

values = [0] * 6
values[0] = 1
print(values)
# [1, 0, 0, 0, 0, 0]

value = 0
values = [value] * 6
value = 1
print(values)
# [0, 0, 0, 0, 0, 0]

my_list = [0]
values = [my_list] * 3
print(values)
# [[0], [0], [0]]

my_list = [0]
values = [my_list] * 3
my_list.append(1)
print(values)
# [[0, 1], [0, 1], [0, 1]]

my_list = [0]
values = [my_list.copy()] * 3
my_list.append(1)
print(values)
# [[0], [0], [0]]

my_list = ["a", "b", "c", "d", "e", "f"]
my_str = "_".join(my_list)
print(my_str)

my_list = ["a", "b", "c", "d", "e", "f"]
my_str = "_".join(my_list[::-1])
print(my_str)

my_list = ["a", "b", "c", "d", "e", "f"]
my_str = "".join(my_list[::2])
print(my_str)