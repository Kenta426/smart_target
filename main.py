import pygame
from ball import *
from board import *
from target import *

NUM = 10
MUTATION = 0.2

pygame.init()
screen = pygame.display.set_mode((800,600))
background = pygame.Surface(screen.get_size())
background.fill((0,0,0))

done = False

balls = []

board = Board()
target = Target()
gen = Generation(NUM, board, screen,target, [])
gen.set_mutation(MUTATION)

count = 0
max_fit = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background, (0,0))


    gen.run()
    success = gen.count_success1()
    success2 = gen.count_success2()
    if gen.is_dead():
        result = gen.evaluate()
        new_board = board.reset()
        new_target = target.reset()
        new_gene = gen.natural_selection()

        gen = Generation(NUM, new_board, screen, new_target, new_gene)
        gen.set_mutation(MUTATION)
        count += 1

        temp_fit = max(result)
        if max_fit < temp_fit:
            max_fit = temp_fit

    myfont = pygame.font.SysFont("Helvetica", 15)
    # render text
    generation = myfont.render("Generation: " + str(count), 1, (255,255,255))
    fit = myfont.render("Max fitness: " + str(max_fit), 1, (255,255,255))
    mutation = myfont.render("Mutation Rate: " + str(MUTATION), 1, (255,255,255))
    suc1 = myfont.render("Board: " + str(success), 1, (255,255,255))
    suc2 = myfont.render("Target: " + str(success2), 1, (255,255,255))


    screen.blit(generation, (10, 10))
    screen.blit(fit, (10, 35))
    screen.blit(mutation, (10, 60))
    screen.blit(suc1, (10, 85))
    screen.blit(suc2, (10, 110))

    board.draw(screen)
    target.draw(screen)
    pygame.display.flip()
