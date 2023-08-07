import ffmpeg
import os
import yt_dlp as ytdl
import ttkbootstrap as tb
from threading import Thread
from tkinter import StringVar, HORIZONTAL, CENTER

class DownloadManager:
    def __init__(self):
        self.active_no = 0

    def download_and_compress_from_link(self, link: str):
        ydl_opts = {'outtmpl': '%(title)s-temp.%(ext)s', 'format': 'mp4'}
        with ytdl.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(link)
        downloaded = ffmpeg.input(f'{result["title"]}-temp.mp4')
        ffmpeg.output(downloaded, f'{result["title"]}.avi', **{'b:v': 200000, 'b:a': 192000, 'vcodec': 'mpeg4', 'vtag': 'xvid', 'vf':'scale=720:480'}).run()
        os.remove(f'{result["title"]}-temp.mp4')
        self.active_no -= 1
    
    def get_dl_status_message(self):
        if self.active_no == 1:
            return 'A video is still downloading'
        else:
            return f'There are {self.active_no + 1} videos still downloading'



def handle_download(manager: DownloadManager, link: str, queue: tb.Frame, dl_count: StringVar):
    manager.active_no += 1
    dl_count.set(manager.get_dl_status_message())
    queue.pack(pady=15)

    try:
        manager.download_and_compress_from_link(link)
    except:
        manager.active_no = manager.active_no - 1 if manager.active_no > 0 else 0

    if manager.active_no <= 0:
        queue.pack_forget()
    else:
        dl_count.set(manager.get_dl_status_message())
        
if __name__ == '__main__':
    dl_manager = DownloadManager()
    root = tb.Window(themename='journal')
    url = StringVar(root)
    dl_count = StringVar(root)
    content = tb.Frame(root)
    title = tb.Label(content, text='YouTube Video Downloader', font=('Helvetica', 25))
    text_field = tb.Entry(content, width=60, textvariable=url)
    queue_frame = tb.Frame(content)
    dl_count_lbl = tb.Label(queue_frame, textvariable=dl_count)
    dl_bar = tb.Progressbar(queue_frame, orient=HORIZONTAL, length=200, mode='indeterminate')
    download_btn = tb.Button(content, text='Download', command=lambda: Thread(target=lambda: handle_download(dl_manager, url.get(), queue_frame, dl_count)).start())

    root.title('YouTube Video Downloader')
    root.geometry('700x300')
    content.place(relx=0.5, rely=0.5, anchor=CENTER)
    title.pack()
    text_field.insert(0, 'Enter URL Here')
    text_field.pack(pady=15)  
    dl_count_lbl.pack()
    dl_bar.pack()  
    dl_bar.start(20)
    download_btn.pack()

    root.mainloop()
