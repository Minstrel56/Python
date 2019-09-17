## https://regex101.com/   Cайт для тренировки и составления Регулярных Выражений
## http://www.generatedata.com/   Сайт генератор демо данных
##

import re
filename = "Files/randomdata.txt"
resultname = 'Files/resultfile.txt'
inputfile = open(filename, mode='r')
resultfile = open(resultname, mode='w', encoding='Latin1')

lookfor = r'[\w.-]+@(?!Quisque.edu)[A-Za-z-]+\.[\w.]+' ## отсортировка всех емейлов за исключением Quisque.edu (?!<фильтр>)
mytext = inputfile.read() # считывает весь файл и переносит его в переменную
results = re.findall(lookfor, mytext)

print(str(len(results)))
for email in results:
    print(email)
    resultfile.write(email + '\n')

resultfile.close()