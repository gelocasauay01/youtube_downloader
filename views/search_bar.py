from ttkbootstrap import Frame, Button, Label, Entry
from tkinter import Widget, StringVar
from threading import Thread

class SearchBar(Frame):
    def __init__(self, root: Widget, on_search: callable):
        super().__init__(root)
        self.search_text = StringVar(self)
        self.on_search = on_search
        Label(self, text='YouTube Downloader', font = ('Arial', 25)).pack()
        Entry(self, textvariable = self.search_text, width = 60).pack(pady = 15)
        Button(self, text = 'Check', command = self.search).pack()
    
    def search(self):
        Thread(target = lambda: self.on_search(self.search_text.get())).start()