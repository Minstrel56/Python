#----
# Ctrl+/ for block comment in pycharm
#----

def duplicate_encode(word):
    #your code here
    z=''
    for i in word:
        x=0
        for y in word:
            if i.lower() == y.lower():
              x+=1
        if x > 1:
            z+=')'
        else:
            z+='('
    return z

print(duplicate_encode("din")) ### == (((
print(duplicate_encode("recede"))  ### === ()()()
print(duplicate_encode("Success"))   #### ===  )())())
print(duplicate_encode("(( @"))     ####  ==   ))((