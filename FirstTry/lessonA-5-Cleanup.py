#----
# Ctrl+/ for block comment in pycharm
#----

import os, time

days = 5   ### maximal age of file to stay, older will be deleted
folders = [
            "F:\Projects\Python\FirstTry\Files\Trash\Musor/",
            "Files\Trash\Old/",
]
print(folders)
total_deleted_size = 0    #### total deleted size(in Bytes), files and empty folders
total_deleted_file = 0
total_deleted_dirs = 0

nowtime = time.time()  ### время в секундах
agetime = nowtime - 60*60*24*days   ### вычисляем время старых файлов секунды*минуты*часы*дни в секундах

def delete_old_files(folder):
    """Delete files older than X days"""
    global total_deleted_file   ### использует внешние переменные а не функции
    global total_deleted_size
    for path, dirs , files, in os.walk(folder):  ### считывает все файлы и папки внутри указаной дириктории
        for file in files:
            filename = os.path.join(path, file)  ### передает полный путь до файла (путь + имя)
            filetime = os.path.getmtime(filename)   ### передает время последней модификации файла в секундах
            if filetime < agetime:
                sizefile = os.path.getsize(filename)
                total_deleted_size += sizefile   ### считает сумму размера всех удаленных файлов/освобожденного места
                total_deleted_file +=1  ### считает количества всех удаленных файлов
                print("Deleted file: "+str(filename))
                os.remove(filename)   ### удаление файла

def delete_empty_dirs(folder):
    global total_deleted_dirs
    x = total_deleted_dirs
    for path, dirs, files, in os.walk(folder):
        if (not dirs) and (not files) and (path != folder): ### проверка на пустую дирикторию, кроме родительского каталога
            total_deleted_dirs +=1
            print("Deleted empty dir: "+str(path))
            os.rmdir(path)
    if x != total_deleted_dirs:  ### если удалился хоть 1 каталог, то запускает еще раз, что бы попытаться заново проверить родителя
        delete_empty_dirs(folder)
#=================
starttime = time.asctime()
for folder in folders:
    delete_old_files(folder)    ### delete old files and empty folders
    delete_empty_dirs(folder)

finishtime = time.asctime()
print("Start time: "+str(starttime)+" End time: "+str(finishtime))
print('Total deleted size: '    +str(int(total_deleted_size/1024/1024))+" MB")
print("Total deleted files: "   +str(total_deleted_file))
print("Total deleted folders: " +str(total_deleted_dirs))
print("-----------EOF-----------")