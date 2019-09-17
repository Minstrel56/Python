

# name = input('Please enter your name: ')
# print('Hi '+name)
#
# num1 = input('Number 1: ')
# num2 = input('Number 2: ')
# print(int(num1)+int(num2))  #---- перевод строки в интеджер и складывание
# age = int(input(''))
message = ''

while True:
    message = input('Enter password: ')
    if message == 'secret':
        break
    print(message + ' - Password not correct')

print('---------------------')
wrongpasswd = 0
while message != 'secret' and wrongpasswd != 3 :

    if message != 'secret' :
        print(message+' - Password not correct')
        wrongpasswd += 1
        continue
    print('Hello')
if wrongpasswd == 3:
    print('You are banned')

for wrongpasswd in range(1,3):
    message = input('Enter password: ')
    if message == 'secret':
        print('Hello')
        break
    print('You are banned')


mylist = []
while message.upper() != 'STOP':   # пока не будет введен любой стоп (маленькие большие буквы - не важно)
    message = input('Enter new item (Print STOP to finish): ')
    mylist.append(message)

print(mylist)