import json
filename = "Files/user_settingsless21.txt"
myfile = open(filename, mode='w', encoding='utf_8')
print(myfile)

player1 = {
    'PlayerName': "Donald Trump",
    'Score': 345,
    'Awards': ["Origon", "Nevada", "New York"],
    'Bussiness': 'Yes',
}

player2 = {
    'PlayerName': "Hillary Clinton",
    'Score': 348,
    'Awards': ["Washington", "Texas", "Missouri"],
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)
### print(myplayers)

####

json.dump(myplayers, myfile) # добавляет и сохраняет данные их myplayers в файл myfile

myfile = open(filename, mode='r')
jsondata = json.load(myfile)  # читает всё из файла и добавляет в переменную jsondata
print(jsondata)
print("+++++++++++++++++++++")

for user in jsondata:
    print('Player: ' +str(user['PlayerName']))
    print('Score: '+str(user['Score']))
    x=1
    for award in user['Awards']:   #### считает количество данных в user['Awards'] и столько раз выполняет цикл
        print('Award №'+str(x)+ " " + award, end=' ')   ###  , end=' ' позволяет печатать в той же строке а не на новой
        x+=1
    print()
print("+++++++++++++++++++++")

# for user in jsondata:                              # не работает потому что award ходит не по строке user['Awards']
#     print('Player: ' +str(user['PlayerName']))     #  а по user где содержимое это плейре нейм авардс скор
#     print('Score: '+str(user['Score']))          # и если значений в словаре больше чем элементов в массиве то
#     x=0                                          # то попытка прочитать из несуществующего элемента массива выдает ошибку
#     for award in user:
#         print(user['Awards'][x])
#         x=x+1

myfile.close()
