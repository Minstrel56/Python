cities = ['New Your', 'Moscow', 'new dehli', 'Simferopol', 'Toronto']

print(cities)
print(len(cities)) # вывод длины массива

print(cities[0])    # печать отпеределенного учстка массива
print(cities[-1])    # печать последнего участа массива
print(cities[2].title())

cities[3] = 'Tula'
print(cities)

cities.append('Kursk') # добавление в конец массива
print(cities)

cities.insert(0, 'Orel')
cities.insert(2, 'Ufa')  #указание в какой именно индекс добавть данные
print(cities)


del cities[-2]   # удаляет 2й элемент массива с конца
print(cities)

cities.remove('Tula')   # удаляет первую Тулу найденую в массиве
print(cities)

deleted_city = cities.pop()
print("Deleted city is: "+deleted_city)
print(cities)

cities.sort() # сортировка по алфавиту
print(cities)

cities.sort(reverse=True)  # сортировка по алфавиту наоборот
print(cities)

cities.reverse()  # меняет массив наоборот
print(cities)
