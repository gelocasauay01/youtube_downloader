from ttkbootstrap import Frame, Label, Progressbar
from tkinter import Widget, StringVar
from views.web_image import WebImage
from controller.video_metadata_extractor import VideoMetadataExtractor
from controller.video_downloader import VideoDownloader
from controller.compressor import Compressor
from threading import Thread
import os.path as path

class ProcessItem(Frame):
    def __init__(self, root: Widget, extractor: VideoMetadataExtractor, downloader: VideoDownloader):
        super().__init__(root)
        self.extractor = extractor
        self.downloader = downloader
        title = self.extractor.metadata['title']
        thumbnail = self.extractor.metadata['thumbnails'][0]['url']
        font_size = 8 if len(title) >= 25 else 10
        self.status = StringVar(self)
        self.image = WebImage(thumbnail, (100, 100))
        Label(self, image = self.image).pack(side = 'left')
        Label(self, text = title, font = ('Helvetica', font_size, 'bold')).pack()
        Label(self, textvariable = self.status).pack()
        self.bar = Progressbar(self, mode = 'indeterminate')
        self.bar.pack()
        self.bar.start(20)
        Thread(target = self.process_item).start()
    
    def process_item(self):
        try:
            output_path = self.download()
            self.compress(output_path,)
            self.status.set('Process Complete')
        except:
            self.status.set('An Error Occurred')
        self.bar.pack_forget()
    
    def download(self) -> str:
        self.status.set('Downloading')
        return self.downloader.download()
    
    def compress(self, input_path: str):
        self.status.set('Compressing')
        output_path = path.join(path.dirname(input_path), f'{self.extractor.metadata["title"]}.avi')
        compressor = Compressor(input_path, output_path)
        compressor.compress()