def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    text = text.split(' ')
    return text[0]


print(first_word("Hello World!"))


def count_zeros(num: int) -> int:
    reverse_string = str(num)[::-1]
    result = 0
    for index in range(len(reverse_string)):
        if reverse_string[index] != '0':
            break
        else:
            result += 1
    return result


mystring = "Hello World!"
mystring = mystring[::-1]
print(mystring)


def is_all_upper(text: str) -> bool:
    try:
        if len(text) == 0:
            return True
        elif text.isspace():
            return True
        else:
            return text.isupper()
    # except len(text) == 0:
    #     return True
    # except text.isspace():
    #     return True
    except ValueError:
        return True


print(type("55 555 5"))

from typing import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    if len(items) > 1:
        last_element = items.pop()
        items.insert(0, last_element)
        return items
    else:
        return items


my_list = [1, 2, 3, 4, 5, 6, 7]

last_element = my_list.pop()
print(last_element)
my_list.insert(0, last_element)
print(my_list)

print(replace_first(my_list))

number = 2593600
result = sorted(str(number), reverse=True)
print(result)
max_digit = int(result[0])
print(max_digit)


def split_pairs(a):
    # your code here
    length = len(a)
    if length % 2:
        a = a + '_'
    else:
        pass
    new_list = []
    for i in range(0, length, 2):
        new_list.append(a[i: i + 2])
    return new_list


print(list(split_pairs('abc')))


def beginning_zeros(number: str) -> int:
    count = 0
    for symbol in number:
        if symbol == '0':
            count += 1
        else:
            break
    return count


print(beginning_zeros('000000012000'))


def nearest_value(values: set, one: int) -> int:
    # your code here
    pass

#--------------------------------------------------------------
test_tuple = ({4, 7, 10, 11, 12, 17}, 9)

my_set = test_tuple[0]
#my_value = test_tuple[1]
# my_list = list(my_set)
my_list = [-2,0]
my_value = -1

abs_diff_function = lambda list_value: abs(list_value - my_value)
closest_value = min(my_list, key=abs_diff_function)

print(closest_value)

# print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

#------------------------------------------------------------
def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    begin_index = text.find(begin)
    end_index = text.rfind(end)
    substring = text[begin_index+1:end_index]
    return substring

#-----------------------------------------------------------------

def correct_sentence(text: str) -> str:
    # your code here
    # if text[0].isupper:
    #     pass
    # else:
    text = text[0].upper() + text[1:]
    if text[-1] == '.':
        pass
    else:
        text = text + '.'
    return text

print(correct_sentence('hello world'))

#--------------------------------------------------------------



