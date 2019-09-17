#         0     1      2        3        4
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
for car in cars:
    print(car.title())

for x in range(1, 6):
    print(x)

number_list = list(range(0, 10))
print(number_list)

for x in number_list:
    x = x*2
    print(x)

number_list.sort(reverse=True)
print(number_list)

print("Max number is: "+ str(max(number_list)))
print("Min number is: "+ str(min(number_list)))
print("Sum number is: "+ str(sum(number_list)))

#         0     1      2        3        4
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

mycars = cars[1:3]
print(mycars)
mycars = cars[:4]
print(mycars)
mycars = cars[:]
print(mycars)
mycars = cars[-3:5]
print(mycars)


mycars = cars
print(str(cars) + "     " + str(mycars))
cars.append('Oka')
print(str(cars) + "     " + str(mycars))

mycars = cars[:]
cars.pop()
print(str(cars) + "     " + str(mycars))
