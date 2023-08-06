from tkinter import Widget
from ttkbootstrap import Frame, Label, Button
import models.video_preview as vp
from views.web_image import WebImage


class VideoPreview(Frame):
    def __init__(self, root: Widget, vp: vp.VideoPreview, on_download: callable):
        super().__init__(root)
        right_side = Frame(self)
        self.image = WebImage(vp.thumbnail_url, (100, 100))
        Label(self, image = self.image).pack(expand= True, fill = 'y',side = 'left')
        Label(right_side, text = vp.title, font=("Helvetica", 12, 'bold')).pack()
        Label(right_side, text = vp.get_formatted_duration()).pack()
        Button(right_side, text = 'Download', command = on_download).pack()
        right_side.pack(padx = 10)