usersfile = "Files/users.txt"
passfile = "Files/passwords.txt"
outputfile = "Files/out_passwords.txt"

# https://docs.python.org/2.4/lib/standard-encodings.html список кодировок

myfile = open(usersfile, mode='r', encoding='utf_8')
myfile2 = open(passfile, mode='r', encoding='latin_1')
outfile = open(outputfile, mode='w', encoding='latin_1')  # если файла нет должен создаться, и обнуляет его - w

for num, line in enumerate(myfile, 1):   ### в num добавляются значения строк из myfile (начало по умолчанию 0) начиная с 1
    if "Malone" in line:
        print("Line №: " + str(num) +" : "+ line.strip())

n=0
for num, line in enumerate(myfile2, 1):
    if "penis" in line:
        print("Line №: " + str(num) +" : "+ line.strip())
        n+=1
print(n)

myfile2 = open(passfile, mode='r', encoding='latin_1')
lookingpass = 'penis'
for num, line in enumerate(myfile2, 1):
    if lookingpass in line:
        outfile.write("Found password: "+lookingpass+" in pass: "+ line.strip() +" on " +str(num)+ ' string\n')

outfile.close()
outfile = open(outputfile, mode='a', encoding='latin_1')  ### a - append добавить в конец файла
outfile.write("END")

myfile.close()
myfile2.close()
outfile.close()
