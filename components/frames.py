# define the frames for the application
from tkinter import Frame

import settings
import utils


class Frames:
    def __init__(self, parent):
        self.parent = parent
        self.top_frame = Frame(
            parent,
            bg="red",
            width=settings.WIDTH,
            height=utils.height_prct(25),
        )
        self.left_frame = Frame(
            parent,
            bg="orange",
            width=utils.width_prct(25),
            height=utils.height_prct(75),
        )
        self.center_frame = Frame(
            parent,
            bg="green",
            width=utils.width_prct(75),
            height=utils.height_prct(75),
        )

    def place_frames(self):
        self.top_frame.place(x=0, y=0)
        self.left_frame.place(x=0, y=utils.height_prct(25))
        self.center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))
