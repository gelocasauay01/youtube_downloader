from ttkbootstrap import Frame, Label, Progressbar
from tkinter import Widget, StringVar
from views.web_image import WebImage
from controller.video_extractor import VideoExtractor
from controller.compressor import Compressor

class DownloadItem(Frame):
    def __init__(self, root: Widget, extractor: VideoExtractor, compressor: Compressor):
        super().__init__(root)
        self.extractor = extractor
        self.compressor = compressor
        title = extractor.metadata['title']
        thumbnail = extractor.metadata['thumbnails'][0]['url']
        self.status = StringVar(self)
        self.image = WebImage(thumbnail, (100, 100))
        Label(self, image = self.image).pack(side = 'left')
        Label(self, text = title, font = ('Helvetica', 12, 'bold')).pack()
        Label(self, textvariable = self.status).pack()
        self.bar = Progressbar(self, mode = 'indeterminate')
        self.bar.pack()
        self.bar.start(20)
    
    def process_item(self):
        self.download()
        self.compress()
        self.status.set('Process Complete')
        self.bar.pack_forget()
    
    def download(self):
        self.status.set('Downloading')
        self.extractor.download()
    
    def compress(self):
        self.status.set('Compressing')
        self.compressor.compress()