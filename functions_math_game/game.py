import pygame
from curses import KEY_ENTER
from icon import Icon, Button, Player, Graph, Background, Background2, Obstacle, ObstacleType, GreenArea

"""
    Zmienne:
    w_size              -> window_size
    color               -> background_color
    running             -> game_running
    graphics_running    -> graphics_menu_running
    input_box           -> formula_box
    game_bg             -> background_image
    text                -> formula
    inscription         -> formula_box_label

    Funkcje:
    graphics_changes()  -> graphics_menu()
    game_start()        -> game_start()
    writing_mode()      -> editing_graph_formula()
    nowa Icon::change_cords()

    Propozycja:
    (OK) zmiana background_color z list na tuple
    zmiana window_size z tuple na dict
    Icon::conditions()  -> Icon::is_mouse_over()

    Pomysł:
    (OK) Kasowanie z formula_box przy trzymaniu backspace'a
    Połączenie klasy Background oraz klasy Background2
    Dodanie nowej funkcji obsługującej eventy z pygame
    Zmiana buttonów od rozdzielczości na dropdown (lista rozwiajana)
"""

class Game:
    # window
    window_size: tuple
    screen: pygame.Surface

    # colors
    background_color: tuple

    # flags
    game_running: bool

    # game specific
    player: Player
    player_velocity: float
    backround_image: Background2
    list_of_obstacles: list
    green_area: GreenArea
    lvl: int
    

    def __init__(self, window_size=(900,600)):
        self.window_size = window_size
        self.screen = pygame.display.set_mode(self.window_size)
        self.running_running = False
        self.background_color = (0, 0, 0)
        self.list_of_obstacles = []
        self.lvl = 0

        self.init_icon()

        pygame.init() # inicjowanie okna gry
    
    def init_icon(self):
        icon = pygame.image.load("assets/player.png")
        pygame.display.set_icon(icon)

    def main_menu(self):
        start_button = Icon(
            "assets/play.png",
            (self.window_size[0]/2, self.window_size[1]/2 - 150),
            (200, 100)
        )
        graphics_button = Icon(
            "assets/graphics.png",
            (self.window_size[0]/2, self.window_size[1]/2 + 50),
            (200, 100)
        )
        start_bg = Background(
            "assets/background.png",
            (self.window_size[0]/2, self.window_size[1]/2),
            (1800, 1200)
        )
        highscore_button = Icon(
            "assets/big_highscore.png",
            (self.window_size[0] - 330, self.window_size[1] - 50),
            (350, 100)
        )
        highscore_font = pygame.font.Font(None, 100)
        try:
            with open("highscore.txt") as file:
                for line in file:
                    highscore_number = int(line)
                    highscore_img = highscore_font.render(str(highscore_number), True, (0, 0, 0))
            file.close()
        except FileNotFoundError:
            file = open("highscore.txt","w")
            file.write('0')
            file.close()
            highscore_img = highscore_font.render(str(0), True, (0, 0, 0))
        

        main_menu_running = True
        while main_menu_running:
            # self.screen.fill(self.background_color)
            start_bg.rescale_and_show(self.window_size, self.screen)
            start_button.show(self.screen)
            graphics_button.show(self.screen)
            highscore_button.show(self.screen)
            self.screen.blit(highscore_img,(self.window_size[0] - 150, self.window_size[1] - 80))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == ord('q'):
                        self.screen.fill(self.background_color)
                        pygame.display.flip()
                        exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.conditions():
                        self.background_color = (0, 0, 0)
                        self.run_game()
                        main_menu_running = False

                    if graphics_button.conditions():
                        self.graphics_menu()
                        start_button.change_cords(
                            (self.window_size[0]/2, self.window_size[1]/2 - 100)
                        )
                        graphics_button.change_cords(
                            (self.window_size[0]/2, self.window_size[1]/2 + 100),
                        )
                        highscore_button.change_cords(
                            (self.window_size[0] - 330, self.window_size[1] - 50),
                        )

            pygame.display.flip() #odświeżanie klatek

    def graphics_menu(self):
        # self.screen.fill(self.background_color)

        start_bg = Background(
            "assets/background.png",
            (self.window_size[0]/2, self.window_size[1]/2),
            (1800, 1200)
        )
        button_fullscreen_window = Button(
            "assets/fsw.png",
            (self.window_size[0]/2 - 200, self.window_size[1]/2 - 200),
            (200, 100),
            (0, 0),
            "fullscreen window"
        )
        button_fullscreen = Button(
            "assets/fs.png",
            (self.window_size[0]/2 + 200, self.window_size[1]/2 - 200),
            (200,100),
            (0,0),
            "fullscreen"
        )
        button_1800x1200 = Button(
            "assets/1800x1200.png",
            (self.window_size[0]/2 - 200, self.window_size[1]/2),
            (200,100),
            (1800,1200),
            "window"
        )
        button_1500x1000 = Button(
            "assets/1500x1000.png",
            (self.window_size[0]/2 + 200, self.window_size[1]/2),
            (200,100),
            (1500,1000),
            "window"
        )
        button_1200x800 = Button(
            "assets/1200x800.png",
            (self.window_size[0]/2 - 200, self.window_size[1]/2 + 200),
            (200,100),
            (1200,800),
            "window"
        )
        button_900x600 = Button(
            "assets/900x600.png",
            (self.window_size[0]/2 + 200, self.window_size[1]/2 + 200),
            (200,100),
            (900,600),
            "window"
        )
        
        button_list = [
            button_fullscreen,
            button_fullscreen_window,
            button_1800x1200,
            button_1500x1000,
            button_1200x800,
            button_900x600
        ]

        graphics_menu_running = True
        while graphics_menu_running:
            
            start_bg.rescale_and_show(self.window_size, self.screen)

            for button in button_list:
                button.show(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == ord('q'):
                        exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in button_list:
                        if button.conditions():
                            if button.mode == "fullscreen":
                                self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                                self.window_size = self.screen.get_size()
                                graphics_menu_running = False
                            elif button.mode == "fullscreen window":
                                self.screen = pygame.display.set_mode((0, 0))
                                self.window_size = self.screen.get_size()
                                graphics_menu_running = False
                            elif button.mode == "window":
                                self.screen = pygame.display.set_mode(button.window_size)
                                # nie ruszać! nie mam bladego pojęcia czemu,
                                # ale musi być dokładnie tak (self.window_size = self.screen.get_size() nie działa)
                                self.window_size = button.window_size
                                graphics_menu_running = False
            
            pygame.display.flip() #odświeżanie klatek


    def run_game(self):
        self.game_running = True
        self.player_velocity = 2
        self.lvl = 1
        self.green_area = GreenArea(self.window_size)

        self.backround_image = Background2(
            "assets/background2.png",
            (self.window_size[0]/2, self.window_size[1]/2),
            (1800, 1200)
        )
        self.backround_image.rescale(self.window_size)

        self.player = Player(
            "assets/player.png",
            (60, self.window_size[1]/2),
            (100,100)
        )
        
        formula_box = pygame.Rect(15, 42, 140, 32)
        formula_box_label = Icon(
            "assets/actual.png",
            (115,23),
            (200,32)
        )
        score_label = Icon(
            "assets/score.png",
            (115,91),
            (300,32)
        )

        graph = Graph(
            self.player,
            formula_box,
            "x**2",
            self.list_of_obstacles,
            self.green_area,
            self.screen
        )
        font = pygame.font.Font(None, 32)
        formula = ''
        actual_score_font = pygame.font.Font(None, 32)

        while self.game_running:
            pygame.time.delay(17)

            # self.screen.fill(self.color)

            self.backround_image.show(self.screen)
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        formula = self.editing_graph_formula(
                            formula_box,
                            formula_box_label,
                            formula,
                            graph.score
                        )
                    elif event.key == pygame.K_SPACE:
                        #Oh my god bless hermenegilda
                        hermenegilda = graph.draw_and_check(self.window_size, formula)
                        if hermenegilda == 1:
                            self.list_of_obstacles.append(Obstacle(self.window_size, len(self.list_of_obstacles)))
                            self.lvl += 1
                            for obstacle in self.list_of_obstacles:
                                obstacle.reroll(self.window_size)
                                obstacle.set_chance(self.lvl, obstacle.number)
                            self.green_area.reroll(self.window_size)
                        elif hermenegilda == -1:
                            self.lose_screen(graph.score)
                        
            if keys[pygame.K_q]:
                self.screen.fill(self.background_color)
                pygame.display.flip()
                exit()
            if keys[pygame.K_LEFT] and self.player.cords[0] - self.player.size[0]/2 - 10 > 0:
                self.player.cords = (self.player.cords[0] - self.player_velocity, self.player.cords[1])
                # self.player.cords[0] -= self.player_velocity
            if keys[pygame.K_RIGHT] and self.player.cords[0] - self.player.size[0]/2 - 90 < 0:
                self.player.cords = (self.player.cords[0] + self.player_velocity, self.player.cords[1])
                # self.player.cords[0] += self.player_velocity
            if keys[pygame.K_UP] and self.player.cords[1] - self.player.size[1]/2 - 96 > 0:
                self.player.cords = (self.player.cords[0], self.player.cords[1] - self.player_velocity)
                # self.player.cords[1] -= self.player_velocity
            if keys[pygame.K_DOWN] and self.player.cords[1] < self.window_size[1] - self.player.size[1]/2:
                self.player.cords = (self.player.cords[0], self.player.cords[1] + self.player_velocity)
                # self.player.cords[1] += self.player_velocity

            self.player.show(self.screen)

            # Rzeczy związane z oknem do wzoru
            formula_box_label.show(self.screen)
            score_label.show(self.screen)
            pygame.draw.rect(
                self.screen,
                pygame.Color('dodgerblue2'),
                formula_box,
                2
            )
            formula_text_surface = font.render(formula, True, (0, 0, 0))
            forumula_box_width = max(200, formula_text_surface.get_width() + 10)
            formula_box.w = forumula_box_width
            actual_score_img = actual_score_font.render(str(graph.score), True, (0, 0, 0))
            self.screen.blit(actual_score_img,(95, 81))
            
            self.screen.blit(formula_text_surface, (formula_box.x + 5, formula_box.y + 5))
            for obstacle in self.list_of_obstacles:
                obstacle.draw_obstacle(self.screen)
            self.green_area.draw_area(self.screen)

            # pygame.display.flip() #odświeżanie klatek
            pygame.display.update()

    def editing_graph_formula(self, formula_box, formula_box_label, old_text, actual_score):
        font = pygame.font.Font(None, 32)
        clock = pygame.time.Clock()
        text = old_text
        actual_score_font = pygame.font.Font(None, 32)
        score_label = Icon(
            "assets/score.png",
            (115,91),
            (300,32)
        )

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        return text
                    else:
                        text += event.unicode
            keys = pygame.key.get_pressed()
            if keys[pygame.K_BACKSPACE]:
                text = text[:-1]

            self.backround_image.show(self.screen)
            formula_box_label.show(self.screen)
            score_label.show(self.screen)
            
            formula_text_surface = font.render(text, True, (0, 0, 0))
            forumula_box_width = max(200, formula_text_surface.get_width() + 10)
            formula_box.w = forumula_box_width
            actual_score_img = actual_score_font.render(str(actual_score), True, (0, 0, 0))
            self.screen.blit(actual_score_img,(95, 81))

            self.screen.blit(formula_text_surface, (formula_box.x + 5, formula_box.y + 5))

            self.player.show(self.screen)

            pygame.draw.rect(
                self.screen,
                pygame.Color(0, 0, 0),
                formula_box,
                2
            )
            for obstacle in self.list_of_obstacles:
                obstacle.draw_obstacle(self.screen)
            self.green_area.draw_area(self.screen)

            pygame.display.flip()
            clock.tick(30)

    
    def lose_screen(self, score):
        try_again_button = Icon(
            "assets/try_again.png",
            (self.window_size[0]/2, self.window_size[1]/2 + 100),
            (200, 100)
        )
        score_button = Icon(
            "assets/big_score.png",
            (self.window_size[0]/2 - 20, self.window_size[1]/2 - 20),
            (200, 100)
        )
        you_lose_button = Icon(
            "assets/lose.png",
            (self.window_size[0]/2, self.window_size[1]/2 - 150),
            (900, 300)
        )
        start_bg = Background(
            "assets/background.png",
            (self.window_size[0]/2, self.window_size[1]/2),
            (1800, 1200)
        )
        score_font = pygame.font.Font(None, 100)
        score_img = score_font.render(str(score), True, (0, 0, 0))

        lose_screen_running = True
        while lose_screen_running:
            # self.screen.fill(self.background_color)
            start_bg.rescale_and_show(self.window_size, self.screen)
            try_again_button.show(self.screen)
            score_button.show(self.screen)
            you_lose_button.show(self.screen)
            self.screen.blit(score_img,(self.window_size[0]/2 + 80, self.window_size[1]/2 - 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == ord('q'):
                        self.screen.fill(self.background_color)
                        pygame.display.flip()
                        exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if try_again_button.conditions():
                        self.background_color = (0, 0, 0)
                        self.list_of_obstacles = []
                        self.green_area.reroll(self.window_size)
                        self.lvl = 0
                        self.main_menu()
                        lose_screen_running = False

            pygame.display.flip() #odświeżanie klatek