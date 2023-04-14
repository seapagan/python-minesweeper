"""Create And control the menu bar."""
from tkinter import Menu


class MenuBar(Menu):
    """Create And control the menu bar."""

    def __init__(self, parent):
        """Create And control the menu bar."""
        super().__init__(parent)
        self.parent = parent
        self.filemenu = Menu(self, tearoff=0)
        self.filemenu.add_command(label="New Game")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.parent.quit)
        self.add_cascade(label="File", menu=self.filemenu)
