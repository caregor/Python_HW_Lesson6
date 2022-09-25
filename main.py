# Задача 1
# my_range = int(input('Введите число: '))
# my_list = []
# for n in range(1,my_range):
#     tmp = (1 + 1 / n) ** n
#     my_list.append(tmp)
# print(my_list)
# print()
# summa = 0
# for value in my_list:
#     summa += value
# print(f'Сумма значений списка: {summa}')
#
# Новый вариант

# my_range = int(input('Введите число: '))
# my_list = [(1 + 1 / n) ** n for n in range(1, my_range)]
# print(my_list,'\n',f'Сумма значений списка: {sum(my_list)}')

# Задача №2
# a = input('Введите число:')
# res = 0
# for i in a:
#     if i.isdecimal():
#         res = int(i) + res
# print(res)
#
# Новый вариант

# print(sum(map(lambda res: int(res) if res.isdecimal() else 0,a)))

# Задача №5

# k = int(input('k = '))
# tmp = 0
# result = []
# fibonacci = [0, 1]
#
# for i in range(k - 1):
#     tmp = fibonacci[i] + fibonacci[i + 1]
#     fibonacci.append(tmp)
#     if i % 2 == 0:
#         result.append(-tmp)
#     else:
#         result.append(tmp)
# result.reverse()
# result.extend(fibonacci)
# print(result)
############################

# Новый вариант

# k = int(input('k = '))
# fib = lambda n: fib(n - 1) + fib(n - 2) if n > 1 else 1
# tmp = 0
# result = []
# fibonacci = [0]
# for i in range(k - 1):
#     tmp = fib(i)
#     fibonacci.append(tmp)
#     if i % 2 == 0:
#         result.append(-tmp)
#     else:
#         result.append(tmp)
# result.reverse()
# result.extend(fibonacci)
# print(result)
