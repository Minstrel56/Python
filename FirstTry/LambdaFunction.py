#----
# Ctrl+/ for block comment in pycharm
#----

def funct1(x):
    return x**2

def perimeter(a,b,c):
    return a+b+c

def hollow():
    return "Abyss"

sqrt = lambda x: x**2    ### работает так же как и функция funct1 - возводит в квадрат

perim = lambda a,b,c: a+b+c   ### работает так же как и функция perimeter - находит периметр

oblivion = lambda : "Blach Hole" ### работает так же как и функция hollow - не принимает аргументов и делает вывод


print(funct1(3))
print(sqrt(4))

print(perimeter(3,4,6))
print(perim(3,4,6))

print(hollow())
print(oblivion())