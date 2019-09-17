import sys  ### импортирование системной библиотеки

filename = "Files/lesson20_1.txt"

while True:
    try:    ############  запуск команды с проверкой на ошибку
        print('Open try')
        myfile = open(filename, mode='r')
    except Exception:    ############ если ошибка есть - выполняется
        print("inside Except")
        print('Error found: '+ str(sys.exc_info()[1]))   #### выводит ошибку на экран
        filename = input("Input correct file name (Files/lesson20.txt): ")
    ##### sys.exit()   ### выход из программы, почему то всё равно отрабатывает файнали
    else:   ########## если ошибки нет - выполняется
        print('Inside Else')
        print(myfile.read())
        break
    finally:    ###### Всгда запускается
        print("Inside Finally")


print("======EOF=======")
sys.exit()
print("======EOF=======")

###myfile = open(filename, mode='r')

####print(myfile.read())