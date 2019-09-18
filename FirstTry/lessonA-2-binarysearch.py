## бинарный поиск

#mylist = [10, 12, 14, 15, 20, 27, 33, 44, 51, 57, 68, 70]

def binsearch(mylist, whatsearch, start, stop):
    if start > stop:
        return False
    else:
        mid = (start+stop)//2  ## // Деление нацело
        if whatsearch == mylist[mid]:
            return mid
        elif whatsearch < mylist[mid]:
            return binsearch(mylist, whatsearch, start, mid-1)
        else:
            return binsearch(mylist, whatsearch, mid+1, stop)

mylist = [10, 12, 14, 15, 20, 27, 33, 44, 51, 57, 68, 70]

whatsearch = 20
start = 0
stop = len(mylist)

x = binsearch(mylist, whatsearch, start, stop)

if x == False:
    print('Item ', whatsearch, ' not found!')
else:
    print('Item ', whatsearch, ' found at index ', x)

x=0
whatsearch = 70
for ind in mylist:        ### обычный поиск по всему массиву
    if whatsearch == ind:
        print('Item ', whatsearch, ' found at index ', x)
    if len(mylist) == x+1 and whatsearch != ind:
        print('Item ', whatsearch, ' not found!')
    x+=1