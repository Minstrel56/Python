class Hero():
    """Class to create hero for our game"""
    def __init__(self, name, lvl, race):                        # класс всегда начинается с метода (функции) инит
        """initiate of our hero"""
        self.name = name
        self.lvl = lvl
        self.race = race
        self.health = 100

    def show_hero(self):
        """Print all parameters of this hero"""
        discription = (self.name + " level is: " + str(self.lvl) + " race is: " + self.race + " Health = " + str(self.health))
        print(discription)

    def level_up(self):
        """Upgrade lvl of hero"""
        self.lvl += 1

    def move(self):
        """Start moving hero"""
        print("Hero "+self.name + " start moving")

    def change_health(self, new_health):
        """Change health of hero"""
        self.health = new_health

class SuperHero(Hero):    #### наследие из другого класса в скобках
    """Class to create Superhero"""
    def __init__(self, name, lvl, race, magiclvl):   #### инициализация класса хиро
        """"initiate our superhero"""
        super().__init__(name,lvl,race)  ### перекидывание данных из  функции хиро
        self.magiclvl = magiclvl
        self.__magic = 100

    def usemagic(self):
        """Use magic"""
        self.__magic -= 10

    def show_hero(self):
        """Print all parameters of this hero"""
        discription = (self.name + " level is: " + str(self.lvl) + " race is: " + self.race + " Health = " + str(self.health)+
                       " Magic level is: " +str(self.magiclvl) + " Mana is: " + str(self.__magic)).title()
        print(discription)