
from tkinter import Widget
from ttkbootstrap import Frame, Label
from views.video_preview import VideoPreview
from views.search_bar import SearchBar
from views.downloads_list import DownloadsList
from models.video_search_preview import VideoSearchPreview
from controller.video_metadata_extractor import VideoMetadataExtractor
from threading import Thread

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
        Thread(target = lambda: self.download_list.add(self.extractor)).start()
        if not self.download_list.is_toggled:
            self.download_list.toggle()
        self.preview.pack_forget()
        self.preview = None
    
    def check_link(self, url: str):
        try:
            self.extractor = VideoMetadataExtractor(url)
            title = self.extractor.metadata['title']
            thumbnail = self.extractor.metadata['thumbnails'][0]['url']
            duration = int(self.extractor.metadata['formats'][0]['fragments'][0]['duration'])
            video_search_preview = VideoSearchPreview(title, thumbnail, duration)
        except:
            video_search_preview = None
        self.toggle_preview(video_search_preview)
    
    def toggle_preview(self, video_search_preview: VideoSearchPreview):
        if self.preview != None:
            self.preview.pack_forget()

        if video_search_preview != None:
            self.preview = VideoPreview(self.center_container, video_search_preview, self.initiate_download)
        else:
            self.preview = Label(self.center_container, text = 'Invalid Link', font = ('Helvetica', 18, 'bold'))
        self.preview.pack(pady = 50)
    
    
        
       
        


    
