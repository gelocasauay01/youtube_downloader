from PIL import ImageTk, Image

class AssetImage(ImageTk.PhotoImage):
    def __init__(self, path: str, size: tuple = None):
        raw_image = Image.open(path)
        if size != None:
            raw_image.thumbnail(size, Image.ANTIALIAS)
        super().__init__(raw_image)