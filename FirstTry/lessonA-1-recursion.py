
def privet(x):
    if x==0:
        return
    else:
        print("Hi")
        privet(x-1)

####  sum 0+1+2+3+4+5+..+n
def sum(y):
    if y < 0:
        return("Value must be more than 0")
    elif y == 0:
        return 0
    else:
        return y + sum(y-1)

### factorial 5!=1*2*3*4*..*n
def fac(z):
    if z < 0:
        return("Factorial must be more than 0")
    elif z == 0:   ## факториал 0 равен 1
        return 1
    else:
        return z*fac(z-1)

def fibo(f):
    if f < 0:
        return("Fibonacci must be more than 0")
    elif f == 0:
        return 0
    elif f == 1:
        return 1
    else:
        return fibo(f-1)+fibo(f-2)



privet(2)

sum1 = sum(4)
print(sum1)

print(str(fac(-4)))

fi = 20
fibo(fi)
print("Fibonacci for %d = "% fi + str(fibo(fi)))   ### %d форматирование для вывода десятичного числа из fi