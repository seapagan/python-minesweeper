from tkinter import Frame, Label, Menu, Tk

import settings
import utils
from cell import Cell

root = Tk()
# override the settings of the root window
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="black",
    width=settings.WIDTH,
    height=utils.height_prct(25),
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame, text="Minesweeper Game", font=("", 30), bg="black", fg="white"
)
game_title.place(x=utils.width_prct(25), y=0)

left_frame = Frame(
    bg="black",
    width=utils.width_prct(25),
    height=utils.height_prct(75),
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    bg="black",
    width=utils.width_prct(75),
    height=utils.height_prct(75),
)
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Game")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,
            row=y,
        )

# call the label from the cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)
Cell.randomize_mines()


# run the window's main loop
root.mainloop()
