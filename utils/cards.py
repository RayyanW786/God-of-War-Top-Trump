from random import shuffle, sample
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
            print("7:     Cooldown")
            return int(input("___________________________"))
        except ValueError:
            print("Invalid Option!!!")
            return


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
    Kratos is a Spartan warrior, who becomes known as the "Ghost of Sparta" and given the title of "God of War" of the Greek Pantheon
    In the Norse Realm he does his best to redeem himself and be close to his son.
    The God of War is to be taken seriously!
    """
    def __init__(self):
        super().__init__(strength=326, defence=346, runic=257, vitality=200, luck=156, cooldown=204, side="Giants")


class Atreus(Gods):
    """
    Atreus (Greek: Ἀτρεύς) is the son of Kratos and Faye. He is the deuteragonist of God of War (2018) and the secondary protagonist of God of War Ragnarök.
    To the Jötnar, he is known as Loki (Nordic: ᛚᛟᚲᛁ), Champion of the Jötnar and God of Mischief.
    """
    def __init__(self):
        super().__init__(strength=134, defence=154, runic=321, vitality=250, luck=200, cooldown=175, side="Giants")


class Odin(Gods):
    """
    Odin is the All-father and Raven God. His sons are Thor and Baldur.
    He seeks knowledge, power, and control to somehow change his fate during Ragnarok.
    He is notorious for double crossing creatures of all manor to further his knowledge of the future.
    He believes the Giants foresight and wisdom is the key to changing his fate.
    """
    def __init__(self):
        super().__init__(strength=300, defence=290, runic=350, vitality=198, luck=78, cooldown=150, side="Aesir")


class Thor(Gods):
    """
    Thor is the God of Thunder and the son of Odin.
    His brother is Baldur. He is the father to Magni and Modi.
    Thor is a notorious killer of Giants, usually with his signature hammer Mjollnir.
    Thor’s sworn enemy is the World Serpent, whom he is destined to fight during Ragnarok.
    """
    def __init__(self):
        super().__init__(strength=325, defence=345, runic=100, vitality=150, luck=97, cooldown=120, side="Aesir")


class Heimdall(Gods):
    """
    Heimdall is the Norse God of Foresight, Surveillance, Order and Foreknowledge.
    He is a son of Odin and Blóðughadda, younger half-brother of Thor and Týr, older half-brother of Baldur, and uncle of Magni, Modi, Forseti and Thrúd.
    """
    def __init__(self):
        super().__init__(strength=230, defence=270, runic=245, vitality=197, luck=47, cooldown=30, side="Aesir")


class Freya(Gods):
    """
    Freya, also known in Old Norse as Frigg, is the Vanir Goddess of Love, Beauty, War, Death and Fertility.
    She is the daughter of Njörd and Nerthus, the sister of Freyr, and the ex-wife of Odin with whom she procreated Baldur, making her the grandmother of Forseti as well.
    She was also the former leader of the Vanir during the Aesir-Vanir War and Queen of the Valkyries before the fallout of her marriage with the All-Father.
    """
    def __init__(self):
        super().__init__(strength=275, defence=297, runic=400, vitality=154, luck=64, cooldown=60, side="Giants")


class Freyr(Gods):
    """
    Freyr, also known as Yngvi, is the Vanir God of Rain and Fertility. He is the son of Njörd and Nerthus, the brother of Freya, and the uncle of Baldur.
    """
    def __init__(self):
        super().__init__(strength=295, defence=243, runic=365, vitality=179, cooldown=42, side="Giants")


class Tyr(Gods):
    """
    Týr is the Aesir God of War, Law, Justice, and Honor.
    He is a son of Odin and Fjörgyn, younger brother of Thor, older half-brother of Heimdall and Baldur, and uncle of Magni, Modi, Forseti and Thrúd.
    """
    def __init__(self):
        super().__init__(strength=321, defence=331, runic=256, vitality=173, cooldown=21, side="Giants")

class Cards(object):
    def __init__(self, players: list):
        self.players = players
        self.Cards = [Kratos(), Atreus(), Odin(), Thor(), Heimdall(), Freya(), Freyr(), Tyr()]
        self.Temp_Deck = []
        self.Player_Decs = {}
        self.PLAYER_CARDS_LMT = 8 // len(players) #22 // len(players)
        self.MAX_CARDS_LMT = self.PLAYER_CARDS_LMT * len(players)
        self.generate_deck()

    def generate_deck(self):
        shuffle(self.Cards)
        self.Cards[:self.MAX_CARDS_LMT]
        copy = self.Cards[:]
        for p in self.players:
            s = sample(copy, self.PLAYER_CARDS_LMT)
            self.Player_Decs[p] = s
            for i in s:
                copy.remove(i)

    def cards_for(self, player: int) -> Union[dict, None]:
        return self.Player_Decs.get(player)
    

