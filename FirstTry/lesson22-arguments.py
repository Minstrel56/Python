import sys,os

print('Hello')
print(sys.argv)  ### при запуске программы из командной строки например
# F:\PythonProject\FirstTry>python lesson22-arguments.py 123 fwege 123
# будет вывод ['lesson22-arguments.py', '123', 'fwege', '123']

x=len(sys.argv)
if x > 1:
    if sys.argv[1] == "/?":
        print('Help requested')
        print('print arguments after program name: <program name> <arg1> <arg2>')
    print('Arguments entered: ' + str(sys.argv[1:]).strip('['+']').replace("'","")) ## выводит введеные аргументы, кроме
    # имени файла и удаляет лишние знаки
else:
    print("Arguments not provided")

# if os.path.isfile(myfile):
#     os.remove(myfile)
# else:    ## Show an error ##
#     print("Error: %s file not found" % myfile)

TestD='TestDir'
if os.path.isdir('TestDir'):
    os.rmdir('TestDir')
    print('%s was deleted' % TestD)
if os.path.isfile('test.txt'):
    os.remove('test.txt')
    print('test.txt was deleted')

os.mkdir('TestDir')
os.system("dir > test.txt")  ## выполняет команды из оболочки ОС (dir в win - вывод содержимого каталога
#os.rmdir('TestDir')
#os.remove('test.txt') # os.remove() удаляет файл. os.rmdir() удаляет пустой каталог. shutil.rmtree() удаляет каталог и все его содержимое.
sys.exit(2)  ## выводит код выхода 2 (по умолчанию при удачном выполнении - 0, при неудачном - 1)