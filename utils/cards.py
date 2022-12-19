from random import shuffle, sample, choice
from typing import Union


# class Menus:
#     def playerchoice(self) -> Union[int, None]:
#         try:
#             print("What stat are you choosing?")
#             print("____________________________")
#             print("1:     Species")
#             print("2:     Strength")
#             print("3:     Defence")
#             print("4:     Runic")
#             print("5:     Vitality")
#             print("6:     Luck")
#             print("7:     Cooldown")
#             return int(input("___________________________"))
#         except ValueError:
#             print("Invalid Option!!!")
#             return


class Base(object):
    def __init__(self, species=None, strength: int = 0, defence: int = 0, runic: int = 0,
                 vitality: int = 0, luck: int = 0, cooldown: int = 0, side="Mutual"):
        self.species = species
        self.strength = strength
        self.defence = defence
        self.runic = runic
        self.vitality = vitality
        self.luck = luck
        self.cooldown = cooldown
        self.side = side


class Gods(Base):
    def __init__(self, **kwargs):
        super().__init__(species="God", **kwargs)


class Giants(Base):
    def __init__(self, **kwargs):
        super().__init__(species="Giant", **kwargs)


class Dwarfs(Base):
    def __init__(self, **kwargs):
        super().__init__(species="Dwarfs", **kwargs)


class Valkyries(Base):
    def __init__(self, **kwargs):
        super().__init__(species="Valkries", **kwargs)


class Elfs(Base):
    def __init__(self, **kwargs):
        super().__init__(species="Elfs", **kwargs)


class Kratos(Gods):
    """
    Kratos is a Spartan warrior, who becomes known as the "Ghost of Sparta" 
    and given the title of "God of War" of the Greek Pantheon
    In the Norse Realm he does his best to redeem himself and be close to his son.
    """
    def __init__(self):
        super().__init__(strength=326, defence=346, runic=257, vitality=200, luck=156, cooldown=204, side="Giants")


class Atreus(Gods):
    """
    Atreus is the son of Kratos and Faye.
    He is the secondary protagonist of God of War Ragnarök.
    To the Jötnar, he is known as Loki, Champion of the Jötnar and God of Mischief.
    """
    def __init__(self):
        super().__init__(strength=134, defence=154, runic=321, vitality=250, luck=200, cooldown=175, side="Giants")


class Odin(Gods):
    """
    Odin is the All-father and Raven God. His sons are Thor and Baldur.
    He seeks knowledge, power, and control to somehow change his fate during Ragnarok.
    """
    def __init__(self):
        super().__init__(strength=300, defence=290, runic=350, vitality=198, luck=78, cooldown=150, side="Aesir")


class Thor(Gods):
    """
    Thor is the God of Thunder and the son of Odin.
    His brother is Baldur. He is the father to Magni and Modi.
    """
    def __init__(self):
        super().__init__(strength=325, defence=345, runic=100, vitality=150, luck=97, cooldown=120, side="Aesir")


class Heimdall(Gods):
    """
    Heimdall is the Norse God of Foresight, Surveillance, Order and Foreknowledge.
    He is a son of Odin.
    """
    def __init__(self):
        super().__init__(strength=230, defence=270, runic=245, vitality=197, luck=47, cooldown=30, side="Aesir")


class Freya(Gods):
    """
    Freya is the Vanir Goddess of Love, Beauty, War, Death and Fertility.
    She is the sister of Freyr, and the ex-wife of Odin with whom she procreated Baldur, 
    She was former leader of the Vanir during the Aesir-Vanir War and Queen of the Valkyries
    """
    def __init__(self):
        super().__init__(strength=275, defence=297, runic=400, vitality=154, luck=64, cooldown=60, side="Giants")


class Freyr(Gods):
    """
    Freyr, also known as Yngvi, is the Vanir God of Rain and Fertility. 
    He is the brother of Freya, and the uncle of Baldur.
    """
    def __init__(self):
        super().__init__(strength=295, defence=243, runic=365, vitality=179, cooldown=42, side="Giants")


class Tyr(Gods):
    """
    Týr is the Aesir God of War, Law, Justice, and Honor.
    He is a son of Odin, younger brother of Thor
    """
    def __init__(self):
        super().__init__(strength=321, defence=331, runic=256, vitality=173, cooldown=21, side="Giants")

class Cards(object):
    def __init__(self, players: list):
        self.players = players
        self.Cards = [Kratos(), Atreus(), Odin(), Thor(), Heimdall(), Freya(), Freyr(), Tyr()]
        self.Temp_Deck = {}
        self.Player_Decs = {}
        self.choices = {1: "strength", 2: "defence", 3:"runic", 4:"vitality", 5:"luck", 6:"cooldown"}
        self.current_choice = None

    def generate_deck(self):
        self.PLAYER_CARDS_LMT = 8 // len(self.players) #22 // len(players)
        self.MAX_CARDS_LMT = self.PLAYER_CARDS_LMT * len(self.players)
        shuffle(self.Cards)
        self.Cards[:self.MAX_CARDS_LMT]
        copy = self.Cards[:]
        for p in self.players:
            s = sample(copy, self.PLAYER_CARDS_LMT)
            self.Player_Decs[p] = s
            for i in s:
                copy.remove(i)

    def cards_for(self, player: str) -> list:
        return self.Player_Decs.get(player, [])
    
    def add_to_temp(self, player: str, card_index: int):
        card = self.Player_Decs[player][card_index]
        res = self.Temp_Deck.get(player, None)
        if res == None:
            self.Temp_Deck[player] = card
        #self.Temp_Deck[player].append(card)
        del self.Player_Decs[player][card_index]
    
    def temp_to_player(self, player: str):
        self.Player_Decs[player].extend(list(self.Temp_Deck.values()))
        self.Temp_Deck = {}
    
    def cards_len(self, player) -> int:
        return len(self.cards_for(player))
    
    def choose_attribute(self) -> str:
        res = choice(list(self.choices.keys()))
        self.current_choice = res
        return self.choices[res]
    
    def compare(self) -> str:
        temp = []
        for player in self.Temp_Deck:
            temp.append(self.Temp_Deck[player])
        attr = self.choices[self.current_choice]
        best: Base = temp[0]
        for card in temp[1:]:
            if self.current_choice == 8:
                if card.__getattribute__(attr) < best.__getattribute__(attr):
                    best = card
            else:
                if card.__getattribute__(attr) > best.__getattribute__(attr):
                    best = card

        for player in self.Temp_Deck:
            card = self.Temp_Deck[player]
            if card == best:
                return player  
