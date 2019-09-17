from lesson17_hero import *

myhero = Hero('Vurdalak',4,"Orc")
mysuperhero = SuperHero("Moisha",10,"Human", 5)

myhero.show_hero()
mysuperhero.show_hero()
mysuperhero.usemagic()
mysuperhero.show_hero()

mysuperhero.__magic = 20
mysuperhero.__magic = 10  #### из-за того что класс назван self.__magic - он не может меняться таким образом, нужно делать отдельный метод для замены
mysuperhero.show_hero()