#----
# Ctrl+/ for block comment in pycharm
#----

def five(x=''):
    if not x: return 5
    else: return eval(str(5)+x)

def seven(x=''):
    if not x: return 7
    else: return eval(str(7)+x)

def plus(x=''):
    return '+'+str(x)

def ad12(x=''):
    if not x:
        return 0
    else: return x

print(five(plus(seven())))
print(ad12(33))
print(type(''))

ff=22
y=str(ff)+'+56'
print(eval(y))

x=print(1)
print(x)



x=bool('+')
ff=22
y=eval('+56')
print(y)

print(zero(plus(one())))

print('11'+x+'223')
print(plus(3))
print('2''+''3')
print(('0')+('1'))
print(zero(plus(one())))
print(zero(zero(0)))
print((0)+(0))
print('2''+''3')
print(one())