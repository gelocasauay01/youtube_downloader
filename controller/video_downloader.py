import yt_dlp as ytdl

class VideoDownloader:
    def __init__(self, url: str, output_path: str, format: str, temp_name_identifier: str = None):
        self.url = url
        self.output_path = output_path
        self.format = format
        self.temp_name_identifier = temp_name_identifier
        if temp_name_identifier != None:
            self.downloader = ytdl.YoutubeDL({'outtmpl': f'{output_path}/%(title)s-{temp_name_identifier}.%(ext)s', 'format': format})
        else:
            self.downloader = ytdl.YoutubeDL({'outtmpl': f'{output_path}/%(title)s.%(ext)s', 'format': format})
    
    def download(self) -> str:
        metadata = self.downloader.extract_info(self.url)
        if self.temp_name_identifier != None:
            return f'{self.output_path}/{metadata["title"]}-{self.temp_name_identifier}.{self.format}'
        else:
            return f'{self.output_path}/{metadata["title"]}.{self.format}'
