
######## факториал
def fac(x):
    y = 1
    for i in range(1, x+1):
        y*=i
    return y
print(str(fac(20)))

############ поиск гипотенузы из 2х катетов   pow(12 , 0.5) это корень   pow(x,y) x-число y-степень

print(pow((179**2+971**2),0.5))

############ ряд лейбница

print(4/1-4/3+4/5-4/7+4/9-4/11+4/13-4/15+4/17-4/19)

def leib(y,x):
    s = 1  ### step
    r = 0
    for i in range(1, x+1):
        r += y/s
        s += 2
        y *= -1
    return r
print(leib(4,10))

############

