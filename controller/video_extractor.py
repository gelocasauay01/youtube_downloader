import yt_dlp as ytdl

class VideoExtractor:
    def __init__(self, options: dict, url: str):
        self.downloader = ytdl.YoutubeDL(options)
        self.metadata = self.downloader.extract_info(url, download = False)
        self.url = url
    
    def download(self):
        self.downloader.download([self.url])