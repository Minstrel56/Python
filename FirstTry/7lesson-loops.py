for x in range(0,100 + 1):    # от 0 до 99 и еще 1 раз
    print(x)

for x in range(100, 0, -2):    # от 0 до 99 c шагом 2 (чётные)
    print(x)
    if x == 50:
        break

print("EOF")

x = 1
while True:
    print(x)
    x = x+1
    if x == 10000:
        break