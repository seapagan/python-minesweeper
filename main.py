from tkinter import Label, Tk

import settings
import utils
from cell import Cell
from components.frames import Frames
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
    text="Minesweeper Game",
    font=("", 30),
    bg="black",
    fg="white",
)
game_title.place(x=utils.width_prct(25), y=0)

# add the menu bar
menubar = MenuBar(root)
root.config(menu=menubar)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(frames.center_frame)
        c.create_btn_object(frames.center_frame)
        c.cell_btn_object.grid(
            column=x,
            row=y,
        )

# call the label from the cell class
Cell.create_cell_count_label(frames.left_frame)
Cell.cell_count_label_object.place(x=0, y=0)
Cell.randomize_mines()


# run the window's main loop
root.mainloop()
