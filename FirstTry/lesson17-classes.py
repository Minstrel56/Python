from lesson17_hero import *   ### иморт класса из файла
###### START

myhero1= Hero('Arkadiy',5,"Ork")
myhero2= Hero('Chuchelo',4,"Human")

myhero1.show_hero()
myhero2.move()

myhero1.level_up()
myhero1.show_hero()

myhero1.health = 80 ##  лучше так не делать а менять через методы#
myhero1.show_hero()
myhero1.change_health(95) ### вот так
myhero1.show_hero()
