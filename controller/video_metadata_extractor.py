import yt_dlp as ytdl

class VideoMetadataExtractor:
    def __init__(self, url: str):
        self.url = url
        self.extractor = ytdl.YoutubeDL({})
        self.metadata = self.extractor.extract_info(url, download = False)
 