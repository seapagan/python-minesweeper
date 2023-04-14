import sys
from tkinter import Button, Label, messagebox

import settings


class Cell:
    all = []
    cell_count = settings.CELLS_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_open = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
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

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg="black",
            fg="white",
            text=f"Cells Left: {Cell.cell_count}",
            font=("", 30),
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        assert self.cell_btn_object is not None
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounding_cells_mines_count == 0:
                for cell in self.surrounding_cells:
                    cell.show_cell()
            self.show_cell()
            # if the cell count is equal to number of mines, the player has won
            if Cell.cell_count == settings.MINES_COUNT:
                messagebox.showinfo(
                    "You Win", "Congratulations, you have won the game"
                )
                sys.exit()

        # cancel the left and right click events if cell is already open
        self.cell_btn_object.unbind("<Button-1>")
        self.cell_btn_object.unbind("<Button-3>")

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
        assert self.cell_btn_object is not None
        if not self.is_open:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(
                text=self.surrounding_cells_mines_count
            )
            # replace the text of cell count lable with newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left: {Cell.cell_count}"
                )
            # if this was a mine candidate, reset the background color
            self.cell_btn_object.configure(bg="gray85")
            # mark this cell as open
            self.is_open = True

    def show_mine(self):
        # a logic to interrupt game and display a message that the player has
        # lost
        assert self.cell_btn_object is not None
        self.cell_btn_object.configure(bg="red")
        messagebox.showinfo("Game Over", "You Clicked on a Mine!")
        sys.exit()

    def right_click_actions(self, event):
        assert self.cell_btn_object is not None
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg="orange")
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(bg="gray85")
            self.is_mine_candidate = False
