#----
# Ctrl+/ for block comment in pycharm
#----

oldlist = [10, 75, 43, 15, 25, -4, 27]

def bubble(mylist):
    lastitem = len(mylist)-1
    for z in range(0, lastitem):
        for x in range(0, lastitem-z):   ### из-за -z он не ходит до последнего массива, т.к. там уже максимальное число и делает меньше шагов
            print(mylist)
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]  ### замена местами элементов массива
    return mylist

print('Original list', oldlist)
newlist = bubble(oldlist).copy() ## делает копию массива
print('New list: ',newlist)
