import numpy as np
import pygame

# initialising pygame
pygame.init()

# setting up constants
width = 600
height = 600
grid_size = 10
cell_size = width // grid_size

# creating a 10 x 10 grid
grid = np.zeros((grid_size, grid_size))     # this line means that an array of zeroes have been created in the dimensions of the grid. we are going to now fill in this grid with ones. 0 = free cell, 1 = obstacle present
grid [2,3] = 1                              # this line means that a 1 is placed at the coordinates (2,3) in the grid
grid [5,5:8] = 1                            # this line means that ones are placed from the coordinated (5,5) to (5,7)

# adding a start and finish
start = (0,0)                               # we are starting at the coordinates (0,0)
finish = (grid_size-1, grid_size-1)         # we are finishing at the coordinates (9,9)

# setting up pygame
screen = pygame.display.set_mode((width, height))       # setting up the screen with the width and height of 600px
pygame.display.set_caption("robot pathfinder")          # naming the window "robot pathfinder"
clock = pygame.time.Clock()                             # setting up a clock to keep track of time

# drawing the grid on the screen
def draw_grid():
    for y in range(grid_size):
        for x in range(grid_size):
            rectangle = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            colour = 'dark green' if grid[y,x] == 0 else 'red' 
            pygame.draw.rect(screen, colour, rectangle)
            pygame.draw.rect(screen, 'black', rectangle, 1)

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('white')
    draw_grid()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()