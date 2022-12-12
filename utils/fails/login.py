# import pygame

# pygame.init()
# pygame.font.init()

# WIDTH, HEIGHT = 900, 500
# WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# pygame.display.set_caption("God Of War: Top Trunks")

# FONT = pygame.font.SysFont("comiscans", 40)
# FPS = 60
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# TURQUOISE = (48, 213, 200)
# BLURPLE = (88, 101, 242)
# GREEN = (127,255,0)
# LIGHTBLUE = (135,206,250)
# INPUTBOXES = []


# WIN.fill(TURQUOISE)

# logged_in = False
# register_button_clicked = False
# input_data = {}

# run = True
# clock = pygame.time.Clock()

# class InputBox:
#     def __init__(self, x, y, w, h, text=''):
#         self.COLOR_INACTIVE = pygame.Color('lightskyblue3')
#         self.COLOR_ACTIVE = pygame.Color('dodgerblue2')
#         self.FONT = pygame.font.Font(None, 32)
#         self.rect = pygame.Rect(x, y, w, h)
#         self.color = self.COLOR_INACTIVE
#         self.text = text
#         self.txt_surface = self.FONT.render(text, True, self.color)
#         self.active = False

#     def handle_event(self, event):
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             # If the user clicked on the input_box rect.
#             if self.rect.collidepoint(event.pos):
#                 # Toggle the active variable.
#                 self.active = not self.active
#             else:
#                 self.active = False
#             # Change the current color of the input box.
#             self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
#         if event.type == pygame.KEYDOWN:
#             if self.active:
#                 if event.key == pygame.K_RETURN:
#                     self.text = ''
#                 elif event.key == pygame.K_BACKSPACE:
#                     self.text = self.text[:-1]
#                 else:
#                     self.text += event.unicode
#                 # Re-render the text.
#                 self.txt_surface = self.FONT.render(self.text, True, self.color)

#     def update(self):
#         # Resize the box if the text is too long.
#         width = max(200, self.txt_surface.get_width()+10)
#         self.rect.w = width

#     def draw(self, screen):
#         # Blit the text.
#         pygame.draw.rect(screen, TURQUOISE, pygame.Rect(self.rect.x, self.rect.y, self.rect.w, self.rect.h), 2)
#         pygame.display.update()
#         screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
#         # Blit the rect.
#         pygame.draw.rect(screen, self.color, self.rect, 2)

# def create_input_box(x, y, width, height):
#     input_box = pygame.Rect(x, y, width, height)
#     pygame.draw.rect(WIN, WHITE, input_box)
#     return input_box

# # Create a text surface
# def create_text_surface(text, color, rect):
#     text_surface = FONT.render(text, True, color)
#     text_rect = text_surface.get_rect()
#     text_rect.center = rect.center
#     WIN.blit(text_surface, text_rect)

# # Create a button
# def create_button(x, y, width, height, text, color, action=None):
#     button = pygame.Rect(x, y, width, height)
#     pygame.draw.rect(WIN, color, button)
#     create_text_surface(text, BLACK, button)
#     if action is not None:
#         if button.collidepoint(pygame.mouse.get_pos()):
#             if pygame.mouse.get_pressed()[0]:
#                 action()

# def register():
#     global register_button_clicked, INPUTBOXES
#     register_button_clicked = True
#     WIN.fill(TURQUOISE)
#     username_input = InputBox(275, 100, 100, 100, text = 'Username')
#     password_input = InputBox(275, 200, 100, 100, text = 'Password')
#     INPUTBOXES.extend([username_input, password_input])
    



# def first_menu():
#     #gonna ask them to click login or register
#     global register_button_clicked
#     if not register_button_clicked:
#         create_button(100, 100, 150, 100, "Register", BLURPLE, action = register)
        

# while run:
#     clock.tick(FPS)
#     for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#                 pygame.quit()
#             for box in INPUTBOXES:
#                 box.handle_event(event)
        
#     for box in INPUTBOXES:
#         box.update()
#     if len(INPUTBOXES) > 0:
#         WIN.fill(TURQUOISE)
#     for box in INPUTBOXES:
#             box.draw(WIN)
            

#     first_menu()        
#     pygame.display.update()
    

            

            
    
