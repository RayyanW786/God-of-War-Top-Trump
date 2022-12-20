import pygame
from utils.user import UserUtils
import string
from utils.game import Game
import time
from utils.cards import Base
import datetime

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("God Of War: Top Trunks")

FONT = pygame.font.SysFont("comiscans", 28)
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TURQUOISE = (48, 213, 200)
BLURPLE = (88, 101, 242)
GREEN = (127,255,0)
LIGHTBLUE = (135,206,250)
INPUTBOXES = []
PERSISTENT_BUTTONS = []
PERSISTENT_TEXT = []
PERSISTENT_FUNCTIONS = []
WINNER_TEXT = [] #txt, dt
ROUND_WINNER_TEXT = []


WIN.fill(TURQUOISE)

logged_in = False
first_menu_button_clicked = False
input_data = {}

run = True
clock = pygame.time.Clock()
userutils = UserUtils()
Gameobj = Game()
IS_PRINTABLE = ''.join([string.ascii_letters, string.punctuation, string.digits])

class InputBox:
    def __init__(self, x, y, w, h, text='', type='register'):
        self.COLOR_INACTIVE = pygame.Color('lightskyblue3')
        self.COLOR_ACTIVE = pygame.Color('dodgerblue2')
        self.FONT = pygame.font.Font(None, 32)
        self.rect = pygame.Rect(x, y, w, h)
        self.color = self.COLOR_INACTIVE
        self.text = text
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False
        self.type = type

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if event.unicode in IS_PRINTABLE:
                        self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, True, self.color)

    def update_text(self):
        self.txt_surface = self.FONT.render(self.text, True, self.color)
    
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        #pygame.draw.rect(screen, TURQUOISE, pygame.Rect(self.rect.x, self.rect.y, self.rect.w, self.rect.h), 2)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

def create_input_box(x, y, width, height):
    input_box = pygame.Rect(x, y, width, height)
    pygame.draw.rect(WIN, TURQUOISE, input_box)
    return input_box


# Create a text surface
def create_text_surface(text, color, rect, special=False):
    if special==False:
        text_surface = FONT.render(text, True, color)
    else:
        special = pygame.font.Font(None, 20) #pygame.font.SysFont("comiscans", 20, italic=True)
        text_surface = special.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = rect.center
    WIN.blit(text_surface, text_rect)

# Create a button
def create_button(x, y, width, height, text, color, action=None, *args):
    button = pygame.Rect(x, y, width, height)
    pygame.draw.rect(WIN, color, button)
    create_text_surface(text, BLACK, button)
    if action is not None:
        if button.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                action(*args)

def previous_card():
    time.sleep(.2)
    Gameobj.card_index -= 1

def next_card():
    time.sleep(.2)
    Gameobj.card_index += 1

def select_card():
    time.sleep(.2)
    global INPUTBOXES, PERSISTENT_BUTTONS, PERSISTENT_TEXT, PERSISTENT_FUNCTIONS, WINNER_TEXT, ROUND_WINNER_TEXT
    Gameobj.cardsobj.add_to_temp(Gameobj.current_player, Gameobj.card_index)
    res = Gameobj.next_player()
    if res == False:
        Game_winner_res = Gameobj.check_game_winner()
        if type(Game_winner_res) == list:
            PERSISTENT_FUNCTIONS = []
            PERSISTENT_TEXT = []
            PERSISTENT_BUTTONS = []
            dt = datetime.datetime.now() + datetime.timedelta(seconds = 6)
            WINNER_TEXT.extend([[f'Player {Game_winner_res[0]} Won the Game with {Game_winner_res[1]} Cards', BLACK, create_input_box(250, 175, 200, 200)], dt.timestamp()])
            
            
        else:   
            Round_Winner_Res = Gameobj.check_round_winner()
            PERSISTENT_TEXT = []
            PERSISTENT_BUTTONS = []
            dt = datetime.datetime.now() + datetime.timedelta(seconds = 2)
            ROUND_WINNER_TEXT.extend([[f'Player {Round_Winner_Res[0]} Won the round and now has {Round_Winner_Res[1]} Cards', BLACK, create_input_box(250, 175, 200, 200)], dt.timestamp()])
            Gameobj.next_round()


def Launcher():
    global INPUTBOXES, PERSISTENT_BUTTONS, PERSISTENT_TEXT, PERSISTENT_FUNCTIONS
    PERSISTENT_TEXT = []
    INPUTBOXES = []
    PERSISTENT_BUTTONS = []
    current_player = Gameobj.current_player
    PERSISTENT_TEXT.append([f"Current Player: {current_player}", BLACK, create_input_box(600, 10, 100, 25)])
    PERSISTENT_TEXT.append([f"Current Round: {Gameobj.round}", BLACK, create_input_box(600, 30, 50, 25)])
    PERSISTENT_TEXT.append([f"Player: Amt of Cards", BLACK, create_input_box(600, 30, 88, 100)])
    height_offset = -25
    for player in Gameobj.all_players:
        height_offset += 50
        PERSISTENT_TEXT.append([f"{player}: {Gameobj.cardsobj.cards_len(player)}", BLACK, create_input_box(600, 50, 75, 100+height_offset)])
    if Gameobj.card_index > 0:
        PERSISTENT_BUTTONS.append([300, 200, 125, 75, "Previous Card", BLURPLE, previous_card])
    if Gameobj.card_index+1 < len(Gameobj.cardsobj.Player_Decs[Gameobj.current_player]):
        PERSISTENT_BUTTONS.append([300, 300, 125, 75, "Next Card", BLURPLE, next_card])
    PERSISTENT_BUTTONS.append([300, 400, 125, 75, "Select Card", BLURPLE, select_card]) 
    display_card = Gameobj.cardsobj.cards_for(Gameobj.current_player)[Gameobj.card_index]
    PERSISTENT_TEXT.append([f"Attribute Being Compared: {Gameobj.current_attribute.capitalize()}", BLACK, create_input_box(200, 25, 25, 25)])
    cardattrs = [a for a in display_card.__dir__() if not a.startswith('__')]
    y_offset = -25
    PERSISTENT_TEXT.append([f"Character: {display_card.__class__.__name__}", BLACK, create_input_box(200, 35, 50, 50)])
    for ln in display_card.__class__.__doc__.split("\n"):
        y_offset += 25
        PERSISTENT_TEXT.append([ln, BLACK, create_input_box(250, 50+y_offset, 50, 50), True])
    y_offset = -25
    for attr in cardattrs:
        y_offset += 25
        PERSISTENT_TEXT.append([f"{attr}: {display_card.__getattribute__(attr)}", BLACK, create_input_box(155, 250+y_offset, 50, 50)])


def start_game():
    global INPUTBOXES, PERSISTENT_BUTTONS, PERSISTENT_TEXT, PERSISTENT_FUNCTIONS
    if len(Gameobj.players) >= 2 and len(Gameobj.players) <= 8: 
        Gameobj.start()
        PERSISTENT_FUNCTIONS = [Launcher]


    else:
        PERSISTENT_TEXT = PERSISTENT_TEXT[:3]
        
        if len(Gameobj.players) < 2: 
            PERSISTENT_TEXT.append(["ERROR - At least 2 players are required to start the game!", BLACK, create_input_box(255, 350, 100, 100)])
        if len(Gameobj.players) > 8:
            PERSISTENT_TEXT.append(["ERROR - You can only have a maximum of 8 players!", BLACK, create_input_box(225, 350, 100, 100)])
            

def create_lobby():
    global INPUTBOXES, PERSISTENT_BUTTONS, PERSISTENT_TEXT
    PERSISTENT_BUTTONS = []
    INPUTBOXES = []
    PERSISTENT_TEXT = []
    add_input = InputBox(125, 125, 50, 50, type = "add_player")
    remove_input = InputBox(155, 200, 50, 50, type = "remove_player")
    PERSISTENT_TEXT.append(['Add Player: ', BLACK, create_input_box(5, 100, len('Add Player: ')*10, 100)])
    PERSISTENT_TEXT.append(['Remove Player: ', BLACK, create_input_box(5, 175, len('Remove Player: ')*10, 100)])
    PERSISTENT_TEXT.append(['Players: ', BLACK, create_input_box(550, 50, 100, 5)])      
    INPUTBOXES.extend([add_input, remove_input])
    PERSISTENT_BUTTONS.append([50, 275, 175, 100, "start game", BLURPLE, start_game])


def register():
    global INPUTBOXES, first_menu_button_clicked
    first_menu_button_clicked = True
    username_input = InputBox(110, 125, 50, 50)
    password_input = InputBox(110, 225, 50, 50)
    PERSISTENT_TEXT.append(['username: ', BLACK, create_input_box(5, 100, len('username: ')*10, 100)])
    PERSISTENT_TEXT.append(['password: ', BLACK, create_input_box(5, 200, len('password: ')*10, 100)])
    INPUTBOXES.extend([username_input, password_input])

def login():
    global first_menu_button_clicked, INPUTBOXES, PERSISTENT_TEXT
    first_menu_button_clicked = True
    username_input = InputBox(110, 125, 50, 50, type = "login")
    password_input = InputBox(110, 225, 50, 50, type = "login")
    PERSISTENT_TEXT.append(['username: ', BLACK, create_input_box(5, 100, len('username: ')*10, 100)])
    PERSISTENT_TEXT.append(['password: ', BLACK, create_input_box(5, 200, len('password: ')*10, 100)])      
    INPUTBOXES.extend([username_input, password_input])


def first_menu():
    #gonna ask them to click login or register
    global first_menu_button_clicked
    if not first_menu_button_clicked:
        create_button(100, 100, 150, 100, "Register", BLURPLE, action=register)
        create_button(100, 200, 150, 100, "Log in", BLURPLE, action=login)

def register_action(username: str, password: str):
    global PERSISTENT_BUTTONS, PERSISTENT_TEXT, INPUTBOXES
    res = userutils.register_checks(username, password)
    if type(res) == bool:
        if res == True:
            res = userutils.register(username, password)
            PERSISTENT_TEXT = []
            PERSISTENT_BUTTONS = []
            INPUTBOXES = []
            txt = "Logged in successfully"
            PERSISTENT_TEXT.append([txt, BLACK, create_input_box(280, 50, len(txt)*10, 100)])
            PERSISTENT_BUTTONS.extend([[175, 200, 175, 100, "Create Lobby", BLURPLE], [425, 200, 175, 100, "Previous Winners", BLURPLE]])

    else:
        title = res[0]
        res = res[1:]
        title_box = create_input_box(275, 50, len(title)*10, 100)
        NEW = []
        NEW.append([title, BLACK, title_box])
        offset_y = 0
        for feedback in res:
            offset_y += 25
            feedback_box = create_input_box(300, 50+offset_y, len(feedback)*10, 100)
            NEW.append([feedback, BLACK, feedback_box])
        PERSISTENT_TEXT = PERSISTENT_TEXT[:2] + NEW

def login_action():
    global PERSISTENT_BUTTONS, PERSISTENT_TEXT, INPUTBOXES
    PERSISTENT_TEXT = []
    PERSISTENT_BUTTONS = []
    INPUTBOXES = []
    txt = "Logged in successfully"
    PERSISTENT_TEXT.append([txt, BLACK, create_input_box(280, 50, len(txt)*10, 100)])
    PERSISTENT_BUTTONS.extend([[175, 200, 175, 100, "Create Lobby", BLURPLE, create_lobby], [425, 200, 175, 100, "Previous Winners", BLURPLE]])

def welcome_back_action():
    global PERSISTENT_BUTTONS, PERSISTENT_TEXT, INPUTBOXES
    PERSISTENT_TEXT = []
    PERSISTENT_BUTTONS = []
    INPUTBOXES = []
    txt = "Welcome Back, What would you like to do?"
    PERSISTENT_TEXT.append([txt, BLACK, create_input_box(280, 50, len(txt)*10, 100)])
    PERSISTENT_BUTTONS.extend([[175, 200, 175, 100, "Create Lobby", BLURPLE, create_lobby], [425, 200, 175, 100, "Previous Winners", BLURPLE]])
    
        
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                txt_register = [box.text for box in INPUTBOXES if box.type == "register"]
                txt_login = [box.text for box in INPUTBOXES if box.type == "login"]
                txt_add_player = [box.text for box in INPUTBOXES if box.type == "add_player"]
                txt_remove_player = [box.text for box in INPUTBOXES if box.type == "remove_player"]
                if len(txt_add_player) == 1:
                    if txt_add_player[0] != "":
                        res = Gameobj.add_player(txt_add_player[0])
                        if res == False:
                            INPUTBOXES[0].text = "Player_Already_Exists!"
                            INPUTBOXES[0].update_text()
                        else:
                            INPUTBOXES[0].text = ""
                            INPUTBOXES[0].update_text()

                if len(txt_remove_player) == 1:
                    if txt_remove_player[0] != "":
                        res = Gameobj.remove_player(txt_remove_player[0])
                        if res == False:
                            INPUTBOXES[1].text = "Player_Not_Found!"
                            INPUTBOXES[1].update_text()
                        else:
                            INPUTBOXES[1].text = ""
                            INPUTBOXES[1].update_text()
                        
                LOG_FLAG = False
                try:
                    if not userutils.login(txt_login[0], txt_login[1]):
                        INPUTBOXES[0].text = "INVALID"
                        INPUTBOXES[1].text = "INVALID"
                        INPUTBOXES[0].update_text()
                        INPUTBOXES[1].update_text()
                        LOG_FLAG = True
                    
                    if not LOG_FLAG:
                        PERSISTENT_BUTTONS = []
                        PERSISTENT_BUTTONS.append([75, 300, 150, 150, "Log In", BLURPLE, login_action])

                except IndexError:
                    pass

                REG_FLAG = False
                try:
                    if userutils.lookup(txt_register[0].strip()):
                        INPUTBOXES[0].text = "Username_Taken"
                        INPUTBOXES[0].update_text()
                        REG_FLAG = True

                    if txt_register[0].strip().lower() in ['', 'invalid', 'username', 'username_taken', 'user_not_found']:
                        INPUTBOXES[0].text = "invalid"
                        INPUTBOXES[0].update_text()
                        #INPUTBOXES[0].draw(WIN)
                        REG_FLAG = True
                    if txt_register[1].strip().lower() in ['', 'invalid', 'password']:
                        INPUTBOXES[1].text = "invalid"
                        INPUTBOXES[1].update_text()
                        #INPUTBOXES[1].draw(WIN)
                        REG_FLAG = True

                    if not REG_FLAG:
                        PERSISTENT_BUTTONS = []
                        PERSISTENT_BUTTONS.append([75, 300, 150, 150, "Sign Up", BLURPLE, register_action, txt_register[0], txt_register[1]])
                except IndexError:
                    pass

        for box in INPUTBOXES:
            box.handle_event(event)

    for box in INPUTBOXES:
        box.update()

    if len(INPUTBOXES) > 0 or len(PERSISTENT_BUTTONS) > 0 or len(PERSISTENT_TEXT) or len(PERSISTENT_FUNCTIONS) > 0 or len(WINNER_TEXT) > 0 or len(ROUND_WINNER_TEXT) > 0:
        WIN.fill(TURQUOISE)

    for box in INPUTBOXES:
        box.draw(WIN)
    
    if Gameobj.started == False:
        y_offset = 0
        for player in Gameobj.players:
            w = -20
            y_offset+=25
            for word in player:
                w += 12
            create_text_surface(player, BLACK, create_input_box(600, 50+y_offset, w, 5))          

    for button in PERSISTENT_BUTTONS:
        create_button(*button)
    
    if len(WINNER_TEXT) >=1:
        dt = datetime.datetime.now().timestamp()
        if WINNER_TEXT[1] > dt:
            create_text_surface(*WINNER_TEXT[0])
        else:
            WINNER_TEXT = []
            Gameobj.reset()
            welcome_back_action()
        
    if len(ROUND_WINNER_TEXT) >=1:
        dt = datetime.datetime.now().timestamp()
        if ROUND_WINNER_TEXT[1] > dt:
            create_text_surface(*ROUND_WINNER_TEXT[0])
        else:
            ROUND_WINNER_TEXT = []

    if len(ROUND_WINNER_TEXT) == 0:
        for func in PERSISTENT_FUNCTIONS:
            func()

    for text in PERSISTENT_TEXT:
        create_text_surface(*text)

    if first_menu_button_clicked == False:
        first_menu()

    pygame.display.update()
    clock.tick(FPS)
    