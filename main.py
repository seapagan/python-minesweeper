from tkinter import Frame, Tk

import settings
import utils

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

# run the window's main loop
root.mainloop()
