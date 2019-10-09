#----
# Ctrl+/ for block comment in pycharm
#----

def funct1(x):
    return x**2

def perimeter(a,b,c):
    return a+b+c

def hollow():
    return "Abyss"

def check(v):
    if v > 0:
        return "Positive"
    else: return "Negative"

def mass(x):
    return x%10   #### берет последнюю цифру

ma = [1214,2148,15,764,5000,67473]
mb = ma.copy()
ma.sort(key=mass)   ### сортирует по условию(ключу) из функции масс, берет последнюю цифру и выстраивает от меньшей к большей
mb.sort(key=lambda mbx: mbx%10)  #### тоже что и mass

sqrt = lambda x: x**2    ### работает так же как и функция funct1 - возводит в квадрат
perim = lambda a,b,c: a+b+c   ### работает так же как и функция perimeter - находит периметр
oblivion = lambda : "Blach Hole" ### работает так же как и функция hollow - не принимает аргументов и делает вывод
realizeif = lambda b: "Positive" if b > 0 else "Negative"   ## тоже что и check, сначала ретёрн True, потом условия потом иначе

print(ma)
print(mb)

print(funct1(3))
print(sqrt(4))

print(perimeter(3,4,6))
print(perim(3,4,6))

print(hollow())
print(oblivion())

print(check(5))
print(realizeif(-4))