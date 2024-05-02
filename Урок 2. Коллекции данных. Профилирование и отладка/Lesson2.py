# Список - это упорядоченный конечный набор элементов. давайте разбиратся,
# по сути список - это тот же саммый масиив,в котором моэно хранить элементы
# любых типовых данных

# list_1 = [] # Создание пустого списка
# list_2 = list() # Создание пустого списка
# list_1 = [7, 9, 11, 13, 15, 17]

# # В списках существует нумерция которая начинается
# # с 0, чтобы вывести первый элемент списка воспользуемся следующей
# # конструкцией :

# list_1 = [7, 9, 11, 13, 15, 17]
# print (list_1 [0]) # 7
# print(*list_1) # Без скобок вывод

# for i in list_1:
#     print(i)

# print(len(list_1))

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8) # Добавление элемента в конец списка
# print(list_1)
# list_1 = []

# for i in range (5):
#     list_1.append(i)
#     print(list_1)

# Метод pop удаляет последний элемент из списка:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]

# t = ()
# print(type(t))
# t = (1, )
# print(type(t))
# v = {1, 8, 9}
# print(*v)
# print(type(v))
# v = tuple(v)
# print(*v)
# print(type(v))

# a,b,c = v
# print(a, b, c)

# t = (1, 2, 3, 5)

# t[0] = 2

# d = {}         # Создание словаря
# d = dict()

# d['q'] = 'qwerty'

# d["w"] = "werty"

# print(d['q'])

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}

# print(dictionary.items())

# # for item in dictionary:
# #         print("{} : {}".format(item, dictionary[item]))

# for k,v in dictionary.items():
#     print(k,v)

# Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
# Одно множество может содержать значения любых типов. Если у Вас есть два множества,
# Вы можете совершать над ними любые стандартные операции, например, объединение,
# пересечение и разность. Давайте разберем их.
# colors = {'red', 'green', 'blue'}

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# # print(colors) # {'red', 'green', 'blue','gray'}
# # colors.remove('red')
# # print(colors) # {'green', 'blue','gray'}
# colors.discard('red') # ok

list_1 = [i for i in range(1, 101)]
print(list_1)