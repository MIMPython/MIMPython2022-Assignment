import pygame
import numpy as np
import time

# Set color for background and cells
aboutDieColor = (238,180,180) 
aliveColor = (255, 255, 255)
backgroudColor = (0, 0, 0)

def update(screen, cells, size):
    newCells = np.zeros((cells.shape[0], cells.shape[1]))

    for i in range(cells.shape[0]):
        for j in range (cells.shape[1]):
            aliveNum = np.sum(cells[i-1:i+2, j-1:j+2]) - cells[i, j]
            # Any live cell with fewer than two live neighbours dies,
            # as if by underpopulation.
            # Any live cell with more than three live neighbours
            # dies, as if by overpopulation.
            if cells[i, j] == 1:
                if aliveNum < 2 or aliveNum > 3:
                    color = aboutDieColor
                # Any live cell with two or three live neighbours 
                # lives on to the next generation.
                else:
                    color = aliveColor
                    newCells[i, j] = 1
            # Any dead cell with exactly three live neighbours 
            # becomes a live cell, as if by reproduction.
            if cells[i, j] == 0 and aliveNum == 3:
                color = aliveColor
                newCells[i, j] = 1
                
            color = color if cells[i, j] == 1 else backgroudColor
            pygame.draw.rect(screen, 
                             color, 
                             (j*size, i*size, size-1, size-1))

    return newCells

def main():
    rows = 80
    cols = 128
    size = 10
    pygame.init()
    surface = pygame.display.set_mode((cols * size, rows * size))
    pygame.display.set_caption("Conway's Game of Life")

    cells = np.random.randint(2, size = (rows, cols))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        cells = update(surface, cells, size)
        pygame.display.update()
        time.sleep(0.01)

if __name__ == "__main__":
    main()