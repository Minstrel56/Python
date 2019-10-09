#----
# Ctrl+/ for block comment in pycharm
#----

def sqInRect(lng, wdth):
    m=[]
    x=0
    if lng == wdth or lng<=0 or wdth <= 0:
        return None
    while lng>=1 and wdth>=1:
        if lng > wdth:
            x = lng//wdth
            for i in range (x):
                m.append(wdth)
            lng-=wdth*x
        elif lng < wdth:
            x = wdth//lng
            for i in range (x):
                m.append(lng)
            wdth-=lng*x
    return m

print(sqInRect(5, 5), None)
print(sqInRect(5, 3), [3, 2, 1, 1])
print(sqInRect(6250, 250), [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250])
print(sqInRect(731 , 230), [230, 230, 230, 41, 41, 41, 41, 41, 25, 16, 9, 7, 2, 2, 2, 1, 1])

