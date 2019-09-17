import re

mytext = "Gavin, 795 5921, 11/12/2019,Reus, azaza@mail.ru," \
        "Isaac, 0500 517975, 04/27/2020, Solapur, 123ololo@yahoo.com," \
        "Robert, (029) 2168 5531, 05/04/2020, Fayetteville, xxxXX22@gmail.com,"  \
        "Jasper, (027) 6817 3812, 02/03/2020, Oberpullendorf, 123qweASD@gmail.com,  "  \
        "Amos, (01424) 542082, 02/13/2020, Lacombe County123qwe, myname@mydomain.biz,"

"""  ### что искать
\d  = Any Digig 0-9   = [0-9][3] ищет 3 любых стоящих подряд цифры
\D  = Any non Digit 
\w  = Any Alphabet [A-Z a-z]
\W  = Any non alphabet 
\s  = breakspace
\S  = non space

"""

textlookfor= r"\d\d\d"  #ищет все 3 стоящих подряд цифры
allresults = re.findall(textlookfor, mytext)
print(allresults)
print(re.findall(r"[0-9][2]", mytext)) # выводит все значение состоящие из 2 указаных цифр подряд
print(re.findall(r"\w{6}", mytext)) # выводит все значение состоящие из 6 символов подряд
print(re.findall(r"[A-Z][a-z]+", mytext)) # выводит все значение начинающиеся с заглавной буквы и до конца букв в County123qwe пишется только County
print(re.findall(r"\@\w+\.\w+", mytext)) ## вывод всех почтовиков