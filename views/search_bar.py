from ttkbootstrap import Frame, Button, Label, Entry
from tkinter import Widget, StringVar
from views.asset_image import AssetImage
from threading import Thread

class SearchBar(Frame):
    def __init__(self, root: Widget, on_search: callable):
        super().__init__(root)
        self.on_search = on_search
        self.search_text = StringVar(self)
        self.icon =  AssetImage('./assets/icon.jpg', (100, 100))
        header_frame = Frame(self)
        Label(header_frame, image = self.icon).pack(side = 'left')
        Label(header_frame, text='YouTube Downloader', font = ('Arial', 25)).pack(padx = 5, side = 'left')
        header_frame.pack()
        Entry(self, textvariable = self.search_text, width = 60).pack(pady = 15)
        Button(self, text = 'Check', command = self.search).pack()
    
    def search(self):
        Thread(target = lambda: self.on_search(self.search_text.get())).start()