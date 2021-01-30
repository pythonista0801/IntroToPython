"----Задача №1----"

value = input("Введите число: ")
value = int(value)

if value % 5 == 0:
    print(value * 2)
else:
    print(0)

###########################################################
"----Задача №2----"

value = input("Введите месяц года числом: ")

if value == '01' or value == '1':
    print("В этом месяце 31 день")
elif value == '02' or value == '2':
    print ("В этом месяце 28 дней")
elif value == '03' or value == '3':
    print ("В этом месяце 31 день")
elif value == '04' or value == '4':
    print ("В этом месяце 30 дней")
elif value == '05' or value == '5':
    print ("В этом месяце 31 день")
elif value == '06' or value == '6':
    print ("В этом месяце 30 дней")
elif value == '07' or value == '7':
    print ("В этом месяце 31 дней")
elif value == '08' or value == '8':
    print ("В этом месяце 31 дней")
elif value == '09' or value == '9':
    print ("В этом месяце 30 дней")
elif value == '10':
    print ("В этом месяце 31 день")
elif value == '11':
    print ("В этом месяце 30 дней")
elif value == '12':
    print ("В этом месяце 31 день и конец года!")
else:
    print ("Вы ввели неправильный месяц. Попробуйте снова!")


############################################################
"-----Задача№3-----"

value = input("Введите месяц года текстом: ")

if value == 'Январь' or value == 'январь':
    print("В этом месяце 31 день")
elif value == 'Февраль' or value == 'февраль':
    print ("В этом месяце 28 дней")
elif value == 'Март' or value == 'март':
    print ("В этом месяце 31 день")
elif value == 'Апрель' or value == 'апрель':
    print ("В этом месяце 30 дней")
elif value == 'Май' or value == 'май':
    print ("В этом месяце 31 день")
elif value == 'Июнь' or value == 'июнь':
    print ("В этом месяце 30 дней")
elif value == 'Июль' or value == 'июль':
    print ("В этом месяце 31 день")
elif value == 'Август' or value == 'август':
    print ("В этом месяце 31 день")
elif value == 'Сентябрь' or value == 'сентябрь':
    print ("В этом месяце 30 дней")
elif value == 'Октябрь' or value == 'октябрь':
    print ("В этом месяце 31 день")
elif value == 'Ноябрь' or value == 'ноябрь':
    print ("В этом месяце 30 дней")
elif value == 'Декабрь' or value == 'декабрь':
    print ("В этом месяце 31 день и конец года!")
else:
    print ("Вы ввели неправильный месяц. Попробуйте снова!")

