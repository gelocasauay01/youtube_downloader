from tkinter import Widget
from ttkbootstrap import Frame, Label, Button
from models.video_search_preview import VideoSearchPreview
from views.web_image import WebImage


class VideoPreview(Frame):
    def __init__(self, root: Widget, video_search_preview: VideoSearchPreview, on_download: callable):
        super().__init__(root)
        font_size = 8 if len(video_search_preview.title) >= 20 else 10
        right_side = Frame(self)
        self.image = WebImage(video_search_preview.thumbnail_url, (100, 100))
        Label(self, image = self.image).pack(expand= True, fill = 'y',side = 'left')
        Label(right_side, text = video_search_preview.title, font=("Helvetica", font_size, 'bold')).pack()
        Label(right_side, text = video_search_preview.get_formatted_duration()).pack()
        Button(right_side, text = 'Download', command = on_download).pack()
        right_side.pack(padx = 10)