from ttkbootstrap import Frame, Button, Label
from tkinter import Widget, StringVar
from views.process_item import ProcessItem
from time import sleep
from threading import Thread
from controller.video_metadata_extractor import VideoMetadataExtractor
from controller.video_downloader import VideoDownloader
from controller.compressor import Compressor

class DownloadsList(Frame):
    def __init__(self, root: Widget, is_toggled: bool = False):
        super().__init__(root, borderwidth=2, relief='flat')
        self.is_toggled = is_toggled
        self.has_downloads = False
        self.moving_container_curr_x = 1 if is_toggled else 1.5
        self.toggle_label = StringVar(self, 'Show All')
        self.no_downloads = Label(self, text = 'No Downloads Yet', anchor = 'center', font = ('Helvetica', 15, 'bold'))
        self.no_downloads.pack(expand = True, fill = 'both')
        self.toggle_button = Button(root, textvariable = self.toggle_label, command = self.toggle)
        self.toggle_button.place(relheight = 0.05, relwidth = 0.1, relx = 1, rely = 0, anchor = 'ne')

    def add(self, extractor: VideoMetadataExtractor):
        if not self.has_downloads:
            self.no_downloads.pack_forget()
        downloader = VideoDownloader(extractor.url, './downloads', 'mp4', 'temp')
        ProcessItem(self, extractor, downloader).pack(padx = 10, pady = 5)
        self.has_downloads = True

    def animate_placement(self, target: float):
        is_increasing = target > self.moving_container_curr_x 
        increment = 0.1 if is_increasing else -0.1
        while (is_increasing and self.moving_container_curr_x < target) or (not is_increasing and self.moving_container_curr_x > target):
            self.moving_container_curr_x += increment
            self.place(relwidth = 0.45, relheight = 1, relx = self.moving_container_curr_x, rely = 0.1, anchor = 'ne')
            sleep(0.01)
        
    def toggle(self):
        target = 1
        if self.is_toggled:
            target = 1.5
        Thread(target = lambda: self.animate_placement(target)).start()
        self.is_toggled = not self.is_toggled
        self.toggle_label.set('Close' if self.is_toggled else 'Show All')

