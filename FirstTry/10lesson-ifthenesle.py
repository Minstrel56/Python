
x = 25
if x == 25:
    print("Yes")
else:
    print("No")

age = int(input(''))
if age <= 4:
    print('So young')
elif age > 4 and age < 12:
    print('Too old')
elif age >= 12 and age < 18:
    print('You are not interesting to me')
else:
    print('You must be on graveyard')

all_cars = ['chrusler','dacia','bmw','KIA','vw','seat','skoda','lada','audi','ford', 'Chevrolette']
german_cars = ['bmw','vw','audi']

for xxx in all_cars:
    if xxx in german_cars:
        print(xxx+'is German car')
    else:
        print(xxx+'is not German car')
