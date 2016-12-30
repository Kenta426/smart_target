import pygame
import random

BOARD_WIDTH = 5
BOARD_HEIGHT = 50

class Board:
    def __init__(self):
        random.seed()
        x = random.randint(400, 800 - BOARD_WIDTH)
        y = random.randint(0, 300 - BOARD_HEIGHT)
        self.pos = (x,y)
        self.hit = False

    def draw(self, screen):
        if self.hit:
            color = (0, 200, 255)
        else:
            color = (255, 255, 255)

        pygame.draw.rect(screen, color, [self.pos[0], self.pos[1], BOARD_WIDTH, BOARD_HEIGHT])

    def check_collide(self, ball):
        if ((ball.pos[1] > self.pos[1] and ball.pos[1] < self.pos[1]+BOARD_HEIGHT)
        and (ball.pos[0]+ball.radius > self.pos[0]
        and ball.pos[0]-ball.radius < self.pos[0] + BOARD_WIDTH)):
            self.hit = True
            ball.board_hit = True
            if ball.vel[0] < 0:
                ball.pos[0] = self.pos[0] + BOARD_WIDTH + ball.radius
            else:
                ball.pos[0] = self.pos[0] - ball.radius
            ball.vel[0] = -0.8*ball.vel[0]
        elif (ball.pos[0]+ball.radius > self.pos[0]
        and ball.pos[0]-ball.radius < self.pos[0] + BOARD_WIDTH):
            dist = min(abs(ball.pos[1] - self.pos[1]), abs(ball.pos[1] - (self.pos[1] + BOARD_HEIGHT)))
            if dist < ball.dist_board:
                ball.dist_board = dist
        else:
            ball.dist_board = 1000

    def reset(self):
        self.hit = False
        return self
