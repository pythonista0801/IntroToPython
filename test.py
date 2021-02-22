import random as rnd
import string

def random_string(min_limit: int, max_limit: int):
    selection = [rnd.choice(string.ascii_lowercase) for i in range(rnd.randint(min_limit, max_limit))]
    str = ''.join(selection)
    return str

print(random_string(35, 70))