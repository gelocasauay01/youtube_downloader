
from tkinter import Widget
from ttkbootstrap import Frame, Label
from views.video_preview import VideoPreview
from views.search_bar import SearchBar
from views.downloads_list import DownloadsList
import models.video_preview as vp
from controller.video_extractor import VideoExtractor
from views.download_item import DownloadItem

class MainScreen(Frame):
    def __init__(self, root: Widget):
        super().__init__(root)
        self.center_container = Frame(self)
        self.preview = None
        self.extractor = None
        self.download_list = DownloadsList(self, False)
        SearchBar(self.center_container, self.check_link).pack()
        self.center_container.place(relx = 0.5, rely = 0.5, anchor = 'center')
        self.download_list.place(relwidth = 0.45, relheight = 1, relx = 1.5, rely = 0.1, anchor = 'ne')

    def initiate_download(self):
        self.download_list.add(self.extractor)
        self.preview.pack_forget()
        self.preview = None
    
    def check_link(self, url: str):
        is_successful = True
        video_preview = None
        try:
            self.extractor = VideoExtractor({'outtmpl': './downloads/%(title)s-temp.%(ext)s', 'format': 'mp4'}, url)
            title = self.extractor.metadata['title']
            thumbnail = self.extractor.metadata['thumbnails'][0]['url']
            duration = int(self.extractor.metadata['formats'][0]['fragments'][0]['duration'])
            path = f'./downloads/{title}-temp.mp4'
            video_preview = vp.VideoPreview(title, thumbnail, duration, path)
        except:
            is_successful = False
        self.toggle_preview(is_successful, video_preview)
    
    def toggle_preview(self, is_successful: bool, video_preview: vp.VideoPreview):
        if self.preview != None:
            self.preview.pack_forget()

        if is_successful and video_preview != None:
            self.preview = VideoPreview(self.center_container, video_preview, self.initiate_download)
        else:
            self.preview = Label(self.center_container, text = 'Invalid Link', font = ('Helvetica', 18, 'bold'))
        self.preview.pack(pady = 50)
    
    
        
       
        


    
