import random
from tkinter import Button

import settings


class Cell:
    all = []

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object: None | Button = None
        self.x = x
        self.y = y

        # Append the object to the list of all cells
        Cell.all.append(self)

    def __repr__(self) -> str:
        return f"Cell({self.x}, {self.y})"

    def create_btn_object(self, location):
        btn = Button(location, width=12, height=4)
        btn.bind("<Button-1>", self.left_click_actions)
        btn.bind("<Button-3>", self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def get_cell_by_axis(self, x, y):
        # return a cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounding_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]
        return [cell for cell in cells if cell is not None]

    @property
    def surrounding_cells_mines_count(self):
        return sum([1 for cell in self.surrounding_cells if cell.is_mine])

    def show_cell(self):
        self.cell_btn_object.configure(text=self.surrounding_cells_mines_count)

    def show_mine(self):
        # a logic to interrupt game and display a message that the player has
        # lost
        self.cell_btn_object.configure(bg="red")

    def right_click_actions(self, event):
        print(event)
        print("Right CLick")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for cell in picked_cells:
            cell.is_mine = True
