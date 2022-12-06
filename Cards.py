import random
from typing import Union

class Menus:
    def playerchoice(self) -> Union[int, None]:
        try:
            print("What stat are you choosing?")
            print("____________________________")
            print("1:     Species")
            print("2:     Strength")
            print("3:     Defence")
            print("4:     Runic")
            print("5:     Vitality")
            print("6:     Luck")
            print("7      Cooldown")
            return int(input("___________________________"))
        except ValueError:
            print("Invalid Option!!!")
            return

class Base(object):
    def __init__(self, species = None, strength: int = 0, defence: int = 0, runic: int = 0, vitality: int = 0, luck: int = 0, cooldown: int = 0, side = "Mutual"):
        self.species = species
        self.strength = strength
        self.defence = defence
        self.runic = runic
        self.vitality = vitality
        self.luck = luck
        self.cooldown = cooldown
        self.side = side

class Gods(Base):
    def __init__(self, *args):
        super().__init__(species="God", *args)


class Giants(Base):
    def __init__(self, *args):
        super().__init__(species="Giant", *args)


class Dwarfs(Base):
    def __init__(self, *args):
        super().__init__(species="Dwarfs", *args)


class Valkyries(Base):
    def __init__(self, *args):
        super().__init__(species="Valkries", *args)

class Elfs(Base):
    def __init__(self, *args):
        super().__init__(species="Elfs", *args)
        
class Cards(object):
    def __init__(self, players: list):
        self.players = players
        self.LIMIT_EACH = 22 // len(self.players)
        self.LIMIT_TOTAL = self.LIMIT_EACH * len(self.players)
        self.Cards = [] # will be all of the cards within this game
        self.Player_Cards = {} # cards for each player represented as player no: [cards, ...]
        self.Temp_Cards = [] # cards which they have placed down this will be [cards, ...] which the winner will take
        self.generate() # will generate the cards for each player randomly
        

    def Generate_Cards(self) -> list: # makes a full list of cards
        pass
