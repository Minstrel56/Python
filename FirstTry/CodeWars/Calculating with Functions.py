#----
# Ctrl+/ for block comment in pycharm
#----
def zero(x=''):
    if not x: return 0
    else: return eval(str(0)+x)
def one(x=''):
    if not x: return 1
    else: return eval(str(1)+x)
def two(x=''):
    if not x: return 2
    else: return eval(str(2)+x)
def three(x=''):
    if not x: return 3
    else: return eval(str(3)+x)
def four(x=''):
    if not x: return 4
    else: return eval(str(4)+x)
def five(x=''):
    if not x: return 5
    else: return eval(str(5)+x)
def six(x=''):
    if not x: return 6
    else: return eval(str(6)+x)
def seven(x=''):
    if not x: return 7
    else: return eval(str(7)+x)
def eight(x=''):
    if not x: return 8
    else: return eval(str(8)+x)
def nine(x=''):
    if not x: return 9
    else: return eval(str(9)+x)

def plus(x):
    return '+'+str(x)
def minus(x):
    return '-'+str(x)
def times(x):
    return '*'+str(x)
def divided_by(x):
    return '//'+str(x)  ### Деление нацело

print(seven(times(five())), 35)
print(four(plus(nine())), 13)
print(eight(minus(three())), 5)
print(six(divided_by(two())), 3)