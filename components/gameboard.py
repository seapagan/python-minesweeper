import random

import settings
from cell import Cell


class GameBoard:
    def __init__(self, parent):
        self.parent = parent

    def reset_board(self):
        for x in range(settings.GRID_SIZE):
            for y in range(settings.GRID_SIZE):
                c = Cell(x, y)
                c.create_btn_object(self.parent)
                assert c.cell_btn_object is not None
                c.cell_btn_object.grid(
                    column=x,
                    row=y,
                )

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for cell in picked_cells:
            cell.is_mine = True
