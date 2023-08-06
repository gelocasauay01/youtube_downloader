from urllib.request import urlopen
from PIL import ImageTk, Image
from io import BytesIO

class WebImage(ImageTk.PhotoImage):
    def __init__(self, url: str, size: tuple = None):
        response = urlopen(url)
        raw_data = response.read()
        raw_image = Image.open(BytesIO(raw_data))
        if size != None:
            raw_image.thumbnail(size, Image.ANTIALIAS)
        super().__init__(raw_image)