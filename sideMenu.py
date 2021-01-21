import pygame


class Menu:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    purple = (255, 0, 255)
    cyan = (0, 255, 255)

    colWidth, colHeight = 50, 50

    def __init__(self):
        self.scale = (75, 75)

        self.resetB = pygame.image.load("Images/refresh.png")
        self.resetB = pygame.transform.scale(self.resetB, self.scale)
        self.resetBRect = pygame.Rect((600, 0), self.scale)

        self.pen_plus = pygame.image.load("Images/plus.png")
        self.pen_plus = pygame.transform.scale(self.pen_plus, self.scale)
        self.pen_plusRect = pygame.Rect((600, 100), self.scale)

        self.pen_minus = pygame.image.load("Images/remove.png")
        self.pen_minus = pygame.transform.scale(self.pen_minus, self.scale)
        self.pen_minusRect = pygame.Rect((700, 100), self.scale)

        self.color_buttons = {
            "blackB": Button(600, 500, self.colWidth, self.colHeight, self.black),
            "blueB": Button(650, 500, self.colWidth, self.colHeight, self.blue),
            "purpleB": Button(700, 500, self.colWidth,
                              self.colHeight, self.purple),
            "redB": Button(750, 500, self.colWidth, self.colHeight, self.red),
            "yellowB": Button(600, 550, self.colWidth,
                              self.colHeight, self.yellow),
            "greenB": Button(650, 550, self.colWidth,
                             self.colHeight, self.green),
            "cyanB": Button(700, 550, self.colWidth, self.colHeight, self.cyan),
            "whiteB": Button(750, 550, self.colWidth,
                             self.colHeight, self.white)

        }

        self.pen_width = 8
        self.pen_color = self.black

    def show(self, win):
        win.blits(((self.resetB, self.resetBRect), (self.pen_plus,
                                                    self.pen_plusRect), (self.pen_minus, self.pen_minusRect)))
        for but in self.color_buttons.values():
            but.show(win)

    def clicked(self, pos):
        if self.pen_minusRect.collidepoint(pos):
            if self.pen_width > 2:
                self.set_width(self.pen_width - 2)
        elif self.pen_plusRect.collidepoint(pos):
            self.set_width(self.pen_width + 2)
        elif self.resetBRect.collidepoint(pos):
            return 1

        for but in self.color_buttons.values():
            if but.isOver(pos):
                self.pen_color = but.get_color()

    def set_width(self, value):
        self.pen_width = value

    def set_color(self, color):
        self.pen_color = color

    def get_color(self):
        return self.pen_color

    def get_width(self):
        return self.pen_width


class Button:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def show(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def isOver(self, pos):
        if self.rect.collidepoint(pos):
            return True
        return False

    def get_color(self):
        return self.color
