# Importieren der Bibliotheken für die Verwendung des Spiels#
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Willkommens nachricht von Pygame verstecken #
import random
import pygame

# Klasse Settings für globale Variablen # 
class Settings:
    # Fenster Größen bestimmen #
    fenster_groeße_x = 600
    fenster_groeße_y = 400
    
    # Farben bestimmen #
    grau = pygame.Color(50, 50, 50)
    schwarz = pygame.Color(0, 0, 0)
    weiß = pygame.Color(255, 255, 255)
    rot = pygame.Color(255, 0, 0)
    gruen = pygame.Color(0, 160, 0)
    blau = pygame.Color(0, 0, 255)
    lila = pygame.Color(255, 0, 255)
    braun = pygame.Color('chocolate4') # Quelle: https://www.pygame.org/docs/ref/color_list.html #
    gelb = pygame.Color(255, 255, 0)
    orange = pygame.Color(220, 110, 0)
   
   # Regenbogenfarben bestimmen (für ein bestimmtes Feature einer Frucht) #
    x = 0
    y = 0
    z = 0
    regenbogen = pygame.Color(x, y, z)
    
    # Geschwindigkeit der Schlange und des Spiels an sich #
    schlangen_geschwindigkeit = 10
    fps_geschwindigkeit = 13

# Schlangen Klasse #
class Snake:
    def __init__(self):
        # Schlangen Variabeln bestimmen #
        self.schlangen_position = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        self.schlangen_körper = []

        # Richtungen bestimmen #
        self.richtung = None
        self.geaenderte_richtung = self.richtung

        # Abfrage für die Richtung der Schlange, sowie der Körper #
        if self.schlangen_position[0] >= 300 and self.schlangen_position[0] <= 600:
            self.richtung = "links"
            self.schlangen_körper = [[self.schlangen_position[0], self.schlangen_position[1]], [self.schlangen_position[0] + 10, self.schlangen_position[1]], [self.schlangen_position[0] + 20, self.schlangen_position[1]]]  #Schlangenkörper Idee aus folgendem Video: https://www.youtube.com/watch?v=Gc92z58-Qm4&t=774s&ab_channel=TheMorpheusTutorials
            self.geaenderte_richtung = self.richtung
        if self.schlangen_position[0] >= 0 and self.schlangen_position[0] <= 290:
            self.richtung = "rechts"
            self.schlangen_körper = [[self.schlangen_position[0], self.schlangen_position[1]], [self.schlangen_position[0] - 10, self.schlangen_position[1]], [self.schlangen_position[0] - 20, self.schlangen_position[1]]]
            self.geaenderte_richtung = self.richtung

    def move_snake(self):
        # Bewegung der Schlange #
        if self.richtung == "rechts":
            self.schlangen_position[0] += Settings.schlangen_geschwindigkeit
        if self.richtung == "links":
            self.schlangen_position[0] -= Settings.schlangen_geschwindigkeit
        if self.richtung == "oben":
            self.schlangen_position[1] -= Settings.schlangen_geschwindigkeit
        if self.richtung == "unten":
            self.schlangen_position[1] += Settings.schlangen_geschwindigkeit 

    def move_snake_body(self):
        # Bewegung des Schlangenkörpers #
        self.schlangen_körper.insert(0, list(self.schlangen_position))
        self.schlangen_körper.pop()

    def check_movement(self):
        # Prüfe ob die Schlange nicht in sich selbst schlängelt (wird verhindert, Idee von https://www.youtube.com/watch?v=_-KjEgCLQFw&ab_channel=CoderSpace) #
        if self.geaenderte_richtung == "rechts" and self.richtung != "links":
            self.richtung = "rechts"
        if self.geaenderte_richtung == "links" and self.richtung != "rechts":
            self.richtung = "links"
        if self.geaenderte_richtung == "oben" and self.richtung != "unten":
            self.richtung = "oben"
        if self.geaenderte_richtung == "unten" and self.richtung != "oben":
            self.richtung = "unten"

    def check_into_snake_body(self):
        # Wenn die Schlange in sich selbst schlängelt verliert man #
        for körper in self.schlangen_körper:
            if self.schlangen_position == körper:
                self.game_over = True
                self.check_game_over()

    def draw_rainbow_snake(self):
        if self.regenbogen:
            x = random.randint(0, 255)
            y = random.randint(0, 255)
            z = random.randint(0, 255)
            Settings.regenbogen = pygame.Color(x, y, z)
            
            # Schlange erscheinen lassen mit Regenbogenfarben effekt #
            for körper in self.schlangen_körper:
                pygame.draw.rect(self.fenster, Settings.regenbogen, pygame.Rect(körper[0], körper[1], 10, 10))

    def draw_snake(self):
        # Schlange erscheinen lassen #
        if not self.regenbogen:
            for körper in self.schlangen_körper:
                pygame.draw.rect(self.fenster, Settings.gruen, pygame.Rect(körper[0], körper[1], 10, 10))
    
    def draw_snake_body_parts(self):
        # Augen und Zunge zu den jeweiligen Richtungen erscheinen lassen  #
        if self.richtung == "rechts":
            # Augen #
            pygame.draw.rect(self.fenster, Settings.weiß, pygame.Rect(self.schlangen_position[0] + 4, self.schlangen_position[1], 4, 4))
            pygame.draw.rect(self.fenster, Settings.weiß, pygame.Rect(self.schlangen_position[0] + 4, self.schlangen_position[1] + 6, 4, 4))
            pygame.draw.rect(self.fenster, Settings.schwarz, pygame.Rect(self.schlangen_position[0] + 7, self.schlangen_position[1] + 1, 2, 2))
            pygame.draw.rect(self.fenster, Settings.schwarz, pygame.Rect(self.schlangen_position[0] + 7, self.schlangen_position[1] + 7, 2, 2))

            # Zunge #
            pygame.draw.rect(self.fenster, Settings.rot, pygame.Rect(self.schlangen_position[0] + 10, self.schlangen_position[1] + 4, 3, 3))

        if self.richtung == "links":
            # Augen #
            pygame.draw.rect(self.fenster, Settings.weiß, pygame.Rect(self.schlangen_position[0] + 2, self.schlangen_position[1], 4, 4))
            pygame.draw.rect(self.fenster, Settings.weiß, pygame.Rect(self.schlangen_position[0] + 2, self.schlangen_position[1] + 6, 4, 4))
            pygame.draw.rect(self.fenster, Settings.schwarz, pygame.Rect(self.schlangen_position[0] + 1, self.schlangen_position[1] + 1, 2, 2))
            pygame.draw.rect(self.fenster, Settings.schwarz, pygame.Rect(self.schlangen_position[0] + 1, self.schlangen_position[1] + 7, 2, 2))

            # Zunge #
            pygame.draw.rect(self.fenster, Settings.rot, pygame.Rect(self.schlangen_position[0] - 3, self.schlangen_position[1] + 4, 3, 3))

        if self.richtung == "oben":
            # Augen #
            pygame.draw.rect(self.fenster, Settings.weiß, pygame.Rect(self.schlangen_position[0], self.schlangen_position[1] + 2, 4, 4))
            pygame.draw.rect(self.fenster, Settings.weiß, pygame.Rect(self.schlangen_position[0] + 6, self.schlangen_position[1] + 2, 4, 4))
            pygame.draw.rect(self.fenster, Settings.schwarz, pygame.Rect(self.schlangen_position[0] + 1, self.schlangen_position[1] + 1, 2, 2))
            pygame.draw.rect(self.fenster, Settings.schwarz, pygame.Rect(self.schlangen_position[0] + 7, self.schlangen_position[1] + 1, 2, 2))

            # Zunge #
            pygame.draw.rect(self.fenster, Settings.rot, pygame.Rect(self.schlangen_position[0] + 4, self.schlangen_position[1] - 3, 3, 3))

        if self.richtung == "unten":
            # Augen #
            pygame.draw.rect(self.fenster, Settings.weiß, pygame.Rect(self.schlangen_position[0], self.schlangen_position[1] + 5, 4, 4))
            pygame.draw.rect(self.fenster, Settings.weiß, pygame.Rect(self.schlangen_position[0] + 6, self.schlangen_position[1] + 5, 4, 4))
            pygame.draw.rect(self.fenster, Settings.schwarz, pygame.Rect(self.schlangen_position[0] + 1, self.schlangen_position[1] + 7, 2, 2))
            pygame.draw.rect(self.fenster, Settings.schwarz, pygame.Rect(self.schlangen_position[0] + 7, self.schlangen_position[1] + 7, 2, 2))

            # Zunge #
            pygame.draw.rect(self.fenster, Settings.rot, pygame.Rect(self.schlangen_position[0] + 4, self.schlangen_position[1] + 10, 3, 3))

class Fruit(Snake):
    def __init__(self):
        super().__init__()
        
        # Bestimmen der Fruchtposition #
        self.frucht_position1 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        self.frucht_position2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        self.frucht_position3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        self.frucht_position4 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        self.frucht_position5 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        self.frucht_position6 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]

    def check_fruit_into_fruit(self):
        # Prüfe ob eine Frucht genau die gleiche Position hat wie eine andere Frucht, und wenn ja soll eine neue Position zugefügt werden #
        if self.frucht_position1 == self.frucht_position2:
            self.frucht_position2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position1 == self.frucht_position3:
            self.frucht_position3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position1 == self.frucht_position4:
            self.frucht_position4 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position1 == self.frucht_position5:
            self.frucht_position5 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position1 == self.frucht_position6:
            self.frucht_position6 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position2 == self.frucht_position3:
            self.frucht_position3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position2 == self.frucht_position4:
            self.frucht_position4 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position2 == self.frucht_position5:
            self.frucht_position5 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position2 == self.frucht_position6:
            self.frucht_position6 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position3 == self.frucht_position4:
            self.frucht_position4 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position3 == self.frucht_position5:
            self.frucht_position5 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position3 == self.frucht_position6:
            self.frucht_position6 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position4 == self.frucht_position5:
            self.frucht_position5 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position4 == self.frucht_position6:
            self.frucht_position6 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position5 == self.frucht_position6:
            self.frucht_position6 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]

    def snake_fruit_collision(self):
        # Kollision mit der Schlange und den Früchten #
        # Frucht gibt nur einen Punkt mit normaler Geschwindigkeit #
        if self.schlangen_position == self.frucht_position1:
            self.frucht_position1 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            self.schlangen_körper.append((-10, -10))
            self.punktestand += 1
            self.essens_sound.play()
            Settings.fps_geschwindigkeit = 13
            self.regenbogen = False
        
        # Frucht gibt nur drei Punkte mit normaler Geschwindigkeit #
        if self.schlangen_position == self.frucht_position2: 
            self.frucht_position2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            self.schlangen_körper.append((-10, -10))
            self.punktestand += 3
            self.essens_sound.play()
            Settings.fps_geschwindigkeit = 13
            self.regenbogen = False

        # Frucht gibt nur einen Punk aber eine höhere geschwindigkeit mit Regenbogenfarben effekt (bei kollision mit allen anderen Früchten wird dies wieder deaktiviert) #
        if self.schlangen_position == self.frucht_position3:
            self.frucht_position3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            self.schlangen_körper.append((-10, -10))
            self.punktestand += 1
            self.essens_sound.play()
            Settings.fps_geschwindigkeit = 23
            self.regenbogen = True
        
        # Frucht gibt nur 5 Punkte und eine etwas langsamere geschwindigkeit #
        if self.schlangen_position == self.frucht_position4:
            self.frucht_position4 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            self.schlangen_körper.append((-10, -10))
            self.punktestand += 5
            self.essens_sound.play()
            Settings.fps_geschwindigkeit = 8
            self.regenbogen = False
            
        # Frucht macht die Schlange größer als alle anderen Früchte und gibt eine normale geschwindigkeit #
        if self.schlangen_position == self.frucht_position5:
            self.frucht_position5 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            self.schlangen_körper.append((-10, -10))
            self.schlangen_körper.append((-10, -10))
            self.essens_sound.play()
            Settings.fps_geschwindigkeit = 13
            self.regenbogen = False

        # Frucht teleportiert die Schlange #
        if self.schlangen_position == self.frucht_position6:
            self.frucht_position6 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            self.schlangen_körper.append((-10, -10))
            self.schlangen_position = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]

            # Überprüfe ob die Schlange sich in einer dummen Stelle teleportiert hat #
            for barriere in self.barriere_körper1, self.barriere_körper2, self.barriere_körper3:
                if self.schlangen_position == barriere:
                    self.schlangen_position = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]

            # Überprüfe ob die Schlange in der Nähe der Barriere Teleportiert wird #
            for barriere in self.barriere_körper1:
                if self.schlangen_position[0] <= barriere[0] + 50 and self.schlangen_position[0] >= barriere[0] - 50 and self.schlangen_position[1] <= barriere[1] + 50 and self.schlangen_position[1] >= barriere[1] - 50:
                    self.schlangen_position = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            for barriere in self.barriere_körper2:
                if self.schlangen_position[0] <= barriere[0] + 50 and self.schlangen_position[0] >= barriere[0] - 50 and self.schlangen_position[1] <= barriere[1] + 50 and self.schlangen_position[1] >= barriere[1] - 50:
                    self.schlangen_position = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            for barriere in self.barriere_körper3:
                if self.schlangen_position[0] <= barriere[0] + 50 and self.schlangen_position[0] >= barriere[0] - 50 and self.schlangen_position[1] <= barriere[1] + 50 and self.schlangen_position[1] >= barriere[1] - 50:
                    self.schlangen_position = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]

            for körper in self.schlangen_körper:
                # Überprüfe ob die Schlange in sich selber Teleportiert hat #
                if körper == self.schlangen_position:
                    self.schlangen_position = [[random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]]

                # Überprüfe ob die Schlange in der Nähe des Spielfensters Telepotiert wird #
                if self.schlangen_position[0] <= 50 or self.schlangen_position[0] >= 550 or self.schlangen_position[1] <= 50 or self.schlangen_position[1] >= 350:
                    self.schlangen_position = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]

                # Überprüfe ob die Schlange in der Nähe seines eigenen Körpers Teleportiert wird #
                if körper[0] <= self.schlangen_position[0] + 50 and körper[0] >= self.schlangen_position[0] - 50 and körper[1] <= self.schlangen_position[1] + 50 and körper[1] >= self.schlangen_position[1] - 50:
                    self.schlangen_position = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]

            self.essens_sound.play()
            Settings.fps_geschwindigkeit = 13
            self.regenbogen = False

    def draw_fruits(self):
        # Früchte erscheinen lassen #
        pygame.draw.rect(self.fenster, Settings.rot, pygame.Rect(self.frucht_position1[0], self.frucht_position1[1], 10, 10))
        pygame.draw.rect(self.fenster, Settings.gruen, pygame.Rect(self.frucht_position1[0] + 4, self.frucht_position1[1] - 4, 2, 6))
        
        pygame.draw.rect(self.fenster, Settings.blau, pygame.Rect(self.frucht_position2[0], self.frucht_position2[1], 10, 10))
        pygame.draw.rect(self.fenster, Settings.gruen, pygame.Rect(self.frucht_position2[0] + 4, self.frucht_position2[1] - 4, 2, 6))

        pygame.draw.rect(self.fenster, Settings.lila, pygame.Rect(self.frucht_position3[0], self.frucht_position3[1], 10, 10))
        pygame.draw.rect(self.fenster, Settings.gruen, pygame.Rect(self.frucht_position3[0] + 4, self.frucht_position3[1] - 4, 2, 6))

        pygame.draw.rect(self.fenster, Settings.braun, pygame.Rect(self.frucht_position4[0], self.frucht_position4[1], 10, 10))
        pygame.draw.rect(self.fenster, Settings.gruen, pygame.Rect(self.frucht_position4[0] + 4, self.frucht_position4[1] - 4, 2, 6))
    
        pygame.draw.rect(self.fenster, Settings.gelb, pygame.Rect(self.frucht_position5[0], self.frucht_position5[1], 10, 10))
        pygame.draw.rect(self.fenster, Settings.gruen, pygame.Rect(self.frucht_position5[0] + 4, self.frucht_position5[1] - 4, 2, 6))
    
        pygame.draw.rect(self.fenster, Settings.orange, pygame.Rect(self.frucht_position6[0], self.frucht_position6[1], 10, 10))
        pygame.draw.rect(self.fenster, Settings.gruen, pygame.Rect(self.frucht_position6[0] + 4, self.frucht_position6[1] - 4, 2, 6))

class Barriere(Fruit):
    def __init__(self):
        super().__init__()

        # Barriere bestimmen #
        self.barriere1 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        self.barriere2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        self.barriere3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]

        # Barriere Aufbau #
        self.barriere_körper1 = []
        self.barriere_körper2 = []
        self.barriere_körper3 = []
    
    def check_barrier(self):
        # Überprüfe ob die Barrieren außerhalb des Spielfensters sind #
        if self.barriere1[0] <= 0 or self.barriere1[0] >= 600 or self.barriere1[1] <= 0 or self.barriere1[1] >= 400:
            self.barriere1 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.barriere2[0] <= 0 or self.barriere2[0] >= 600 or self.barriere2[1] <= 0 or self.barriere2[1] >= 400:
            self.barriere2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.barriere3[0] <= 0 or self.barriere3[0] >= 600 or self.barriere3[1] <= 0 or self.barriere3[1] >= 400:
            self.barriere3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]

        # Falls die Barrieren aufeinander liegen, werden sie neu generiert #
        if self.barriere1 == self.barriere2:
            self.barriere2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.barriere1 == self.barriere3:
            self.barriere3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.barriere2 == self.barriere3:
            self.barriere3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]

        # Abfrage wenn der Schlangenkopf in der Barriere spawnt #
        if self.barriere1 == self.schlangen_position:
            self.barriere1 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.barriere2 == self.schlangen_position:
            self.barriere2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.barriere3 == self.schlangen_position:
            self.barriere3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]

        # Ansonsten wird der Körper normal angepasst #
        else:
            self.barriere_körper1 = [[self.barriere1[0], self.barriere1[1]], [self.barriere1[0] + 10, self.barriere1[1]], [self.barriere1[0] + 20, self.barriere1[1]], [self.barriere1[0] - 10, self.barriere1[1]], [self.barriere1[0] - 20, self.barriere1[1]], [self.barriere1[0], self.barriere1[1] + 10], [self.barriere1[0], self.barriere1[1] + 20], [self.barriere1[0], self.barriere1[1] - 10], [self.barriere1[0], self.barriere1[1] - 20]]
            self.barriere_körper2 = [[self.barriere2[0], self.barriere2[1]], [self.barriere2[0] + 10, self.barriere2[1]], [self.barriere2[0] + 20, self.barriere2[1]], [self.barriere2[0] - 10, self.barriere2[1]], [self.barriere2[0] - 20, self.barriere2[1]], [self.barriere2[0], self.barriere2[1] + 10], [self.barriere2[0], self.barriere2[1] + 20], [self.barriere2[0], self.barriere2[1] - 10], [self.barriere2[0], self.barriere2[1] - 20]]
            self.barriere_körper3 = [[self.barriere3[0], self.barriere3[1]], [self.barriere3[0] + 10, self.barriere3[1]], [self.barriere3[0] + 20, self.barriere3[1]], [self.barriere3[0] - 10, self.barriere3[1]], [self.barriere3[0] - 20, self.barriere3[1]], [self.barriere3[0], self.barriere3[1] + 10], [self.barriere3[0], self.barriere3[1] + 20], [self.barriere3[0], self.barriere3[1] - 10], [self.barriere3[0], self.barriere3[1] - 20]]

    def check_into_barrier(self):
        # Prüfe ob die Schlange in die Barriere trifft #
        for barriere in self.barriere_körper1:
            if self.schlangen_position == barriere:
                self.game_over = True
                self.check_game_over()
        for barriere in self.barriere_körper2:
            if self.schlangen_position == barriere:
                self.game_over = True
                self.check_game_over()
        for barriere in self.barriere_körper3:
            if self.schlangen_position == barriere:
                self.game_over = True
                self.check_game_over()

    def draw_barriers(self):
        for barriere in self.barriere_körper1:
            pygame.draw.rect(self.fenster, Settings.weiß, pygame.Rect(barriere[0], barriere[1], 10, 10))

        for barriere in self.barriere_körper2:
            pygame.draw.rect(self.fenster, Settings.weiß, pygame.Rect(barriere[0], barriere[1], 10, 10))

        for barriere in self.barriere_körper3:
            pygame.draw.rect(self.fenster, Settings.weiß, pygame.Rect(barriere[0], barriere[1], 10, 10))

class extra_game_checks(Barriere):
    def __init__(self):
        super().__init__()
    
    def extra_options(self):
        # Prüfe ob eine Frucht im Körper der Schlange auftaucht, wenn ja soll eine neue Position zugefügt werden #
        for körper in self.schlangen_körper:
            if körper == self.frucht_position1:
                self.frucht_position1 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if körper == self.frucht_position2:
                self.frucht_position2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if körper == self.frucht_position3:
                self.frucht_position3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if körper == self.frucht_position4:
                self.frucht_position4 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if körper == self.frucht_position5:
                self.frucht_position5 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if körper == self.frucht_position6:
                self.frucht_position6 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]    

        # Überprüfe ob die barriere am Score erscheinen wird #
        if self.barriere1[0] <= 120 and self.barriere1[1] >= 350:
            self.barriere1 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.barriere2[0] <= 120 and self.barriere2[1] >= 350:
            self.barriere2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.barriere3[0] <= 120 and self.barriere3[1] >= 350:
            self.barriere3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]

        # Wenn eine Frucht auf einer Barriere auftaucht, so wird eine neue Position für die Frucht generiert #
        for barriere in self.barriere_körper1:
            if self.frucht_position1 == barriere:
                self.frucht_position1 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if self.frucht_position2 == barriere:
                self.frucht_position2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if self.frucht_position3 == barriere:
                self.frucht_position3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if self.frucht_position4 == barriere:
                self.frucht_position4 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if self.frucht_position5 == barriere:
                self.frucht_position5 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if self.frucht_position6 == barriere:
                self.frucht_position6 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]

        for barriere in self.barriere_körper2:
            if self.frucht_position1 == barriere:
                self.frucht_position1 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if self.frucht_position2 == barriere:
                self.frucht_position2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if self.frucht_position3 == barriere:
                self.frucht_position3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if self.frucht_position4 == barriere:
                self.frucht_position4 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if self.frucht_position5 == barriere:
                self.frucht_position5 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if self.frucht_position6 == barriere:
                self.frucht_position6 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]

        for barriere in self.barriere_körper3:
            if self.frucht_position1 == barriere:
                self.frucht_position1 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if self.frucht_position2 == barriere:
                self.frucht_position2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if self.frucht_position3 == barriere:
                self.frucht_position3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if self.frucht_position4 == barriere:
                self.frucht_position4 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if self.frucht_position5 == barriere:
                self.frucht_position5 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
            if self.frucht_position6 == barriere:
                self.frucht_position6 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]

        # Überprüfe ob eine Frucht am Score auftaucht, wenn ja soll eine neue Position generiert werden #
        if self.frucht_position1[0] <= 120 and self.frucht_position1[1] >= 350:
            self.frucht_position1 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position2[0] <= 120 and self.frucht_position2[1] >= 350:
            self.frucht_position2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position3[0] <= 120 and self.frucht_position3[1] >= 350:
            self.frucht_position3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position4[0] <= 120 and self.frucht_position4[1] >= 350:
            self.frucht_position4 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position5[0] <= 120 and self.frucht_position5[1] >= 350:
            self.frucht_position5 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position6[0] <= 120 and self.frucht_position6[1] >= 350:
            self.frucht_position6 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]

        # Überprüfe ob die Früchte außerhalb des Fensters erscheinen #
        if self.frucht_position1[0] <= 0 or self.frucht_position1[0] >= 600 or self.frucht_position1[1] <= 0 or self.frucht_position1[1] >= 400:
            self.frucht_position1 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
        if self.frucht_position2[0] <= 0 or self.frucht_position2[0] >= 600 or self.frucht_position2[1] <= 0 or self.frucht_position2[1] >= 400:
            self.frucht_position2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10)* 10]
        if self.frucht_position3[0] <= 0 or self.frucht_position3[0] >= 600 or self.frucht_position3[1] <= 0 or self.frucht_position3[1] >= 400:
            self.frucht_position3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y)//10 * 10]
        if self.frucht_position4[0] <= 0 or self.frucht_position4[0] >= 600 or self.frucht_position4[1] <= 0 or self.frucht_position4[1] >= 400:
            self.frucht_position4 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y)//10 * 10]
        if self.frucht_position5[0] <= 0 or self.frucht_position5[0] >= 600 or self.frucht_position5[1] <= 0 or self.frucht_position5[1] >= 400:
            self.frucht_position5 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y)//10 * 10]
        if self.frucht_position6[0] <= 0 or self.frucht_position6[0] >= 600 or self.frucht_position6[1] <= 0 or self.frucht_position6[1] >= 400:
            self.frucht_position6 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y)//10 * 10]

    def check_into_window(self):
        # Wenn die Schlange den Spielfenster berührt, hat man verloren #
        if self.schlangen_position[0] + 10 > Settings.fenster_groeße_x or self.schlangen_position[0] < 0:
            self.game_over = True
            self.check_game_over()
        if self.schlangen_position[1] + 10 > Settings.fenster_groeße_y or self.schlangen_position[1] < 0:
            self.game_over = True
            self.check_game_over()

    def squared_environment(self):
        # Kariertes Spielfeld #
        for kariert in range(0, Settings.fenster_groeße_x, 10):
            pygame.draw.line(self.fenster, Settings.schwarz, (kariert, 0), (kariert, Settings.fenster_groeße_y))
        for kariert in range(0, Settings.fenster_groeße_y, 10):
            pygame.draw.line(self.fenster, Settings.schwarz, (0, kariert), (Settings.fenster_groeße_x, kariert))

    def score(self):
        # Score-, Font und Surface festlegen und anzeigen lassen #
        self.punktestand_font = pygame.font.SysFont('bauhaus 93', 20)
        self.punktestand_surface = self.punktestand_font.render("Score : "+ str(self.punktestand), True, Settings.weiß)
        self.fenster.blit(self.punktestand_surface,(0,380))
        
class Game(extra_game_checks):
    def __init__(self):
        super().__init__()
        # Initialisierung aller wichtigen Pygame-Modulen #
        pygame.init()

        # Spielfenster einen Namen hinzufügen #
        pygame.display.set_caption("Snake")

        # Fenster bestimmen #
        self.fenster = pygame.display.set_mode((Settings.fenster_groeße_x, Settings.fenster_groeße_y))
        self.fenster.fill(Settings.grau)
        
        # FPS bestimmen #
        self.fps = pygame.time.Clock()

        # Musik bestimmen und abspielen #
        self.music = pygame.mixer.music.load(os.path.join('Sound', 'music.mp3')) #Quelle: https://www.youtube.com/watch?v=06R6-fAcbrk&ab_channel=DaissMusicFree
        self.music = pygame.mixer.music.set_volume(0.05)
        self.music = pygame.mixer.music.play(-1, 0.0)

        # Score festlegen #
        self.punktestand = 0

        # Game Over Variable um zur Überprüfung ob man verloren hat #
        self.game_over = False

        # Geheime Tastenkombination festlegen #
        self.geheimnis = True

        # Rainbow Variable um die Schlange verschiedene Farben geben kann #
        self.regenbogen = False

        # Essens sound #
        self.essens_sound = pygame.mixer.Sound(os.path.join('Sound', 'crunch.wav'))

    def run_game(self):
        # Schleife des Spiels #
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # pygame.key.get_pressed methode abspeichern um die Geheime Tastenkombination am laufen zu bringen #
                g_t_kombination = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.geaenderte_richtung = "rechts"
                    if event.key == pygame.K_a:
                        self.geaenderte_richtung = "links"
                    if event.key == pygame.K_w:
                        self.geaenderte_richtung = "oben"
                    if event.key == pygame.K_s:
                        self.geaenderte_richtung = "unten"
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_SPACE:
                        # Pause #
                        self.pause = True
                        self.pause_game()

                    # Geheime Tastenkombination Überprüfung #
                    if g_t_kombination[pygame.K_p] and g_t_kombination[pygame.K_r] and g_t_kombination[pygame.K_o]: 
                        if self.geheimnis == True:
                            self.punktestand += 5
                            self.geheimnis = False
            
            # Methoden aufrufen damit das Spiel funktioniert #
            self.move_snake()
            self.check_movement()
            self.check_into_snake_body()
            self.check_fruit_into_fruit()
            self.snake_fruit_collision()
            self.move_snake_body()
            self.check_barrier()
            self.check_into_barrier()
            self.extra_options()
            self.check_into_window()
            self.draw_barriers()
            self.squared_environment()
            self.score()
            self.draw_rainbow_snake()
            self.draw_snake()
            self.draw_snake_body_parts()
            self.draw_fruits()
            self.fps.tick(Settings.fps_geschwindigkeit)
            pygame.display.update()
            self.fenster.fill(Settings.grau)

    def pause_game(self):
        # Pause-, Font und Surface festlegen und anzeigen lassen #
        self.pause_schrift = pygame.font.SysFont('bauhaus 93', 30)
        self.pause_oberflaeche = self.pause_schrift.render('Pause', True, Settings.rot)
        self.squared_environment()
        self.fenster.blit(self.pause_oberflaeche, (260, 190))
        pygame.display.update()

        # Pause Schleife #
        while self.pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_SPACE:
                        self.pause = False
    

    def check_game_over(self):
        pygame.time.wait(1000)
        # Game Over-, Font und Surface festlegen und anzeigen lassen #
        self.squared_environment()
        self.game_over_schrift = pygame.font.SysFont('bauhaus 93', 30)
        self.game_over_oberfläche = self.game_over_schrift.render('You lost!', True, Settings.rot)
        self.game_over_oberfläche2 = self.game_over_schrift.render('Your score was: ' + str(self.punktestand), True, Settings.rot)
        self.game_over_oberfläche3 = self.game_over_schrift.render('"Space" to resart the game!', True, Settings.gruen)
        self.fenster.blit(self.game_over_oberfläche, (150, 150))
        self.fenster.blit(self.game_over_oberfläche2, (150, 180))
        self.fenster.blit(self.game_over_oberfläche3, (150, 220))
        pygame.display.update()

        # Game Over Schleife #
        while self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_SPACE:
                        # Schlangen Variabeln bestimmen #
                        self.schlangen_position = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
                        self.schlangen_körper = []

                        # Abfrage für die Richtung der Schlange, sowie der Körper #
                        if self.schlangen_position[0] >= 300 and self.schlangen_position[0] <= 600:
                            self.richtung = "links"
                            self.schlangen_körper = [[self.schlangen_position[0], self.schlangen_position[1]], [self.schlangen_position[0] + 10, self.schlangen_position[1]], [self.schlangen_position[0] + 20, self.schlangen_position[1]]]  #Schlangenkörper Idee aus folgendem Video: https://www.youtube.com/watch?v=Gc92z58-Qm4&t=774s&ab_channel=TheMorpheusTutorials
                            self.geaenderte_richtung = self.richtung
                        if self.schlangen_position[0] >= 0 and self.schlangen_position[0] <= 290:
                            self.richtung = "rechts"
                            self.schlangen_körper = [[self.schlangen_position[0], self.schlangen_position[1]], [self.schlangen_position[0] - 10, self.schlangen_position[1]], [self.schlangen_position[0] - 20, self.schlangen_position[1]]]
                            self.geaenderte_richtung = self.richtung

                        # Barriere bestimmen #
                        self.barriere1 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
                        self.barriere2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
                        self.barriere3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
                        
                        # Falls die Barrieren aufeinander liegen, werden sie neu generiert #
                        if self.barriere1 == self.barriere2:
                            self.barriere2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
                        if self.barriere1 == self.barriere3:
                            self.barriere3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
                        if self.barriere2 == self.barriere3:
                            self.barriere3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]

                        # Barriere Aufbau #
                        self.barriere_körper1 = []
                        self.barriere_körper2 = []
                        self.barriere_körper3 = []

                        # Abfrage wenn der Schlangenkopf in der Barriere spawnt #
                        if self.barriere1 == self.schlangen_position:
                            self.barriere1 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
                        if self.barriere2 == self.schlangen_position:
                            self.barriere2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
                        if self.barriere3 == self.schlangen_position:
                            self.barriere3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
                        
                        # Ansonsten wird der Körper normal angepasst #
                        else:
                            self.barriere_körper1 = [[self.barriere1[0], self.barriere1[1]], [self.barriere1[0] + 10, self.barriere1[1]], [self.barriere1[0] - 10, self.barriere1[1]], [self.barriere1[0], self.barriere1[1] + 10], [self.barriere1[0], self.barriere1[1] - 10]]
                            self.barriere_körper2 = [[self.barriere2[0], self.barriere2[1]], [self.barriere2[0] + 10, self.barriere2[1]], [self.barriere2[0] - 10, self.barriere2[1]], [self.barriere2[0], self.barriere2[1] + 10], [self.barriere2[0], self.barriere2[1] - 10]]
                            self.barriere_körper3 = [[self.barriere3[0], self.barriere3[1]], [self.barriere3[0] + 10, self.barriere3[1]], [self.barriere3[0] - 10, self.barriere3[1]], [self.barriere3[0], self.barriere3[1] + 10], [self.barriere3[0], self.barriere3[1] - 10]]

                        # Alles andere wieder auf normal setzen #
                        self.frucht_position1 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10] #Idee mit random.randrange vom Folgenden Video: https://www.youtube.com/watch?v=_-KjEgCLQFw&ab_channel=CoderSpace
                        self.frucht_position2 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
                        self.frucht_position3 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
                        self.frucht_position4 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
                        self.frucht_position5 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
                        self.frucht_position6 = [random.randint(1, Settings.fenster_groeße_x//10) * 10, random.randint(1, Settings.fenster_groeße_y//10) * 10]
                        self.punktestand = 0
                        self.game_over = False
                        self.geheimnis = True
                        self.regenbogen = False
                        Settings.fps_geschwindigkeit = 13
                        self.game_over = False

# Hauptprogramm #
game = Game()
game.run_game()