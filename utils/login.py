import pygame
from user import UserUtils
import string

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


WIN.fill(TURQUOISE)

logged_in = False
register_button_clicked = False
input_data = {}

run = True
clock = pygame.time.Clock()
userutils = UserUtils()
IS_PRINTABLE = ''.join([string.ascii_letters, string.punctuation, string.digits])
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.COLOR_INACTIVE = pygame.Color('lightskyblue3')
        self.COLOR_ACTIVE = pygame.Color('dodgerblue2')
        self.FONT = pygame.font.Font(None, 32)
        self.rect = pygame.Rect(x, y, w, h)
        self.color = self.COLOR_INACTIVE
        self.text = text
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False

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
def create_text_surface(text, color, rect):
    text_surface = FONT.render(text, True, color)
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

def register():
    global register_button_clicked, INPUTBOXES
    register_button_clicked = True
    WIN.fill(TURQUOISE)
    username_input = InputBox(75, 100, 100, 100, text='Username')
    password_input = InputBox(75, 200, 100, 100, text='Password')
    INPUTBOXES.extend([username_input, password_input])


def first_menu():
    #gonna ask them to click login or register
    global register_button_clicked
    if not register_button_clicked:
        create_button(100, 100, 150, 100, "Register", BLURPLE, action=register)

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
            PERSISTENT_TEXT.append([txt, BLACK, create_input_box(250, 50, len(txt)*10, 100)])
            PERSISTENT_BUTTONS.extend([[75, 100, 175, 100, "Create Lobby", BLURPLE], [75, 100, 175, 100, "Join Lobby", BLURPLE]])

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
        PERSISTENT_TEXT = NEW
        
while run:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    txt = [box.text for box in INPUTBOXES]
                    FLAG = False
                    try:
                        if userutils.lookup(txt[0].strip()):
                            INPUTBOXES[0].text = "Username_Taken"
                            FLAG = True

                        if txt[0].strip().lower() in ['', 'invalid', 'username', 'username_taken']:
                            INPUTBOXES[0].text = "invalid"
                            #INPUTBOXES[0].draw(WIN)
                            FLAG = True
                        if txt[1].strip().lower() in ['', 'invalid', 'password']:
                            INPUTBOXES[1].text = "invalid"
                            #INPUTBOXES[1].draw(WIN)
                            FLAG = True

                        if not FLAG:
                            PERSISTENT_TEXT = []
                            PERSISTENT_BUTTONS = []
                            PERSISTENT_BUTTONS.append([75, 300, 150, 150, "Sign Up", BLURPLE, register_action, txt[0], txt[1]])
                    except IndexError:
                        pass

            for box in INPUTBOXES:
                box.handle_event(event)

    for box in INPUTBOXES:
        box.update()

    if len(INPUTBOXES) > 0 or len(PERSISTENT_BUTTONS) > 0 or len(PERSISTENT_TEXT):
        WIN.fill(TURQUOISE)

    for box in INPUTBOXES:
            box.draw(WIN)

    for button in PERSISTENT_BUTTONS:
        create_button(*button)

    for text in PERSISTENT_TEXT:
        create_text_surface(*text)


    first_menu()
    pygame.display.update()
    clock.tick(FPS)
    

            

            
    
