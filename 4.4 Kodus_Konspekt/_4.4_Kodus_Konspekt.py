
# Создание различных списков
letters = ["a", "b", "c"]  # Список из строковых символов
matrix = [[0, 1], [2, 3]]  # Двумерный список (матрица)
zeros = [0] * 5  # Список из пяти нулей: [0, 0, 0, 0, 0]
combined = zeros + letters  # Объединение списков
numbers = list(range(20))  # Создание списка чисел от 0 до 19
chars = list("Hello World")  # Преобразование строки в список символов

# Вывод созданных списков
print(numbers)  # Выводит числа от 0 до 19
print(chars)  # Выводит список символов строки "Hello World"
print(combined)  # Вывод объединённого списка (нули + буквы)
print(matrix)  # Вывод двумерного списка
print(letters)  # Вывод списка букв
print(len(chars))  # Выводит количество символов в списке chars

# Изменение элементов списка
letters = ["a", "b", "c", "d"]
letters[0] = "A"  # Меняем первый элемент "a" на "A"

# Срезы списка (slice)
print(letters[0:3])  # Вывод элементов с 0 по 2 (не включая 3)
print(letters[0:])  # Вывод всех элементов списка
print(letters[:])  # Вывод всех элементов (копия списка)
print(letters[::2])  # Каждый второй элемент списка
print(letters)  # Вывод обновлённого списка

# Работа со списком чисел
numbers = list(range(20))
print(numbers[::2])  # Каждый второй элемент (чётные числа)
print(numbers[::-1])  # Разворачиваем список в обратном порядке

# Распаковка списка (unpacking)
numbers = [1, 2, 3]
first, second, third = numbers  # Присваиваем переменным значения из списка
first, second, *other = numbers  # *other забирает оставшиеся элементы

# Альтернативное присваивание элементов списка
first = numbers[0]
second = numbers[1]
third = numbers[2]

# Вывод значений после распаковки
print(first)  # Выводит первый элемент (1)
print(other)  # Выводит оставшиеся элементы после второго (пустой список, так как всего 3 элемента)

# Кортеж и распаковка его значений
letters = ["a", "b", "c"]
items = (0, "a")  # Кортеж (число и буква)
index, letter = items  # Распаковка кортежа

# Использование enumerate для получения индексов и значений
for letter in enumerate(letters):
    print(index, letter)  # ОШИБКА! Должно быть `for index, letter in enumerate(letters):`

# Добавление элементов в список
letters.append("d")  # Добавляет "d" в конец списка
letters.insert(0, "_")  # Вставляет "_" в начало списка
print(letters)  # Выводит список после добавления элементов

# Удаление элементов
letters.pop(0)  # Удаляет элемент с индексом 0 (первый элемент)
letters.remove("b")  # Удаляет первое вхождение "b" из списка
# del letters[0:3]  # ОШИБКА в коде (переменная названа неправильно)
letters.clear()  # Очищает список полностью
print(letters)  # Вывод пустого списка

# Поиск индекса элемента
letters = ["a", "b", "c"]
letters.count("d")  # Подсчитывает, сколько раз "d" встречается в списке (вернёт 0)
print(letters.index("d"))  # ОШИБКА! "d" нет в списке, выдаст ValueError
# Поиск минимального и макс числа
numbers = [10, 5, 23, 45, 78, 2]
print(max(numbers))  # 78 (наибольшее число)
print(min(numbers))  # 2 (наименьшее число)
# Поиск сколько раз встречается в списке
letters = ["a", "b", "a", "c", "a", "b"]
print(letters.count("a"))  # 3 (буква "a" встречается трижды)

elementid = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
element = elemtid[0][2]
print(element)

loend_hulgad = [
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
]
otsitav_element = 3
for hulk in loend_hulgad:
    if otsitav_element in hulk:
        print("Leidimse elemendi", otsitav_element, "hulgast:", hulk)

