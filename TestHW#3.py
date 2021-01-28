# www = 'www.google.com'
# if "com" in www:
#     print("com in www")
# else:
#     print("com not in www")

#### answer: com in www

# www = 'www.command_and_conquer.com'
# if "com" in www:
#     print("com in www")
# else:
#     print("com not in www")
#### answer: com in www

# www = 'www.command_and_conquer.net'
# if "com" in www:
#     print("com in www")
# else:
#     print("com not in www")
#### answer: com in www

# www = 'www.command_and_conquer.net'
# if ".com" in www:
#     print("com in www")
# else:
#     print("com not in www")
#### answer: com in www

# www = 'www.conquer_and_command.net'
# if ".com" in www:
#     print("com in www")
# else:
#     print("com not in www")

#### answer: com not in www

# value = 123
# my_str = str(value) if value < 200 else str(value % 10)
# print(my_str)

# value = 321
# my_str = str(value) if value < 200 else str(value) [::-1]
# print(my_str)
### answer: 123

# value = "123456789"
# my_str = value if len(value) <= 5 else value[2:5:2]
# print(my_str[::-1])

my_str = "My name is Vova. I am a teacher !"

# for symbol in my_str:
#     print(symbol)

# for symbol in my_str:
#     if symbol in 'eyuioa':
#         print(symbol)

# for symbol in my_str:
#     if symbol in 'EYUIOA':
#         print(symbol)

# for symbol in my_str:
#     if symbol.isupper():
#         print(symbol)

for symbol in my_str:
    if not symbol.isupper() and symbol.isalpha():
        print(symbol)


