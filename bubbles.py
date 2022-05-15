import sys, pygame
pygame.init()
import random
import math

size = width, height = 800, 600
black = 0, 0, 0

def getRandomColor(seed):
    random.seed(seed)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color

class Bubble():
    def __init__(self, seed):
        self.color = getRandomColor(seed)
        self.size = 30
        self.karma = 30
        self.pos = (random.randint(0,800), random.randint(0,600))
        self.moveVector = [0, 0]

    def moveAway(self, position, dist):
        x, y = position

        xdiff = x - self.pos[0]
        ydiff = y - self.pos[1]

        total_dist = math.sqrt(xdiff**2 + ydiff**2)

        self.moveVector[0] += xdiff * dist / total_dist
        self.moveVector[1] += ydiff * dist / total_dist

    def drawSelf(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.size)

    def update(self):
        x, y = self.pos
        dx = self.moveVector[0] / 2
        dy = self.moveVector[1] / 2

        x += dx
        y += dy

        self.moveVector[0] /= 2
        self.moveVector[1] /= 2

        self.pos = (x, y)

class BubbleMap():
    def __init__(self, N):
        self.N = N
        self.bubbles = [Bubble(i) for i in range(N)]
        self.size_factor = 1

    def update(self):
        count_side_collisions = 0
        for i in range(self.N):
            for j in range(i+1, self.N):
                dist = self.get_dist(i, j)
                min_dist = (self.bubbles[i].size + self.bubbles[j].size)
                if dist < min_dist:
                    self.bubbles[i].moveAway(self.bubbles[j].pos, dist - min_dist)
                    self.bubbles[j].moveAway(self.bubbles[i].pos, dist - min_dist)
            if self.bubbles[i].pos[0] < self.bubbles[i].size:
                self.bubbles[i].moveVector[0] += self.bubbles[i].size - self.bubbles[i].pos[0] + 1
                count_side_collisions += 1
            if 800 - self.bubbles[i].pos[0] < self.bubbles[i].size:
                self.bubbles[i].moveVector[0] += 800 - self.bubbles[i].pos[0] - self.bubbles[i].size - 1
                count_side_collisions += 1
            if self.bubbles[i].pos[1] < self.bubbles[i].size:
                self.bubbles[i].moveVector[1] += self.bubbles[i].size - self.bubbles[i].pos[1] + 1
                count_side_collisions += 1
            if 600 - self.bubbles[i].pos[1] < self.bubbles[i].size:
                self.bubbles[i].moveVector[1] += 600 - self.bubbles[i].pos[1] - self.bubbles[i].size - 1
                count_side_collisions += 1

        self.size_factor += 0.01
        if count_side_collisions > 16:
            self.size_factor -= 0.02

        for b in self.bubbles:
            b.size = self.size_factor * b.karma
            if random.random() < 0.5:
                b.karma *= 1.001
            else:
                b.karma /= 1.001
            b.update()

        return None

    def get_dist(self, i, j):
        x1, y1 = self.bubbles[i].pos
        x2, y2 = self.bubbles[j].pos

        return math.sqrt( (x1 - x2)**2 + (y1 - y2)**2)

    def display(self, screen):
        for b in self.bubbles:
            b.drawSelf(screen)

bMap = BubbleMap(100)
ticks_threshold = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ticks = pygame.time.get_ticks()
    if ticks > ticks_threshold:
        ticks_threshold += 100
        bMap.update()

    screen = pygame.display.set_mode(size)
    screen.fill(black)
    bMap.display(screen)
    pygame.display.flip()
