import pygame
import sys
from cell import Cell

""" This is the main file you work on for the project"""
# We want to create a mine sweeper game, where the user can click on cells to reveal them.
# The game is over when the user clicks on a bomb. The user can also flag cells that they think are bombs.
# The user wins when all cells that are not bombs are revealed.
# Sorrounding bombs will be indicated when clicking a cell, but only upp to two cells away.

pygame.init()

SCREEN_MIN_SIZE = 750  # Can be made to autoadjust after % of ur screen
amount_of_cells = 16  # The amount of cells is equal in rows and columns, 16x16 (LOCKED)
bomb_chance = 0.10  # Change to prefered value or use default 0.25

CELL_SIZE = SCREEN_MIN_SIZE // amount_of_cells
READJUSTED_SIZE = CELL_SIZE * amount_of_cells
CELL_WIDTH = CELL_HEIGHT = CELL_SIZE  # Probably not needed, just use cell_size

SCREEN_WIDTH, SCREEN_HEIGHT = READJUSTED_SIZE, READJUSTED_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("MineSweeper")

cells = []


def count_neighbouring_bombs(row, col):
    count = 0
    cell_range = range(amount_of_cells)
    for n_row in range(row - 1, row + 2):
        if n_row not in cell_range:
            continue
        for n_col in range(col - 1, col + 2):
            if n_col not in cell_range:
                continue
            # Skip self
            if row == n_row and col == n_col:
                continue
            count += cells[n_row][n_col].bomb
    return count


def create_cells():
    """This function is meant to initialy generate all the cells and create the boundaries"""
    cell_range = range(amount_of_cells)
    for a_row in cell_range:
        row_list = []
        for a_column in cell_range:
            row_list.append(
                Cell(
                    a_column * CELL_SIZE,
                    a_row * CELL_SIZE,
                    CELL_WIDTH,
                    CELL_HEIGHT,
                    bomb_chance,
                )
            )
        cells.append(row_list)
    for row in cell_range:
        for col in cell_range:
            cells[row][col].neighbouring_bombs = count_neighbouring_bombs(row, col)


def draw_cells():
    """In this function we want to draw each cell, i.e call upon each cells .draw() method!"""
    for row in cells:
        for cell in row:
            cell.draw(screen)


def reveal_cell(row, col):
    clicked_cell = cells[row][col]
    clicked_cell.reveal_cell(row, col, cells, amount_of_cells)


def check_win_condition():
    revealed_cells = sum(
        1 for row in cells for cell in row if cell.revealed and not cell.bomb
    )
    non_bomb_cells = amount_of_cells * amount_of_cells - int(
        amount_of_cells * amount_of_cells * bomb_chance
    )
    if revealed_cells == non_bomb_cells:
        print("Congratulations! You've won!")


def draw():
    """This function handles all the drawings to the screen, such as drawing rectangles, objects etc"""
    draw_cells()


def event_handler(event):
    if event.type == pygame.QUIT:
        terminate_program()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        row = y // CELL_SIZE
        col = x // CELL_SIZE
        if 0 <= row < amount_of_cells and 0 <= col < amount_of_cells:
            reveal_cell(row, col)


def run_setup():
    """This function is meant to run all code that is neccesary to setup the app, happends only once"""
    create_cells()


def terminate_program():
    """Functionality to call on whenever you want to terminate the program"""
    pygame.quit()
    sys.exit()


def main():
    run_setup()

    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            event_handler(event)

        draw_cells()
        check_win_condition()
        pygame.display.update()


if __name__ == "__main__":
    main()
