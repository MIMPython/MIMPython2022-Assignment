from turtle import color
import numpy as np
import pygame


"""
Cells: live or dead.
Every cell interacts with its eight neighbours:
    - Any live cell with fewer than 2 live neighbours dies.
    - Any live cell with 2 or 3 live neighbours lives on to the next.
    - Any live cell with more than 3 live neighbours dies.
    - Any dead cell with exactly 3 live neighbours becomes a live cell.
    (or simply:
    - Any live cell with 2 or 3 live neighbours survives.
    - Any dead cell with three live neighbours becomes a live cell.
    - All other live cells die in the next generation (all other dead cells stay dead).)
"""


screenWidth = 1500
screenHeight = 1000
cellSize = 100
cellNumberByWidth = int(screenWidth / cellSize)
cellNumberByHeight = int(screenHeight / cellSize)


def checkLiveOrDead(currentField, row, column):
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(column - 1, column + 2):
            if currentField[i][j]:
                count += 1

    """
    - Any live cell with 2 or 3 live neighbours survives.
    - Any dead cell with three live neighbours becomes a live cell.
    - All other live cells die in the next generation (all other dead cells stay dead).
    """
    if currentField[row][column]:
        count = count - 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


def colorCell(screen, color, row, column):
    pygame.draw.rect(
        screen,
        pygame.Color(color),
        (
            row * cellSize + 2,
            column * cellSize + 2,
            cellSize - 2,
            cellSize - 2,
        ),
    )


def main():
    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()

    screen.fill(pygame.Color("black"))
    for i in range(0, screenWidth, cellSize):
        pygame.draw.line(screen, pygame.Color("gray"), (i, 0), (i, screenHeight))
    for j in range(0, screenHeight, cellSize):
        pygame.draw.line(screen, pygame.Color("gray"), (0, j), (screenWidth, j))

    pygame.display.update()

    # currentField = np.random.randint(2, size=(cellNumberByHeight, cellNumberByWidth))
    currentField = np.zeros((cellNumberByHeight, cellNumberByWidth))
    for i in range(cellNumberByHeight):
        for j in range(cellNumberByWidth):
            if (i * j) % 28 == 0:
                currentField[i][j] = 1
    nextField = np.zeros((cellNumberByHeight, cellNumberByWidth))

    pause = False
    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_RETURN:
                    running = not running
                if event.key == pygame.K_SPACE:
                    pause = not pause

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = pygame.mouse.get_pos()
                currentField[
                    mousePosition[1] // cellSize, mousePosition[0] // cellSize
                ] = 1
                colorCell(
                    screen,
                    "white",
                    mousePosition[1] // cellSize,
                    mousePosition[0] // cellSize,
                )
                pygame.display.update()

        if running:
            if not pause:
                for row in range(1, cellNumberByHeight - 1):
                    for column in range(1, cellNumberByWidth - 1):
                        if currentField[row][column]:
                            colorCell(screen, "white", row, column)
                        else:
                            colorCell(screen, "black", row, column)
                        nextField[row][column] = checkLiveOrDead(
                            currentField, row, column
                        )

                currentField = nextField[::]
                pygame.display.update()
                clock.tick(10)


if __name__ == "__main__":
    main()
