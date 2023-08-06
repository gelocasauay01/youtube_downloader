class VideoPreview:
    def __init__(self, title: str, thumbnail_url: str, duration: int, path: str):
        self.title = title
        self.thumbnail_url = thumbnail_url
        self.duration = duration
        self.path = path
    
    def get_formatted_duration(self):
        hours = self.duration // 3600
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{hours:02d} : {minutes:02d} : {seconds:02d}"