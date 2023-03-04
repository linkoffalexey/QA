# МАТЕМАТИЧЕСКИЕ ОПЕРАЦИИ
# 1
# x = '25'
# x = int(x)
# print(x+25)

# 2
# x = int(input())
# y = int(input())
# print(x+y)

# 3

# x = int(input())
# y = int(input())
# print(x*60+y)

# СТРОКИ
# print('abc ' '\n' 'bbc')
# print("abc "*3)
# print(len("abc "))


# 1
# x = input()
# y = input()
# print(x, y)

# 2
# x = input()
# y = input()
# print(len(x) + len(y))

# 3

# x = input("Сделайте первый вклад:")
# y = input("Сделайте второй вклад:")
# n = int(input("Насколько преумножить вклады:"))
# print("Ваши вклады преумножены:", (x+y)*n)

"""Логические операции"""

# 1

# a,b,c,d = False, True, False, True
# print(a and b and (not c or d))

# 2

# x = int(input("Введите первое число:"))
# y = int(input("Введите второе число:"))
# print(x > y)

'''Условия if/elif/else (1/3)'''

# 1

# x = int(input("Введите первое число:"))
# y = int(input("Введите второе число:"))
#
# if x + y > 10:
#     print("Сумма больше")
# elif x + y < 10:
#     print("Сумма меньше")
# else:
#     print("Сумма равна")

# 2

# x = int(input("Введите целое число:"))
#
# if x > 0:
#     print(1)
# elif x < 0:
#     print(-1)
# else:
#     print(0)

# 3

# x = int(input("Введите первое число:"))
# y = int(input("Введите второе число:"))
# if x > y:
#     print(y)
# elif x == y:
#     print("Числа совпадают")
# else:
#     print(x)

"""Задачи по всем материалам"""

# 1
#
# name = input("Ваше имя:")
# profession = input("Ваша профессия:")
# age = input("Ваш возраст:")
# print("Имя: " + name + "\n" + "Профессия: " + profession + "\n" + "Возраст: " + age)

# 2

# x = int(input("Введите первое число:"))
# y = int(input("Введите второе число:"))
# z = int(input("Введите третье число:"))
# n = int(input("Введите четвертое число:"))
# print((x+y)/(z+n))

# 3

# x = int(input("Введите первое число:"))
# y = int(input("Введите второе число:"))
# z = int(input("Введите третье число:"))
# if x > y > z:
#     print(x)
# elif y > x > z:
#     print(y)
# else:
#     print(z)

# 4

# x = int(input("Введите первое число:"))
# y = int(input("Введите второе число:"))
# z = int(input("Введите третье число:"))
# if z > y > x:
#     print(y)
# if y > x > z:
#     print(x)
# if x > z > y:
#     print(z)
# if y > z > x:
#     print(z)
# if z > x > y:
#     print(x)
# if x > y > z:
#     print(y)

# 5
# x = int(input("Введите целое число:"))
# print("Следующее число для числа " + str(x) + " это " + str(x+1))
# print("Предыдущее число для числа " + str(x) + " это " + str(x-1))

# 6
# print("Нужно купить хлеб стоимостью 30 рублей, молоко стоимостью 50 рублей и сыр стоимостью 100 рублей")
# bread = 30
# milk = 50
# cheese = 100
# sum = int(input("Сколько у вас денег?"))
# if sum - bread - milk - cheese == 0:
#     print("Спасибо, что без сдачи!")
# elif sum - bread - milk - cheese > 0:
#     print("Стоимость товаров: " + str(bread + milk + cheese) + " руб")
#     print("Ваша сдача: " + str(sum - bread - milk - cheese) + " руб")
# else:
#     print("Недостаточно денег")

""""Дополнительная задача"""

x = int(input("Сколько рекомендуется бегать:"))
y = int(input("Сколько не рекомендуется бегать:"))
z = int(input("Сколько Маша фактически бегает:"))
if y >= z >= x:
    print("Дистанция в норме!")
elif x > z:
    print("Слишком мало бегаете")
else:
    print("Много бегать вредно")
