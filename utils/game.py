from .cards import Cards
from typing import Union
class Game(object):
    def __init__(self):
        self.players: list = []
        self.cardsobj: Cards = Cards(self.players)
        self.started: bool = False
        
    def add_player(self, name: str) -> bool:
        if name not in self.players:
            self.players.append(name) 
            return True
        return False

    def remove_player(self, name: str) -> bool:
        if name in self.players:
            self.players.remove(name)
            return True
        return False
    
    def start(self):
        self.cardsobj.generate_deck()
        self.current_attribute = self.cardsobj.choose_attribute()
        self.started = True
        self.current_player = self.players[0]
        self.player_before = self.current_player
        self.card_index = 0
        self.round = 1
        self.all_players = self.players
    
    def next_player(self):
        self.check()
        try:
            index = self.players.index(self.current_player)
        except Exception:
            return False
        try:
            self.current_player = self.players[index+1]
            self.card_index = 0
            self.player_before = self.players[index]
        except Exception as e:
            return False
    
    def check(self):
        for player in self.cardsobj.Player_Decs:
            if self.cardsobj.Player_Decs[player] == [] and player in self.players:
                self.players.remove(player)
    
    def check_game_winner(self) -> Union[bool, list[str, int]]:
        self.check()
        if len(self.players) == 1:
            self.cardsobj.temp_to_player(self.players[0])
            return [self.players[0], self.cardsobj.cards_len(self.players[0])] 
        else:
            return False 

    def next_round(self):
        self.check()
        self.current_player = self.players[0]
        self.card_index = 0
        self.current_attribute = self.cardsobj.choose_attribute()
        self.round += 1
        self.round_before = self.round - 1
    
    def get_round(self) -> int:
        return self.round
    
    def check_round_winner(self) -> list[str, int]:
        self.check()
        winner = self.cardsobj.compare()
        self.cardsobj.temp_to_player(winner)
        return [winner, self.cardsobj.cards_len(winner)]
