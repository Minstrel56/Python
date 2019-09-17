
def pechat_privetstvie(name):
    'Print Privetstvie'  #комментарий к функции
    print("Hello friend " + name)


def cumma(x ,y):
    print(x + y)
    s = x+y
    return s  # возвращяет наружу s и прекращяет выполнение дальше
    print(x+y)

def cumma2(x,y):
    return x+y

def factorial(x):
    "Calculate factorial of X"
    otvet = 1
    for i in range(1, x+1):   # считать до X , т.к. считает не до X а на 1  меньше, то нужно добавить 1
        otvet*=i
    return otvet


#----
print('-=-=-=-=-')

pechat_privetstvie('Peta')
pechat_privetstvie('Boba')

cumma(33,22)
x = cumma(31,22)
print(x)

cumma2(11,15)
y=cumma2(11,15)
print(y)

print(factorial(1))
print(factorial(5))
print(factorial(10))
print('-------')

for x1 in range(1,10):
    print(str(x1) + "!\t = " + str(factorial(x1)))