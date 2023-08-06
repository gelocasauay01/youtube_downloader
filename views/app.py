from ttkbootstrap import Window
from views.main_screen import MainScreen

class App(Window):
    def __init__(self, size: tuple, title: str):
        super().__init__(themename = 'superhero')
        width = size[0]
        height = size[1]
        self.title(title)
        self.geometry(f"{width}x{height}")
        MainScreen(self).pack(expand = True, fill = 'both')

    def run(self):
        self.mainloop()