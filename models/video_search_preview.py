from models.video_preview import VideoPreview

class VideoSearchPreview(VideoPreview):
    def __init__(self, title: str, thumbnail_url: str, duration: int):
        super().__init__(title, thumbnail_url)
        self.duration = duration
    
    def get_formatted_duration(self):
        hours = self.duration // 3600
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{hours:02d} : {minutes:02d} : {seconds:02d}"