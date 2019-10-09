def tickets(people):
    b=[0,0,0]
    for i in people:
        if i == 25:
            b[0]+=1
        elif i == 50 and b[0] >= 1:
            b[0]-=1
            b[1]+=2
        elif i == 100 and (b[0]+b[1])>=3 and b[0]>=1:
            if b[1] >= 2:
                b[0]-=1
                b[1]-=2
                b[2]+=4
            else:
                b[0]-=3
                b[2]+=4
        else:
            return "NO"
    return "YES"
