import pygame
import random

TARGET_WIDTH = 50
TARGET_HEIGHT = 5

class Target:
    def __init__(self):
        random.seed()
        x = random.randint(0, 400 - TARGET_WIDTH)
        self.pos = (x, 600-TARGET_HEIGHT)
        self.hit = False

    def draw(self, screen):
        if self.hit:
            color = (0, 200, 255)
        else:
            color = (255, 255, 255)

        pygame.draw.rect(screen, color, [self.pos[0], self.pos[1], TARGET_WIDTH, TARGET_HEIGHT])


    def check_hit(self, b):
        if ((b.pos[0] > self.pos[0] and b.pos[0] < self.pos[0] + TARGET_WIDTH)
        and (b.pos[1] + b.radius > self.pos[1])):
            if b.board_hit:
                self.hit = True
                b.target_hit = True
                b.vel[1] = b.vel[1] = -0.8*b.vel[1]
                b.pos[1] = self.pos[1] - b.radius

        elif (b.pos[1] + b.radius > self.pos[1]):
            dist = min(abs(b.pos[0] - self.pos[0]), abs(b.pos[0] - (self.pos[0] + TARGET_WIDTH)))
            if dist < b.dist_target:
                b.dist_target = dist
        else:
            b.dist_target = 1000

    def reset(self):
        self.hit = False
        return self
