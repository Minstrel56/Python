#!/bin/python3

#----
# Ctrl+/ for block comment in pycharm
#----

import shutil ### for copy file
import os     ### for get file size and check if file exist
import sys    ### for Comand line instrument

####  lessonA-4-logfilesclean.py Files/LogFile.txt 5 5   (5 килобайт и 5 файлов)

if(len(sys.argv) < 4): ### проверка на количество аргументов
    print('Missing arguments: Usage is > script.py file 10(kb) 5(files)')
    exit(1)  ### если не введены все аргументы, выйти с ошибкой

file_name = sys.argv[1]
limitsize = int(sys.argv[2])   #### in kilobytes
logsnumber = int(sys.argv[3])

if (os.path.isfile(file_name) == True):  ### check if Main log file exist
    logfilesize = os.stat(file_name).st_size   ### get file size in byte
    logfilesize = logfilesize/1024              ### convert from bytes to kilobytes

    if(logfilesize >= limitsize):
        if(logsnumber > 0):
            for currentFileNum in range(logsnumber, 1, -1):   ### для количества от logsnumber до 1 проверяет наличие предыдущего файла и копирует
                source = file_name + "_" + str(currentFileNum-1)
                destination = file_name+ "_" + str(currentFileNum)
                if(os.path.isfile(source) == True):
                    shutil.copyfile(source, destination)
                    print("Copied: " +source+" to" + destination)
            shutil.copyfile(file_name, file_name+"_1")
            print("Copied: "+file_name+" to "+ file_name+"_1")
        myfile = open(file_name, 'w')  ## открывает файл на запись
        myfile.close()                 ## даже если ничего не произошло, но файл был открыт на запись, он будет пустым
