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


# class Dwarfs(Base):
#     def __init__(self, **kwargs):
#         super().__init__(species="Dwarfs", **kwargs)


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
        super().__init__(strength=321, defence=331, runic=256, vitality=173, luck=82, cooldown=21, side="Giants")

class Jormungandr(Giants):
    """
    Jörmungandr, also known as the World Serpent,
    is a mythical Jötunn serpent destined to fight Thor come Ragnarök.
    """
    def __init__(self):
        super().__init__(strength=786, defence=420, runic=76, vitality=123, luck=73, cooldown = 0, side="Giants")

class Angrboda(Giants):
    """
    Angrboða or Angrboda is a female jötunn,
    She is the mate of Loki and the mother of monsters.
    """
    def __init__(self):
        super().__init__(strength=64, defence=71, runic=110, vitality=157, luck=92, cooldown=32, side="Giants")

class Eir(Valkyries):
    """
    The Healer. Strange, for a Valkyrie. Very quiet. Very calm. 
    Where her sisters were violent rapids, Eir was a gentle stream.
    She healed the wounds of both mortals and gods.
    """
    def __init__(self):
        super().__init__(strength=269, defence=296, runic=101, vitality=111, luck=77, cooldown=32, side="Aesir")

class Gunnr(Valkyries):
    """
    Mistress of War. After any conflict, big or small, 
    she would be first on the scene, sussing out the worthy spirits for a free trip to Valhalla.
    Her judgement of the fallen was unparalleled, and an invaluable resource to Odin.
    She was one of his favorites
    """
    def __init__(self):
        super().__init__(strength=279, defence=297, runic=107, vitality=121, luck=76, cooldown=12, side="Aesir")

class Olrun(Valkyries):
    """
    Once the daughter of a powerful chieftain, she fell defending him during a Reaver attack.
    Olrun was escorted to Valhalla, where she chose to pursuit of knowledge above all else.
    Odin appointed her as the Valkyrie's resident historian.
    """
    def __init__(self):
        super().__init__(strength=289, defence=298, runic=111, vitality=127, luck=101, cooldown=33, side="Aesir")

class Rota(Valkyries):
    """
    One of the Choosers of the Slain.
    Róta was the first to go mad after being imprisoned in a physical form.
    Sigrún stashed her in Helheim to keep her away from harming herself or others.
    Mostly others.
    """
    def __init__(self):
        super().__init__(strength=299, defence=291, runic=213, vitality=113, luck=109, cooldown=29, side="Aesir")

class Hildr(Valkyries):
    """
    Mistress of Battle. She and Odin got on quite well, actually.
    Her and the other Valkyries... not so much.
    She lived for conflict. Some say she WAS conflict, personified.
    I wonder what will become of her, now that she's free.
    """
    def __init__(self):
        super().__init__(strength=267, defence=299, runic=164, vitality=142, luck=116, cooldown=27, side="Aesir")

class Gondul(Valkyries):
    """
    The sight of Gondul always took my breath away.
    Gondul had a sharp wit, and struck a figure so stunning, it literally drove men insane.
    Odin forbid her from setting foot in Midgard after a time, 
        as insanity is not a welcome trait in Valhalla.
    """
    def __init__(self):
        super().__init__(strength=215, defence=301, runic=145, vitality=133, luck = 124, cooldown=24, side="Aesir")

class Sigrun(Valkyries):
    """
    Queen of the Valkyries, although she does not appear to refer to herself as such.
    When Freya, the original Queen Valkyrie, lost her wings to Odin, 
        Sigrún grudgingly took the position in her stead.
    """
    def __init__(self):
        super().__init__(strength=356, defence=345, runic=173, vitality=178, luck=247, cooldown=7, side="Giants")
        
class Hrist(Valkyries):
    """
    Their coordination in battle is unmatched.
    It is a pity their fealty to Odin is by choice, and not a corruption abated by their death.
    """
    def __init__(self):
        super().__init__(strength=257, defence=312, runic=133, vitality=164, luck=217, cooldown=39, side="Aesir")

class Mist(Valkyries):
    """
    Their coordination in battle is unmatched.
    It is a pity their fealty to Odin is by choice, and not a corruption abated by their death.
    """
    def __init__(self):
        super().__init__(strength=298, defence=309, runic=123, vitality=154, luck=199, cooldown=41, side="Aesir")


class Svartaljofurr(Elfs):
    """
    King of the Dark Elves, Svartáljǫfurr leads the war against the Light Elves for the Light of Alfheim,
    """
    def __init__(self):
        super().__init__(strength=317, defence=311, runic=217, vitality=126, luck=204, cooldown=36, side = "Giants")



class Cards(object):
    def __init__(self, players: list):
        self.players = players
        self.Cards = [Kratos(), Atreus(), Odin(), Thor(), Heimdall(), Freya(), Freyr(), Tyr(), Jormungandr(), Angrboda(), Eir(), Gunnr(), Olrun(), Rota(), Hildr(), Gondul(), Sigrun(), Hrist(), Mist()]
        print(len(self.Cards))
        self.Temp_Deck = {}
        self.Player_Decs = {}
        self.choices = {1: "strength", 2: "defence", 3:"runic", 4:"vitality", 5:"luck", 6:"cooldown"}
        self.current_choice = None

    def generate_deck(self):
        self.PLAYER_CARDS_LMT = len(self.Cards) // len(self.players) #22 // len(players)
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
            if self.current_choice == 6:
                if card.__getattribute__(attr) < best.__getattribute__(attr):
                    best = card
            else:
                if card.__getattribute__(attr) > best.__getattribute__(attr):
                    best = card

        for player in self.Temp_Deck:
            card = self.Temp_Deck[player]
            if card == best:
                return player  
