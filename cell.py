import pygame
import random


class Cell:
    """This file contains the cell class representing each square in the game"""

    def __init__(self, x, y, width, height, bomb_chance):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (0, 64, 0)  # RGB color
        self.cell_thickness = 2
        self.neighbouring_bombs = 0
        self.selected = False
        self.revealed = False

        self.cell_center = (
            self.x + self.width // 2,
            self.y + self.width // 2,
        )  # useful for drawing
        self.bomb = (
            random.random() < bomb_chance
        )  # each cell has a chance of being a bomb

    def draw(self, screen):
        """This method is called in the main.py files draw_cells fkn"""
        # Hint: Should draw each cell, i.e something to do with pygame.draw.rect
        # Later on in the assignment it will do more as well such as drawing X for bombs or writing digits
        # Important: Remember that pygame starts with (0,0) coordinate in upper left corner!
        pygame.draw.rect(
            screen,
            self.color,
            (self.x, self.y, self.width, self.height),
            self.cell_thickness,
        )
        if self.revealed:
            font = pygame.font.Font(None, 36)
            text = font.render(
                "X" if self.bomb else str(self.neighbouring_bombs),
                True,
                (255, 0, 0) if self.bomb else (255, 255, 255),
            )
            text_rect = text.get_rect(
                center=(self.x + self.width // 2, self.y + self.height // 2)
            )
            screen.blit(text, text_rect)

    def reveal_as_neighbour(self, row, col, cells, amount_of_cells):
        if self.revealed:
            return
        self.revealed = True
        if self.neighbouring_bombs == 0:
            self.reveal_neighbouring_cells(row, col, cells, amount_of_cells)

    def reveal_neighbouring_cells(self, row, col, cells, amount_of_cells):
        cell_range = range(amount_of_cells)
        for i in range(-1, 2):
            neighbor_row = row + i
            if neighbor_row not in cell_range:
                continue
            for j in range(-1, 2):
                neighbor_col = col + j
                if neighbor_col not in cell_range:
                    continue
                neighbor_cell = cells[neighbor_row][neighbor_col]
                neighbor_cell.reveal_as_neighbour(
                    neighbor_row, neighbor_col, cells, amount_of_cells
                )

    def reveal_cell(self, row, col, cells, amount_of_cells):
        if self.revealed:
            return
        self.revealed = True
        if self.bomb:
            print("Game Over! You clicked on a bomb.")
            # You can add additional game over logic here if needed
        elif self.neighbouring_bombs == 0:
            self.reveal_neighbouring_cells(row, col, cells, amount_of_cells)
        else:
            print("Cell revealed!")
