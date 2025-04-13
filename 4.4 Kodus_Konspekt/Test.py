listing = [["Apple","Orange","Banana","Kiwi"],["1","2","3","4"]]
print (listing)
print("_" * 20)
print (listing[0])
print("_" * 20)
#Выведет первый список из матрицы
print (listing[1])
print("_" * 20)
#Выведет первый элемент первого списка
print (listing[0][0])
print("_" * 20)
#Выведет первые элементы из обоих списков
print (listing[0][0],listing[1][0])
print("_" * 20)
#Выведет весь список
for fruit in listing:
    print(fruit)
print("_" * 20)
#Выведет первые элементы из обоих список
for fruit in listing:
    print(fruit[0])
print("_" * 20)
#Выведет первые символы элементов из обоих списков
for fruit in listing:
    print(fruit[0][0])
print("_" * 20)
#Выведет первый символ первого элемента в первом списке и первый символ первого элемента во втором списке
for fruit in listing:
    print (fruit[0])
    print (fruit[1])
print("_" * 20)
#Показывает только первый список
for fruit in range(0,1):
    print(listing[fruit])
print("_" * 20)
#Показывает только второй список
for fruit in range(1,2):
    print(listing[fruit])
print("_" * 20)
#Распакует первый список и распечатает без скобок
for fruit in range(0,1):
    for item in listing[fruit]:
        print(item)
print("_" * 20)
#Распечатает оба списка построчно
for fruit in range(len(listing)):
    for item in listing[fruit]:
        print(item)
print("_" * 20)
#Распечатает списки через тире, каждый элемент в своей строке
for fruit in range(len(listing[0])):
    print(f"{listing[0][fruit]} - {listing[1][fruit]}")
print("_" * 20)
#Красивая таблица. :<8 означает, что делается поле 8 между продолжением
print("Fruit    | Number")
print("-" *20)
for fruit in range (len(listing[0])):
    print(f"{listing[0][fruit]:<8} - {listing[1][fruit]}")
print("_" * 20)