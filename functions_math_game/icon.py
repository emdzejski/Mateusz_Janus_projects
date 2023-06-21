from cmath import pi
from enum import Enum
from random import *
import pygame
import time
# from math import *
import numpy
from sympy import *

class Icon:
    """Podstawowa przechowująca grafiki, ich koordynaty i ich wielkość, służaca do ich wyświetlania i sprawdzania czy są wciśnięte"""
    def __init__(self, image, cords, size):
        self.image = pygame.image.load(image) # zmienna przechowująca grafikę
        self.cords = cords # tupla przechowująca położenie w oknie (x,y)
        self.size = size # tupla przechowująca wymiary grafiki (szerokość, wysokość)
    
    def show(self, screen):
        x = self.cords[0] - self.size[0]/2 # wyrównywanie środka grafiki
        y = self.cords[1] - self.size[1]/2 # do położenia 
        screen.blit(self.image, (x,y))
    
    def conditions(self): #jeśli myszka znajduje się na grafice zwraca True, jeśli nie zwraca False
        mouse_position = pygame.mouse.get_pos()
        if (self.cords[0] - self.size[0]/2 < mouse_position[0] \
            and mouse_position[0] < self.cords[0] + self.size[0]/2) \
            and (self.cords[1] - self.size[1]/2 < mouse_position[1] \
            and mouse_position[1] < self.cords[1] + self.size[1]/2):
            return True
        else:
            return False

    def change_cords(self, cords):
        self.cords = cords

class Background(Icon):
    """Klasa ustawiająca tło w menu"""
    def __init__(self, image, cords, size):
        self.image = pygame.image.load(image)
        self.cords = cords
        self.size = size
    
    def rescale_and_show(self, w_size, screen):
        bg_img = pygame.transform.scale(self.image, (w_size[0],w_size[1]))
        screen.blit(bg_img,(0,0))


class Background2(Icon):
    """Klasa ustawiająca tło w grze"""
    def __init__(self, image, cords, size):
        self.image = pygame.image.load(image)
        self.cords = cords
        self.size = size
    
    def rescale(self, w_size):
        self.image = pygame.transform.scale(self.image, (w_size[0],w_size[1]))
    
    def show(self,screen):
        screen.blit(self.image.convert(),(0,0))



class Button(Icon):
    """"Klasa służąca do wyświetlania przycisku i sprawdzania czy został wcśnięty"""
    def __init__(self, image, cords, size, window_size, mode):
        self.image = pygame.image.load(image) 
        self.cords = cords 
        self.size = size 
        self.mode = mode
        self.window_size = window_size


class Player(Icon):
    """Klasa gracza służąca do zmieniania jego pozycji, obracania i wyświetlania modelu"""""
    image: pygame.Surface
    cords: tuple
    size: tuple

    def __init__(self, image, cords, size):
        self.image = pygame.image.load(image)
        self.cords = cords
        self.size = size

    def rot(self,function):
        x = Symbol('x')
        f_prime = eval(function).diff(x)
        f_deriv = lambdify(x, f_prime)
        angle_tangent = f_deriv(self.size[0]/4)
        rad_angle = atan(angle_tangent)
        angle = rad_angle*360/(2*pi) - 32
        rot_image = pygame.transform.rotate(self.image, angle)
        rect = rot_image.get_rect(center = self.image.get_rect(center = (self.cords[0],self.cords[1]-10)).center)

        return [rot_image,rect]


class Point(Icon):
    """Klasa tworząca pojedyńczy punkt na wykresie"""
    def __init__(self, image, cords, size):
        self.image = pygame.image.load(image)
        self.cords = cords
        self.size = size


class Graph:
    """Klasa tworząca wykres funkcji podanej jako argument poprzez wyświetlenie wielu punktów"""
    def __init__(self, player, rect, function, list_of_obstacles, green_area, screen,):
        self.rect = rect
        self.player = player
        self.function = function
        self.list_of_obstacles = list_of_obstacles
        self.green_area = green_area
        self.screen = screen
        self.score = 0
        self.highscore = 0
        try:
            with open("highscore.txt") as file:
                for line in file:
                    self.highscore = int(line)
            file.close()
        except FileNotFoundError:
            file = open("highscore.txt","w")
            file.write('0')
            file.close()


    def find(self, function):
        txt = '-(' + function.replace('x','t') + ')'
        txt2 = function.replace('x','0')

        while 'etp' in txt:
            txt = txt[0 : txt.find('etp')+1] + 'x' + txt[ txt.find('etp')+2 : ]

        while 'e0p' in txt2:
            txt2 = txt2[0 : txt2.find('e0p')+1] + 'x' + txt2[ txt2.find('e0p')+2 : ]

        while 'nett' in txt:
            txt = txt[0 : txt.find('nett')+2] + 'x' + txt[ txt.find('nett')+3 : ]

        while 'ne0t' in txt2:
            txt2 = txt2[0 : txt2.find('ne0t')+2] + 'x' + txt2[ txt2.find('ne0t')+3 : ]

        return [txt,txt2]


    def draw_and_check(self, w_size, function):
        [f_x , f_0] = self.find(function)
        rot_img = self.player.rot(function)[0]
        rect = self.player.rot(function)[1]

        for x in numpy.arange(self.player.cords[0], w_size[0], 1):
            t = x - self.player.cords[0]
            point = Point("assets/dot.png",(x, eval(f_x) + self.player.cords[1] + eval(f_0)),(3,3))
            point.show(self.screen)
            self.screen.blit(rot_img,rect)
            for obstacle in self.list_of_obstacles:
                obstacle.draw_obstacle(self.screen)
            self.green_area.draw_area(self.screen)

            if self.green_area.is_collision_detected(point.cords[0], point.cords[1]):
                self.score += 1
                if self.score > self.highscore:
                    self.highscore = self.score
                    f = open("highscore.txt","w")
                    f.write(str(self.highscore))
                return 1
            for obstacle in self.list_of_obstacles:
                if obstacle.chance > obstacle.random_number:
                    if obstacle.is_collision_detected(point.cords[0], point.cords[1]):
                        return -1
            if point.cords[0] > w_size[0] or point.cords[0] < 0:
                return
            if point.cords[1] > w_size[1] or point.cords[1] < 0:
                return

            time.sleep(0.0001)
            pygame.display.flip()

class ObstacleType(Enum):
    CIRCLE = 1
    RECTANGLE = 2

class Obstacle:
    type: ObstacleType
    cords: tuple
    size: tuple
    rotation_angle: float
    number: float
    radius: float
    random_number: float

    def __init__(self, window_size: tuple, number: int):
        self.type = choice([type.value for type in ObstacleType])
        if self.type == 1:
            self.cords = (randrange(250, round(window_size[0]-250)),randrange(0, round(window_size[1]-100)))
        elif self.type == 2:
            self.cords = (randrange(250, round(9*window_size[0]/10 -250)), randrange(0, round(9*window_size[1]/10)))

        if self.type == 1:
            self.radius = randrange(round((window_size[0] + window_size[1])/40 - 20), round((window_size[0] + window_size[1])/40 + 20))
            self.size = (0,0)
        elif self.type == 2:
            self.radius = 0
            self.size = (randrange(round(window_size[0]/10 - 20),round(window_size[0]/10 +20)), randrange(round(window_size[1]/10 - 20), round(window_size[1]/10 +20)))
        self.rotation_angle = uniform(0, 6.28)
        self.chance = 0
        self.number = number
        self.random_number = random()

    def set_chance(self, lvl, number):
        k = lvl - number -1
        self.chance = (2**k - 1)/(2**k)
        if self.chance < 0:
            self.chance = 0
    
    def reroll(self, window_size):
        self.type = choice([type.value for type in ObstacleType])
        if self.type == 1:
            self.cords = (randrange(250, round(window_size[0]-250)),randrange(0, round(window_size[1]-100)))
        elif self.type == 2:
            self.cords = (randrange(250, round(9*window_size[0]/10 -250)), randrange(0, round(9*window_size[1]/10)))

        if self.type == 1:
            self.radius = randrange(round((window_size[0] + window_size[1])/40 - 20), round((window_size[0] + window_size[1])/40 + 20))
            self.size = (0,0)
        elif self.type == 2:
            self.radius = 0
            self.size = (randrange(round(window_size[0]/10 - 20),round(window_size[0]/10 +20)), randrange(round(window_size[1]/10 - 20), round(window_size[1]/10 +20)))
        self.rotation_angle = uniform(0, 6.28)
        self.random_number = random()

    def draw_obstacle(self,screen):
        if self.chance > self.random_number:
            if self.type == 2:
                pygame.draw.rect(screen, (255,0,0), pygame.Rect(self.cords[0],self.cords[1],self.size[0],self.size[1]))
            elif self.type == 1:
                pygame.draw.circle(screen, (255,0,0), self.cords, self.radius)
    
    def is_collision_detected(self, x, y):
        if self.type == 2:
            rect = pygame.Rect(self.cords[0],self.cords[1],self.size[0],self.size[1])
            return rect.collidepoint(x,y)
        elif self.type == 1:
            if (x - self.cords[0])**2 + (y - self.cords[1])**2 <= self.radius**2:
                return True
            else:
                return False
            

class GreenArea:
    type: ObstacleType
    cords: tuple
    size: tuple
    radius: float

    def __init__(self, window_size: tuple):
        self.type = choice([type.value for type in ObstacleType])
        if self.type == 1:
            self.cords = (randrange(round(window_size[0]-150),round(window_size[0]-50)),randrange(0, round(window_size[1]-100)))
        elif self.type == 2:
            self.cords = (randrange(round(window_size[0]-150),round(window_size[0]-50)), randrange(0, round(9*window_size[1]/10)))

        if self.type == 1:
            self.radius = randrange(round((window_size[0] + window_size[1])/40 - 20), round((window_size[0] + window_size[1])/40 + 20))
            self.size = (0,0)
        elif self.type == 2:
            self.radius = 0
            self.size = (randrange(round(window_size[0]/10 - 20),round(window_size[0]/10 +20)), randrange(round(window_size[1]/10 - 20), round(window_size[1]/10 +20)))
    
    def reroll(self, window_size):
        self.type = choice([type.value for type in ObstacleType])
        if self.type == 1:
            self.cords = (randrange(round(window_size[0]-150),round(window_size[0]-50)),randrange(0, round(window_size[1]-100)))
        elif self.type == 2:
            self.cords = (randrange(round(window_size[0]-150),round(window_size[0]-50)), randrange(0, round(9*window_size[1]/10)))

        if self.type == 1:
            self.radius = randrange(round((window_size[0] + window_size[1])/40 - 20), round((window_size[0] + window_size[1])/40 + 20))
            self.size = (0,0)
        elif self.type == 2:
            self.radius = 0
            self.size = (randrange(round(window_size[0]/10 - 20),round(window_size[0]/10 +20)), randrange(round(window_size[1]/10 - 20), round(window_size[1]/10 +20)))

    def draw_area(self,screen):
        if self.type == 2:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(self.cords[0],self.cords[1],self.size[0],self.size[1]))
        elif self.type == 1:
            pygame.draw.circle(screen, (0,255,0), self.cords, self.radius)

    def is_collision_detected(self, xx, yy):
        if self.type == 2:
            rect = pygame.Rect(self.cords[0],self.cords[1],self.size[0],self.size[1])
            return rect.collidepoint(xx,yy)
        elif self.type == 1:
            if (xx - self.cords[0])**2 + (yy - self.cords[1])**2 <= self.radius**2:
                return True
            else:
                return False