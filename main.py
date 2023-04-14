from tkinter import Label, Tk

import settings
import utils
from cell import Cell
from components.frames import Frames
from components.gameboard import GameBoard
from components.menu import MenuBar

root = Tk()
# override the settings of the root window
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper")
root.resizable(False, False)

frames = Frames(root)
frames.place_frames()

game_title = Label(
    frames.top_frame,
    text="PySweeper",
    font=("", 30),
    bg="black",
    fg="white",
)

game_title.place(x=settings.WIDTH / 2, y=50, anchor="center")


# add the menu bar
menubar = MenuBar(root)
root.config(menu=menubar)

# create the game board
game_board = GameBoard(frames.center_frame)
game_board.reset_board()
game_board.randomize_mines()

# setup the cell-count label
Cell.create_cell_count_label(frames.left_frame)
Cell.cell_count_label_object.place(x=0, y=0)  # type: ignore


# run the window's main loop
root.mainloop()
