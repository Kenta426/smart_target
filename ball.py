import pygame
import random
import numpy as np

def CDF(index, lst):
    ans = []
    for i in range(len(lst)):
        ans.append(sum(lst[0:i+1]))

    for i in range(len(lst)):
        if index > lst[i]:
            index = index - lst[i]
        else:
            return i


class Gene:
    def __init__(self):
        random.seed()
        self.mass = float(random.randint(3,10))
        self.vx = float(random.randint(-5,20))
        self.vy = float(random.randint(-40,0))

    @classmethod
    def modified(cls,mass,vx,vy):
        self.mass = mass
        self.vx = vx
        self.vy = vy

class Ball:

    gravity = (0,0.3)
    radius = 8

    def __init__(self, gene):
        self.gene = gene
        self.mass = gene.mass
        self.vel = np.array([gene.vx,gene.vy])
        self.pos = (50,550)
        self.life = 255
        self.color = (255,100,0)
        # self.prev_vy = vy
        # self.count = 0
        self.board_hit = False
        self.target_hit = False
        self.dist_board = 1000
        self.dist_target = 1000
        self.fitness = 0

    def boundary(self):
        if self.pos[0] > 800 - self.radius:
            self.vel[0] = -0.8*self.vel[0]
            self.pos[0] = 800 - self.radius
        if self.pos[1] > 600 - self.radius:
            # self.vel[1] = -0.8*self.vel[1]
            self.vel[1]= 0
            self.pos[1] = 600 - self.radius
            self.life = 0
        if self.pos[0] < 0 + self.radius:
            self.vel[0] = -0.8*self.vel[0]
            self.pos[0] = 0 + self.radius
        if self.pos[1] < 0 + self.radius:
            self.vel[1] = -0.8*self.vel[1]
            self.pos[1] = 0 + self.radius

    # def calc_life(self):
    #     if (int(self.vel[1]) == int(self.prev_vy)):
    #         self.count = self.count + 1
    #     else:
    #         self.count = 0
    #
    #     if self.count > 0:
    #         self.life = self.life - 5
    #
    #     if self.life < 0:
    #         self.life = 0

    """ get_Fitness() will evaluate the fitness level of a ball
        if ball.hit_board:
            fitness = 1 / (dist from board)
        else
            fitness = 1 + 1 / (dist from target) """
    def get_fitness(self):
        if not self.board_hit:
            fitness = 1 / self.dist_board
            if fitness > self.fitness:
                self.fitness = fitness
        else:
            fitness = 1 + 1 / self.dist_target
            if fitness > self.fitness:
                self.fitness = fitness

    def update(self):
        self.prev_vy = self.vel[1]
        self.vel = self.vel + np.multiply(self.mass, self.gravity)
        self.pos = self.pos + self.vel
        self.boundary()
        # self.calc_life()

    def draw(self, screen):
        pos = [int(self.pos[0]),int(self.pos[1])]
        if (self.board_hit):
            self.color = (255,0,255)
        else:
            self.color = (255,100,0)
        if (self.life != 0):
            pygame.draw.circle(screen, self.color, pos, self.radius)

class Generation:
    def __init__(self, num, board, screen, target, genes):
        self.board = board
        self.balls = []
        self.num = num
        self.screen = screen
        self.target = target
        self.results = []
        self.mutation = 0
        self.genes = genes
        if self.genes == []:
            for i in range(num):
                gene = Gene()
                self.balls.append(Ball(gene))
        else:
            for i in range(num):
                gene = genes[i]
                self.balls.append(Ball(gene))

    def run(self):
        pygame.draw.rect(self.screen, (255,255,255), [45,545,10,10], 2)
        for i in range(self.num):
            self.balls[i].update()
            self.board.check_collide(self.balls[i])
            self.target.check_hit(self.balls[i])
            self.balls[i].draw(self.screen)
            self.balls[i].get_fitness()

    def is_dead(self):
        for b in self.balls:
            if b.life != 0:
                return False
        return True

    ''' evaluate() will return list of fitness '''
    def evaluate(self):
        self.results = []
        for b in self.balls:
            b.get_fitness()
            self.results.append(b.fitness)
        return self.results


    def cross_over(self, gene1, gene2):
        random.seed()
        check1 = random.random()
        if check1 < self.mutation:
            modified = Gene()
        else:
            random.seed()
            check2 = random.random()
            check3 = random.random()
            check4 = random.random()
            if check2 < 0.5:
                new_mass = gene1.mass + random.random()
            else:
                new_mass = gene2.mass

            if check3 < 0.5:
                new_vx = gene1.vx + random.random()
            else:
                new_vx = gene2.vx

            if check4 < 0.5:
                new_vy = gene1.vy + random.random()
            else:
                new_vy = gene2.vy

            modified = Gene()
            modified.mass = new_mass
            modified.vx = new_vx
            modified.vy = new_vy

        return modified


    ''' natural_selection() will return list of new genes '''
    def natural_selection(self):
        fitness = self.evaluate()
        fix_fitness = [x+0.0001 for x in fitness]
        sum_fit = sum(fix_fitness)
        norm_fitness = [float(x)/sum_fit for x in fix_fitness]
        max_fitness = max(norm_fitness)
        for i in range(len(norm_fitness)):
            if norm_fitness[i] == max_fitness:
                best_gene = self.balls[i].gene

        rand_index = []

        while len(rand_index) < 2:
            index = random.random()
            temp = CDF(index, norm_fitness)

            if not temp in rand_index:
                rand_index.append(self.balls[temp].gene)

        genes = []

        for i in range(len(self.balls)-1):
            gene = self.cross_over(rand_index[0], rand_index[1])
            genes.append(gene)
            print(gene.mass, gene.vx, gene.vy)
        genes.append(best_gene)
        return genes

    def set_mutation(self, mutation):
        self.mutation = mutation

    def count_success1(self):
        count = 0
        for b in self.balls:
            if b.board_hit:
                count += 1
        return count

    def count_success2(self):
        count = 0
        for b in self.balls:
            if b.target_hit:
                count += 1
        return count
