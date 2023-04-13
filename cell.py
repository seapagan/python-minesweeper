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
        btn = Button(
            location,
            width=12,
            height=4,
        )
        btn.bind("<Button-1>", self.left_click_actions)
        btn.bind("<Button-3>", self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(event)
        print("Left CLick")

    def right_click_actions(self, event):
        print(event)
        print("Right CLick")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for cell in picked_cells:
            cell.is_mine = True
