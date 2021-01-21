import pygame
import sideMenu
pygame.init()


def main():
    width, height = 800, 600
    beige = (234, 227, 199)
    drag = False

    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Drawing Board')
    board = Board(0, 0, 600, 600)
    clock = pygame.time.Clock()
    menu = sideMenu.Menu()

    run = True
    while run:
        # input
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if menu.clicked(pygame.mouse.get_pos()) == 1:
                    board.reset()
                drag = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                drag = False
                board.set_lastP()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                board.reset()

        # Update
        pen_width = menu.get_width()
        pen_color = menu.get_color()

        win.fill(beige)

        if drag and board.is_over(pygame.mouse.get_pos()):
            board.draw(pygame.mouse.get_pos(), pen_width, pen_color)

        # Show
        board.show(win)
        menu.show(win)
        pygame.display.update()


class Board:

    white = (255, 255, 255)

    def __init__(self, x, y, width, height):
        self.x, self.y, self.width, self.height, = x, y, width, height
        self.board = pygame.Surface((self.width, self.height))
        self.reset()
        self.lastP = None

    def reset(self):
        self.board.fill(self.white)

    def draw(self, pos, width, color):
        if not self.lastP:
            self.lastP = pos
        else:
            pygame.draw.line(self.board, color, self.lastP, pos, width * 2 + 1)
            self.lastP = pos
        pygame.draw.circle(self.board, color, pos, width)

    def show(self, win):
        win.blit(self.board, (self.x, self.y))

    def is_over(self, pos):
        if self.x <= pos[0] <= self.width - self.x and self.y <= pos[1] <= self.height - self.x:
            return True
        return False

    def set_lastP(self):
        self.lastP = None


if __name__ == "__main__":
    main()
