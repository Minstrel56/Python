def duplicate_encode(word):
    #your code here
    y=''
    for i in word:
        x=0
 #       print(i)
        for z in word:
            if i.lower() == z.lower():
                x+=1
        if x > 1:
            y+=")"
        else:
            y+="("
    print(y)

duplicate_encode("Success")