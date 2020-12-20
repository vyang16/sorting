import pygame
import sorting
import argparse
import sys
import random
import numpy as np

WIDTH = 1024
HEIGHT = 512

BACKGROUND_COLOR = '#ebd834'
BAR_COLOR = '#4290f5'
CHANGE_COLOR = '#f55d42'

SPACING = 0.8

ALGORITHMS = sorting.ALGORITHMS


def initialize(n, name):
    if name == 'counting_sort':
        elements = (np.random.choice(n // 4, n) + 1).tolist()
    else:
        elements = random.sample(range(1, n+1), n)
    
    sort_iter = iter(ALGORITHMS[name](elements))
    return elements, sort_iter

def game_loop(n, algorithmName):
    pygame.font.init()
    pygame.display.set_caption(algorithmName) 

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(pygame.Color(BACKGROUND_COLOR))

    elements, sort_iter = initialize(n, algorithmName)
    idle = True
    finish = False
    while True:
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            idle = not idle

        # run step
        if keys[pygame.K_RIGHT]:
            if not finish and idle:
                i, special = next(sort_iter)  
                update(screen, elements, special)
                if i == -1:
                    finish = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        if not idle:
            if not finish:
                i, special = next(sort_iter)  
                update(screen, elements, special)

                if(i == -1):
                    finish = True
                    idle = True
            else:
                elements, sort_iter = initialize(n, algorithmName) 
                finish = False
                idle = True
    
        pygame.display.update()
        pygame.time.delay(50)

def update(screen, array, special=None):
    screen.fill(BACKGROUND_COLOR)
    n = len(array)
    h = WIDTH / n
    b = HEIGHT / max(array)
    for i in range(len(array)):
        pygame.draw.rect(screen, BAR_COLOR, (i*h, 0, h * SPACING, array[i] * b))
    
    # draw elements that are currently changed
    if special is not None:
        for i in special:
            pygame.draw.rect(screen, CHANGE_COLOR, (i*h, 0, h * SPACING, array[i] * b))


def main():
    p = argparse.ArgumentParser()
    p.add_argument('-n', type=int, default=50, help='Number of elements to be sorted')
    p.add_argument('-a', type=str, default='selection_sort', help='Sorting algorithm:\n' + str(ALGORITHMS.keys()))
    args = p.parse_args()

    game_loop(args.n, args.a)


if __name__=='__main__':
    main()